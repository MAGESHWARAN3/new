from sqlalchemy import Table, Column, Integer, String, column 
from app.database.database import engine,Base
from typing import Annotated


class Admin(Base):
        __tablename__ = 'admin'

        name=column(str)
        user_name=column(str(index=True))
        password=column(str)



       