from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_DATABASE_URL = "postgresql://uu2z6538gcgk7emceidd:wSlJdLJ02Sxkx4ZK5dNbqR0AIVi7Uu@bjvr6fcz4godqoi9yo1p-postgresql.services.clever-cloud.com:5432/bjvr6fcz4godqoi9yo1p"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()