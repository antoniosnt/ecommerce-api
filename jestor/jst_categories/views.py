import traceback
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from jestor.core.utils.dto import ResponseDTO, HttpErrorDTO
from jestor.jst_categories.repository import CategoryRepository

# from jestor.jst_categories.validators import CategoryDTO


class CategoryViewSet(viewsets.ModelViewSet):

    @extend_schema(
        summary="Listagem de categorias",
        description="Retorna todas as categorias cadastradas no catálogo podendo-se passar filtros.",
        responses={200: ResponseDTO[None], 404: HttpErrorDTO},
    )
    def list(self, request):
        try:

            category_rep = CategoryRepository()

            na_category = request.query_params.get("na_category", None)
            cd_category = request.query_params.get("cd_category", None)

            categories = category_rep.get_categories(
                na_category=na_category, cd_category=cd_category
            )

            if not categories:
                return Response(
                    data={"message": "categories not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            return Response(data={"categories": categories}, status=status.HTTP_200_OK)
        except Exception:
            print(traceback.print_exc())
            return Response(
                data={"message": "internal server error ocurred"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @extend_schema(
        summary="Criação de categorias",
        description="Cria novas categorias para o catálogo.",
        responses={200: ResponseDTO[None], 404: HttpErrorDTO},
    )
    def create(self, request):
        try:
            category_rep = CategoryRepository()

            data = {**request.data}

            category_rep.insert_category(data=data)

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
