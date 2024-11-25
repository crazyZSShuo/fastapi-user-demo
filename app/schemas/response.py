from typing import Generic, Optional, TypeVar
from pydantic import BaseModel

DataT = TypeVar('DataT')

class ResponseModel(BaseModel, Generic[DataT]):
    code: int = 200
    message: str = "Success"
    data: Optional[DataT] = None 