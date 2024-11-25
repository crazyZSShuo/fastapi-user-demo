from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api.deps import get_db, get_current_user
from app.core.response import success_response, error_response
from app.schemas.response import ResponseModel
from app.schemas.user import User, UserCreate
from app.services.user import create_user, get_user_by_email

router = APIRouter()

@router.post("/", response_model=ResponseModel[User])
async def create_new_user(
    user_in: UserCreate,
    db: Session = Depends(get_db)
):
    user = get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    user = create_user(db, user_in)
    return success_response(data=user)

@router.get("/me", response_model=ResponseModel[User])
async def read_current_user(
    current_user: User = Depends(get_current_user)
):
    return success_response(data=current_user)
