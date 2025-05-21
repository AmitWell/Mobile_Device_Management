# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # your real DATABASE_URL (e.g. from env)
# DATABASE_URL = f"postgresql://{config('POSTGRES_USER')}:{config('POSTGRES_PASSWORD')}@" \
#                f"{config('POSTGRES_HOST')}:{config('POSTGRES_PORT')}/{config('POSTGRES_DB_NAME')}"

# engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Base lives here, and nothing else imports models
# Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# app/database.py

from decouple import config           # ← add this line
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# now config() is defined
DATABASE_URL = (
    f"postgresql://{config('POSTGRES_USER')}:"
    f"{config('POSTGRES_PASSWORD')}@"
    f"{config('POSTGRES_HOST')}:{config('POSTGRES_PORT')}/"
    f"{config('POSTGRES_DB_NAME')}"
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
