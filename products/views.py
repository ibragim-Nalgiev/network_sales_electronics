from django.views.generic import ListView
from rest_framework.permissions import IsAdminUser

from users.permissions import IsClientActive
from .models import Product
from .paginations import ProductPagination
from .serializers import ProductBaseSerializer


class ProductListView(ListView):
    model = Product
    serializer_class = ProductBaseSerializer
    permission_classes = [IsClientActive, IsAdminUser]
    pagination_class = ProductPagination

