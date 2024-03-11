from app.core.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(Config.PG_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
