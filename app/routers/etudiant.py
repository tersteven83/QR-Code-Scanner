from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..services import etudiant as etudiant_service
from ..helpers.database import SessionLocal
from ..helpers import schemas


router = APIRouter(
    prefix="/etudiants",
    tags=["etudiants"]
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.Etudiant])
async def read_etudiants(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    etudiants = etudiant_service.get_all(db, skip=skip, limit=limit)
    return etudiants


@router.get("/{user_im}", response_model=schemas.Etudiant)
async def read_etudiant(im: str, db: Session = Depends(get_db)):
    etudiant = etudiant_service.get_by_im(db, im)
    if etudiant is None:
        raise HTTPException(status_code=404, detail="User not found")
    return etudiant
