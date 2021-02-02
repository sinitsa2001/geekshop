from django.urls import path

import adminapp.views as adminapp


app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('users/', adminapp.UserListView.as_view(), name='admin_users'),
    # path('users/', adminapp.admin_users, name='admin_users'),
    # path('users/create/', adminapp.admin_users_create, name='admin_users_create'),
    path('users/create/', adminapp.UserCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>/', adminapp.UserUpdateView.as_view(), name='admin_users_update'),
    path('users/remove/<int:pk>/', adminapp.UserDeleteView.as_view(), name='admin_users_remove'),
    # path('categories/', adminapp.categories, name='categories'),
    # path('logout/', adminapp.logout, name='logout'),
    path('categories/create', adminapp.category_create, name='admin_category_create'),
    path('categories/read', adminapp.categories, name ='admin_categories'),
    path('categories/update/<int:pk>', adminapp.category_update, name ='admin_category_update_delete'),
    path('categories/delete/<int:pk>', adminapp.category_delete, name = 'admin_category_delete'),

    path('products/create/category/<int:pk>', adminapp.product_create, name = 'admin_product_create'),
    path('products/read/category/<int:pk>', adminapp.products, name = 'admin_product_create'),
    path('products/read/<int:pk>', adminapp.product_read, name = 'admin_product_read'),
    path('products/update/<int:pk>', adminapp.product_update, name = 'admin_product_update'),
    path('products/delete/<int:pk>', adminapp.product_delete, name = 'admin_product_delete'),



]