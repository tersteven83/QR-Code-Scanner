from typing import Union

from datetime import datetime
from pydantic import BaseModel, EmailStr


class QR_CodeBase(BaseModel):
    expire_date: datetime
    is_valid: bool = True
    data: str
    created_at: datetime


class QR_CodeCreate(QR_CodeBase):
    id_etudiant: int


class QR_Code(QR_CodeBase):
    id: int

    class Config:
        orm_mode = True


class EtudiantBase(BaseModel):
    nom: str
    prenom: str
    dob: datetime
    cin: Union[str, None] = None
    cin_date: Union[datetime, None] = None
    tel: str
    email: EmailStr
    adresse: str
    niveau: str
    parcours: str
    matricule: str
    annee_univ: str


class EtudiantCreate(EtudiantBase):
    pass


class EtudiantUpdate(EtudiantBase):
    pass


class Etudiant(EtudiantBase):
    id: int
    qrcode: Union[list[QR_Code], None] = None

    class Config:
        orm_mode = True


class OperateurBase(BaseModel):
    nom: str


class OperateurCreate(OperateurBase):
    hashed_password: str
    access_token: str


class Operateur(OperateurBase):
    id: int

    class Config:
        orm_mode = True


class JournalBase(BaseModel):
    operation: str
    effectue_par: Operateur
    etudiant: Etudiant
    date: datetime


class JournalCreate(JournalBase):
    pass


class Journal(JournalBase):
    id: int

    class Config:
        orm_mode = True
