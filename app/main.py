from fastapi import FastAPI
from app.routers import users, payments, transactions
from app.database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Sistema de Pagos API REST")
app.include_router(users.router, prefix="/users")
app.include_router(payments.router, prefix="/payments", tags=["Payments"])
app.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])
@app.get("/") 
def read_root():
    return {"message": "Sistema de pagos API-REST!"}