from fastapi import APIRouter
from app.api.v1.endpoints import auth, health, users, admin

api_router = APIRouter()

api_router.include_router(auth.router, tags=["auth"])
api_router.include_router(health.router, tags=["health"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(
    admin.router, 
    prefix="/admin", 
    tags=["admin"]
)
