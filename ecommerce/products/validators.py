from typing import Optional
from decimal import Decimal
from pydantic import BaseModel


class ProductDTO(BaseModel):
    nce: int
    fk_color: int
    na_product: str
    na_description: str
    total_vl: Decimal
    installments: Optional[dict] = None
    images: Optional[dict] = None
