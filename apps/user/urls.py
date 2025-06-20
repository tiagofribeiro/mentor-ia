from django.urls import path
from .api.user import UserView
from .api.superuser import SuperUserView

urlpatterns = [
    path('', UserView.as_view(), name='user-register'),
    path('super/', SuperUserView.as_view(), name='superuser-register'),
]