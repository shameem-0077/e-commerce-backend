from django.urls import path
from api.v1.products import views


app_name = "api_v1_products"

urlpatterns = [
    # chief_side
    path('create-product/', views.create_product),
    path('edit-product/<int:pk>/', views.edit_product),

    path('create/category/', views.create_category),
    path('edit-category/<int:pk>/', views.edit_category),

    path('create-featured/', views.create_featured),
    path('edit-featured/<int:pk>/', views.edit_featured),

    path('add-product-image/<int:product_id>/', views.add_product_image),
    path('edit-product-image/<int:product_id>/<int:pk>/', views.edit_product_image),

    path('add-product-size/<int:product_id>/', views.add_product_size),
    path('edit-product-size/<int:product_id>/<int:pk>/', views.edit_product_size),

    # client_side







    path('categories/', views.fetch_categories),

]