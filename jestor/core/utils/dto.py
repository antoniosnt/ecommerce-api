from typing import Generic, Optional, TypeVar
from pydantic import Field, BaseModel
from pydantic.generics import GenericModel

T = TypeVar("T")


class ResponseDTO(GenericModel, Generic[T]):
    message: str = Field(
        description="Mensagem de resposta da requisição", example="success"
    )
    data: T = Field(description="Resposta da requisição")


class HttpErrorDTO(BaseModel):
    message: str = Field(description="Mensagem de erro da requisição")
    data: None = Field(description="Resposta de erro requisição", example=None)
