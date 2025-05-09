from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models
from ..database import get_db

router = APIRouter()

@router.post("/")
def create_transaction(user_id: int, amount: float, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    # Validación básica de autorización
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Monto inválido")
    if amount > 5000:
        raise HTTPException(status_code=403, detail="Transacción no autorizada")

    transaction = models.Transaction(user_id=user_id, amount=amount)
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return {"transaction_id": transaction.id, "status": "success"}

@router.get("/user/{user_id}")
def get_user_transactions(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    transactions = db.query(models.Transaction).filter(models.Transaction.user_id == user_id).all()
    return [{"id": t.id, "amount": t.amount, "timestamp": t.timestamp} for t in transactions]
