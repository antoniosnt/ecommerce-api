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
        description="Retorna todas as categorias cadastradas no catálogo.",
        responses={200: ResponseDTO[None], 404: HttpErrorDTO},
    )
    def list(self, request):
        category_rep = CategoryRepository()
        categories = category_rep.get_categories()

        if not categories:
            raise NotFound("categories not found")

        return Response(data={"categories": categories}, status=status.HTTP_200_OK)

    @extend_schema(exclude=True)
    def create(self, request):
        pass

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

    @extend_schema(exclude=True)
    @action(url_path="detail", methods=["GET"], detail=False)
    def get_by_cd_category(self, request):
        pass
