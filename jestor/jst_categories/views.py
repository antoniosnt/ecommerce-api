import traceback
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.decorators import action
from jestor.jst_categories.repository import CategoryRepository


class CategoryViewSet(viewsets.ModelViewSet):
    def list(self, request):
        category_rep = CategoryRepository()
        categories = category_rep.get_categories()

        if not categories:
            raise NotFound("categories not found")

        return Response(data={"categories": categories}, status=status.HTTP_200_OK)

    def create(self, request):
        pass

    @action(url_path="detail", methods=["GET"], detail=False)
    def get_by_cd_category(self, request):
        pass