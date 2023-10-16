from django.urls import path

from sole_proprietor.apps import SoleProprietorConfig
from sole_proprietor.views import SoleProprietorListView, SoleProprietorCreateView, SoleProprietorUpdateView, \
    SoleProprietorRetrieveView, SoleProprietorDeleteView

app_name = SoleProprietorConfig.name

urlpatterns = [
    path("sole-proprietors/", SoleProprietorListView.as_view(), name='list_sole_proprietor'),
    path("sole-proprietors/create/", SoleProprietorCreateView.as_view(), name='create_sole_proprietor'),
    path("sole-proprietors/update/<int:pk>/", SoleProprietorUpdateView.as_view(), name='update_sole_proprietor'),
    path("sole-proprietors/get/<int:pk>/", SoleProprietorRetrieveView.as_view(), name='get_sole_proprietor'),
    path("sole-proprietors/delete/<int:pk>/", SoleProprietorDeleteView.as_view(), name='delete_sole_proprietor'),
]
