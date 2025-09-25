import traceback
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from jestor.core.utils.dto import ResponseDTO, HttpErrorDTO
from jestor.jst_products.repository import ProductRepository
from jestor.jst_products.validators import ProductDTO


class ProductViewSet(viewsets.ModelViewSet):
    """
    API de gerenciamento de produtos do catálogo.
    """

    @extend_schema(
        summary="Listagem de produtos",
        description="Retorna todos os produtos cadastrados no catálogo podendo-se passar filtros.",
        responses={200: ResponseDTO[ProductDTO], 404: HttpErrorDTO},
    )
    def list(self, request):
        sku = request.query_params.get("sku", None)
        na_product = request.query_params.get("na_product", None)

        product_rep = ProductRepository()
        products = product_rep.get_products(sku=sku, na_product=na_product)

        if not products:
            return Response(
                data={"message": "products not found", "data": None},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(data={"data": products}, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Criação de produto",
        description="Cria um novo produto no catálogo.",
        responses={200: ResponseDTO[None], 500: HttpErrorDTO},
    )
    def create(self, request):
        try:
            product_rep = ProductRepository()

            data = {**request.data}

            product_dto = ProductDTO(**data)

            product_rep.insert_product(data=product_dto.model_dump())

            return Response(
                data={"message": "success", "data": None},
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            print(traceback.print_exc())
            return Response(
                data={"message": "internal server error ocurred"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @extend_schema(exclude=True)
    def update(self, request, pk=None):
        pass

    @extend_schema(exclude=True)
    def partial_update(self, request, pk=None):
        pass

    @extend_schema(exclude=True)
    def retrieve(self, request, pk=None):
        pass

    @extend_schema(exclude=True)
    def destroy(self, request, pk=None):
        pass
