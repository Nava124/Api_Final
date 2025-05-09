from fastapi import APIRouter
router = APIRouter()

@router.post("/")
def create_transaction():
    return {"message": "Transaction created"}