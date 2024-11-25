from fastapi import APIRouter
from app.core.response import success_response
from app.schemas.response import ResponseModel
from typing import Dict

router = APIRouter()

@router.get("/health", response_model=ResponseModel[Dict])
async def health_check():
    return success_response(
        data={
            "status": "healthy",
            "version": "1.0.0"
        }
    )
