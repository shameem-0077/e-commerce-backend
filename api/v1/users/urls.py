from django.urls import path, include
from api.v1.users import views


app_name = "api_v1_users"

urlpatterns = [
    path('user/signup/', views.sign_up),

]