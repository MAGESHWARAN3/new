from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy import create_engine, select,column
from app.database.database import engine,Base
from sqlalchemy import Table, Column, Integer, String

class Withdraw(Base):
    __tablename__ = 'withdraw'

    
    account_id=column(int ,foreign_key=True)
    amount= column(float)
