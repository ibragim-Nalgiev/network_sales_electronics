from django.urls import path

from networks_electronics.apps import RetailNetworkConfig
from networks_electronics.views.retail_network_views import RetailNetListAPIView, RetailNetCreateAPIView, RetailNetUpdateAPIView, \
    RetailNetRetrieveAPIView, RetailNetDeleteAPIView
from networks_electronics.views.main_network_views import MainNetListView, MainNetCreateAPIView, MainNetUpdateAPIView, \
    MainNetRetrieveAPIView, MainNetDeleteAPIView

app_name = RetailNetworkConfig.name

urlpatterns = [
    # main_networks
    path("main-networks/", MainNetListView.as_view(), name='list_main_networks'),
    path("main-networks/create/", MainNetCreateAPIView.as_view(), name='create_main_networks'),
    path("main-networks/update/<int:pk>/", MainNetUpdateAPIView.as_view(), name='update_main_networks'),
    path("main-networks/get/<int:pk>/", MainNetRetrieveAPIView.as_view(), name='get_main_networks'),
    path("main-networks/delete/<int:pk>/", MainNetDeleteAPIView.as_view(), name='delete_main_networks'),


    # retail-networks
    path("retail-networks/", RetailNetListAPIView.as_view(), name='list_retail_networks'),
    path("retail-networks/create/", RetailNetCreateAPIView.as_view(),
         name='create_retail_network'),
    path("retail-networks/update/<int:pk>/", RetailNetUpdateAPIView.as_view(), name='update_retail_network'),
    path("retail-networks/get/<int:pk>/", RetailNetRetrieveAPIView.as_view(),
         name='get_retail_network'),
    path("retail-networks/delete/<int:pk>/", RetailNetDeleteAPIView.as_view(), name='delete_retail_network'),
]
