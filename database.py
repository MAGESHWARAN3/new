from sqlalchemy.orm import  sessionmaker,declarative_base
from sqlalchemy import  create_engine
from app.database.database import engine,Base

# Database setup
URL_DATABASE = "mysql+pymysql://root:@localhost/project_db"
engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Create tables
Base.metadata.create_all(bind=engine)



