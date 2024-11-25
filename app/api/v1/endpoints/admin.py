from typing import List, Dict
from fastapi import APIRouter
from app.api.deps import CurrentSuperUser
from app.core.response import success_response
from app.schemas.response import ResponseModel

router = APIRouter()

@router.get(
    "/system-info", 
    response_model=ResponseModel[Dict],
    summary="获取系统信息",
    description="获取系统相关信息，仅超级管理员可访问"
)
async def get_system_info(
    current_user: CurrentSuperUser  # 这里使用 CurrentSuperUser 依赖，确保只有超级管理员可以访问
):
    system_info = {
        "system_name": "FastAPI Admin System",
        "version": "1.0.0",
        "environment": "production",
        "database_status": "connected",
        "admin_user": {
            "id": current_user.id,
            "email": current_user.email,
            "is_superuser": current_user.is_superuser
        },
        "system_statistics": {
            "total_users": 100,
            "active_users": 85,
            "system_uptime": "7 days",
            "cpu_usage": "32%",
            "memory_usage": "45%"
        },
        "features": [
            "用户管理",
            "权限控制",
            "系统监控",
            "日志记录",
            "数据备份"
        ]
    }
    
    return success_response(
        data=system_info,
        message="系统信息获取成功"
    ) 