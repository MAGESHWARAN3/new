from fastapi import FastAPI,APIRouter
from app.database.database import engine,Base
from app.api.admin.router import router as admin_router
from app.api.create.router import router as create_router
from app.api.loan.router import router as loan_router
from app.api.withdraw.router import router as withdraw_router

 
Base.metadata.create_all(bind=engine)
app=FastAPI()

app.include_router(admin_router)
app.include_router(create_router)
app.include_router(loan_router)
app.include_router(withdraw_router)