from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.config import settings
from app.core.security import create_access_token, verify_password
from app.core.response import success_response, error_response
from app.api.deps import get_db
from app.services.user import get_user_by_email
from app.schemas.token import Token
from app.schemas.response import ResponseModel

router = APIRouter()

@router.post(
    "/login", 
    response_model=ResponseModel[Token],
    summary="用户登录",
    description="使用邮箱和密码进行登录"
)
async def login(
    db: Annotated[Session, Depends(get_db)],
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    # 1. 查找用户
    user = get_user_by_email(db, email=form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误"
        )
    
    # 2. 验证密码
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误"
        )
    
    # 3. 验证用户状态
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="用户已被禁用"
        )
    
    # 4. 创建访问令牌
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, 
        expires_delta=access_token_expires
    )
    
    return success_response(
        data={
            "access_token": access_token, 
            "token_type": "bearer"
        },
        message="登录成功"
    )
