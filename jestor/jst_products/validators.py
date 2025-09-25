from typing import Optional
from decimal import Decimal
from pydantic import BaseModel, Field


class ProductDTO(BaseModel):
    nce: int = Field(description="Código de identificação do produto", example="1982")
    cd_color: int = Field(description="Código de identificação da cor", example="45")
    cd_marca: int = Field(description="Código de identificação da marca", example="23")
    na_product: str = Field(
        description="Título do produto", example="Geladeira Eletrolux"
    )
    na_description: str = Field(
        description="Descrição do produto", example="Geladeira econômica"
    )
    total_vl: Decimal = Field(description="Valor total do produto", example="1200.00")
    installments: Optional[dict] = Field(
        description="Parcelas e juros do produto",
        example="{'1': 2, '2': 3}",
    )
    images: Optional[dict] = Field(
        description="Imagens do produto",
        example="{'banner': " "}",
    )
