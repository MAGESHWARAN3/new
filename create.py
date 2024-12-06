from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy import  create_engine, select, column
from app.database.database import engine,Base
from sqlalchemy import Table, Column, Integer, String

class Create(Base):
    __tablename__ = 'create'
   
    name=column(str)
    aadhar_no=column(int)
    city=column(str)
    account_id=column(int,primary_key=True)
    total_amount=column(float)
    