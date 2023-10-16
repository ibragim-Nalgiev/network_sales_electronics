from .main_network_views import MainNetCreateAPIView, MainNetListView, MainNetUpdateAPIView, MainNetRetrieveAPIView, \
    MainNetDeleteAPIView
from .retail_network_views import RetailNetCreateAPIView, RetailNetListAPIView, RetailNetRetrieveAPIView, \
    RetailNetDeleteAPIView, RetailNetUpdateAPIView


__all__ = [
    'MainNetCreateAPIView', 'MainNetListView', 'MainNetUpdateAPIView', 'MainNetRetrieveAPIView', 'MainNetDeleteAPIView',
    'RetailNetCreateAPIView', 'RetailNetListAPIView', 'RetailNetRetrieveAPIView', 'RetailNetDeleteAPIView',
    'RetailNetUpdateAPIView']
