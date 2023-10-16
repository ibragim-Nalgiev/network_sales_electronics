from django.views.generic import ListView
from rest_framework.permissions import IsAdminUser

from users.permissions import IsUserActive
from .models import Product
from .paginations import ProductPagination
from .serializers import ProductSmallSerializer


class ProductListView(ListView):
    model = Product
    serializer_class = ProductSmallSerializer
    permission_classes = [IsUserActive, IsAdminUser]
    pagination_class = ProductPagination
