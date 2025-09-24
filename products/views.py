from rest_framework import viewsets, status
from rest_framework.response import Response
from products.repository import ProductRepository

class ProductViewSet(viewsets.ModelViewSet):
    def list(self, request):
        try:
            return Response(data={"message": "ok"})
        except Exception as e:
            return Response(data={"message": "internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)