from fastapi import FastAPI, HTTPException, Depends, status,APIRouter
from pydantic import BaseModel
from typing import Annotated
import models,schema
from sqlalchemy import engine
from sqlalchemy.orm import Session
from app.models.withdraw import Withdraw

from database.database import SessionLocal
import models.withdraw

router=APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
        
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]

@router.post("/withdraw/")
async def create_withdraw(withdraw:Withdraw, db: db_dependency):
    db_withdraw = models.withdraw(**withdraw.dict())
    db.add(db_withdraw)
    db.commit()


@router.get("/withdraw/{withdraw_account_id}")
async def read_withdraw(account_id:int, db: db_dependency):
   withdraw = db.query(models.withdraw).filter(Withdraw.account_id == account_id).first()
   if withdraw is None:
        raise HTTPException(status_code=404, detail='withdraw not found')
   return withdraw

@router.delete("/withdraw/{withdraw_account_id}")
async def delete_withdraw(account_id:int, db: db_dependency):
    db_withdraw = db.query(models.withdraw).filter(Withdraw.account_id == account_id).first()
    if db_withdraw is None:
        raise HTTPException(status_code=404, detail='withdraw was not found')
    db.delete(db_withdraw)
    db.commit()

