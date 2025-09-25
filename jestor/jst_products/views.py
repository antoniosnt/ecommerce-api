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
        description="Retorna todos os produtos cadastrados no catálogo.",
        responses={200: ResponseDTO[ProductDTO], 404: HttpErrorDTO},
    )
    def list(self, request):
        product_rep = ProductRepository()
        products = product_rep.get_products()

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

    @extend_schema(
        summary="Listagem de produto por sku",
        description="Retorna produtos que possuem um nce parece ou produto por sku.",
        responses={200: ResponseDTO[ProductDTO], 500: HttpErrorDTO},
    )
    @action(url_path="detail", methods=["GET"], detail=False)
    def get_by_sku(self, request):
        product_rep = ProductRepository()

        nce = request.query_params.get("nce", None)
        fk_color = request.query_params.get("fk_color", None)
        fk_marca = request.query_params.get("fk_marca", None)

        if not nce:
            return Response(
                {"message": "nce are required", "data": None},
                status=status.HTTP_400_BAD_REQUEST,
            )

        sku = f"{nce.zfill(3)}{fk_color.zfill(3)}{fk_marca.zfill(3)}"

        products = product_rep.get_product_by_sku(sku=sku)

        if not products:
            return Response(
                data={"message": "product not found", "data": None},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            data={"message": "success", "data": products}, status=status.HTTP_200_OK
        )
