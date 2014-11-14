from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = 'mysql://root:lucidlinhxeonx128@localhost:3306/compsoc_auth'

engine = create_engine(DB_PATH, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()

def init_db():
	"""Create all the models in the database."""
	from models import *
	Base.metadata.create_all(bind=engine)
