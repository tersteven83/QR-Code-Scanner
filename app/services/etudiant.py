from datetime import datetime, timedelta
from pyexpat import model
from typing import Type

from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..helpers import models, schemas
from ..services import qrcode as qrcode_service


def create(db: Session, etudiant: schemas.EtudiantCreate):
    # Créer un étudiant
    db_etudiant = models.Etudiant(**etudiant.model_dump())
    db.add(db_etudiant)
    db.commit()
    db.refresh(db_etudiant)

    # créer un code QR pour ce dernier
    qcode_dict = {
        "id_etudiant": db_etudiant.id,
        "expire_date": datetime.now() + timedelta(days=365),
        "is_valid": True,
        "data": "test_fotsiny_anle_qr_code",
        "created_at": datetime.now()
    }
    db_qcode = models.QR_Code(**qcode_dict)
    db.add(db_qcode)
    # faire la transaction vers la BD
    db.commit()
    
    # Rafraîchir avant de retourner vers la route
    db.refresh(db_etudiant)
    return db_etudiant


def update(db: Session, matricule: str, etudiant_param: dict):
    db.query(models.Etudiant).filter(models.Etudiant.matricule == matricule)\
        .update(etudiant_param)
    db.commit()
    return get_by_im(db, matricule)


def delete(db: Session, matricule: str):
    etudiant = get_by_im(db, matricule)
    return db.query(etudiant).delete()


def get_by_im(db: Session, im: str) -> models.Etudiant:
    return db.query(models.Etudiant).filter(models.Etudiant.matricule == im).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Etudiant)\
        .offset(skip).limit(limit).all()


def get_by_cin(db: Session, cin: str):
    return db.query(models.Etudiant).filter(models.Etudiant.cin == cin).first()
