from django.urls import path
from . import views


app_name = 'account'

urlpatterns = [
    path('account/create/', views.UserCreateView.as_view(), name='new_account'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(next_page='/'), name='logout'),
]