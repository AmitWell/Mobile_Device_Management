from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.rbac import Base

DATABASE_URL = "postgresql://user:password@localhost:5432/mdm_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
