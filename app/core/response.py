from typing import Any, Optional
from fastapi.responses import JSONResponse
from fastapi import status

class ResponseHandler:
    @staticmethod
    def success(*, data: Any = None, message: str = "Success") -> dict:
        return {
            "code": status.HTTP_200_OK,
            "message": message,
            "data": data
        }

    @staticmethod
    def error(*, code: int = status.HTTP_400_BAD_REQUEST, message: str = "Error") -> dict:
        return {
            "code": code,
            "message": message,
            "data": None
        }

success_response = ResponseHandler.success
error_response = ResponseHandler.error 