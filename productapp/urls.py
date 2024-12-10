from django.urls import path
from .import views

urlpatterns = [
    path('',views.productform,name='productform'),
    path('productregister',views.productregister,name='productregister'),
    path('productdetails',views.productdetails,name='productdetails'),
    path('editdetails/<int:id>',views.editdetails,name='editdetails'),
    path('editpage/<int:id>',views.editpage,name='editpage'),
    path('delete/<int:id>',views.delete,name='delete'),
]