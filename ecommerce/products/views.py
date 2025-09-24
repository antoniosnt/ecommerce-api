import traceback
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.decorators import action
from ecommerce.products.repository import ProductRepository
from ecommerce.products.validators import ProductDTO


class ProductViewSet(viewsets.ModelViewSet):
    def list(self, request):
        product_rep = ProductRepository()
        products = product_rep.get_products()

        if not products:
            raise NotFound("products not found")

        return Response(data={"products": products}, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            product_rep = ProductRepository()

            data = {**request.data}

            product_dto = ProductDTO(**data)

            product_rep.insert_product(data=product_dto.model_dump())

            return Response(
                data={"message": "product created"}, status=status.HTTP_201_CREATED
            )

        except Exception as e:
            print(traceback.print_exc())
            return Response(
                data={"message": "internal server error ocurred"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @action(url_path="detail", methods=["GET"], detail=False)
    def get_by_sku(self, request):
        product_rep = ProductRepository()

        nce = request.query_params.get("nce", None)
        fk_color = request.query_params.get("fk_color", None)

        if not nce or not fk_color:
            return Response({"error": "params are required"}, status=400)

        sku = f"{nce.zfill(3)}{fk_color.zfill(3)}"

        product = product_rep.get_product_by_sku(sku=sku)

        if not product:
            raise NotFound("product not found")

        return Response(data={"product": product}, status=status.HTTP_200_OK)
