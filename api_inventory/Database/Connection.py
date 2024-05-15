import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DBConnection:
    def __init__(self):
        load_dotenv()

        port = os.getenv('DB.PORT_MYSQL')
        host = os.getenv('DB.HOST_MYSQL')
        database = os.getenv('DB.DATABASE_MYSQL')
        user = os.getenv('DB.USER_MYSQL')
        password = os.getenv('DB.PASSWORD_MYSQL')

        try:
            self.engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
            Base.metadata.create_all(self.engine)
            self.Session = sessionmaker(bind=self.engine)
            print("Successful connection to the db with MySQL")
        except Exception as e:
            print(f"Error connecting to db: {str(e)}")
            self.Session = None
    
    def get_session(self):
        if self.Session is not None:
            return self.Session()
        else:
            raise Exception("Could not establish connection to db")