from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./qr_code_app.db"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://qcode_app_user:p4ssw0rd@127.0.0.1/QCode_App_DB?charset=utf8mb4"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
