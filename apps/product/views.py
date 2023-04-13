from .models import Product
from .serializers import ProductSerializer
from rest_framework import permissions , viewsets
from .permissions import IsOwner

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        method = self.get.method
        if method in permissions.SAFE_METHODS:
            self.permissions_classes = [permissions.AllowAny]
        elif method == "POST":
            self.permissions_classes = [permissions.IsAuthenticated]
        elif method in ['DELETE', 'PUT', 'PATCH']:
            self.permissions_classes = [IsOwner]
        return super().get_permissions()