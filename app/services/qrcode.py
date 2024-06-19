from sqlalchemy.orm import Session

from ..helpers import models, schemas


def create(db: Session, qcode: schemas.QR_CodeCreate):
    db_qrcode = models.QR_Code(qcode)
    db.add(db_qrcode)
    db.commit()
    db.refresh(db_qrcode)
    return db_qrcode


def delete(db: Session, identifiant: int):
    return db.query(models.QR_Code).filter(models.QR_Code.id == identifiant).delete()