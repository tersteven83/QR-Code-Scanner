import datetime
from typing import Type

from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select
from fastapi import HTTPException

from ..helpers import models, schemas


def create(db: Session, etudiant: schemas.EtudiantCreate):
    # Création du QR Code
    qrcode = schemas.QR_CodeCreate(created_at=datetime.datetime.now(), expire_date="2025-01-01", data="test_fotsiny",
                                   is_valid=True)
    etudiant_dict = {
        "nom": etudiant.nom,
        "prenom": etudiant.prenom,
        "dob": etudiant.dob,
        "cin": etudiant.cin,
        "cin_date": etudiant.cin_date,
        "tel": etudiant.tel,
        "email": etudiant.email,
        "matricule": etudiant.matricule,
        "adresse": etudiant.adresse,
        "parcours": etudiant.parcours,
        "niveau": etudiant.niveau,
        "annee_univ": etudiant.annee_univ,
        "qrcode": qrcode
    }
    db_etudiant = models.Etudiant(etudiant_dict)
    db.add(db_etudiant)
    db.commit()
    db.refresh(db_etudiant)
    return db_etudiant


def update(db: Session, matricule: str, etudiant_param: schemas.EtudiantUpdate):
    etudiant = get_by_im(matricule)
    db.query(etudiant).update(**etudiant_param.dict())
    db.commit()
    db.refresh(etudiant)
    return etudiant


def delete(db: Session, matricule: str):
    etudiant = get_by_im(matricule)
    return db.query(etudiant).delete()


def get_by_im(db: Session, im: int) -> Type[models.Etudiant]:
    etudiant = db.query(models.Etudiant).filter(models.Etudiant.matricule == im).first()
    if not etudiant:
        raise HTTPException(status_code=404, detail="Etudiant non trouvé")
    return etudiant


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Etudiant)\
        .offset(skip).limit(limit).all()
