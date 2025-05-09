from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class TransactionCreate(BaseModel):
    user_id: int
    amount: float
    method: str = "card"


class PaymentCreate(BaseModel):
    user_id: int
    amount: float
    method: str = "card"
