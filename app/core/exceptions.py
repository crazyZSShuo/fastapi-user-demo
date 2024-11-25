from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "code": exc.status_code,
            "message": exc.detail,
            "data": None
        }
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "code": status.HTTP_422_UNPROCESSABLE_ENTITY,
            "message": "Validation Error",
            "data": str(exc.errors())
        }
    ) 