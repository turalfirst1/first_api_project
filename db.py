from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()
engine = create_engine(f"postgresql://{os.environ('pg_db_user')}:{os.environ('pg_db_pass')}@{os.environ('pg_db_host')}/item_db", 
                       echo = True)


Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)