from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy import create_engine, select,column
from app.database.database import engine,Base
from sqlalchemy import Table, Column, Integer, String


class Loan(Base):
    __tablename__ = 'loan'

    account_id=column(int , foreign_key=True)
    name=column(str)
    description=column(str)
