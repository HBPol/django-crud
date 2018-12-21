from django.urls import path
from crudapp import views

from django.urls import include

urlpatterns = [
    
    path('', views.index, name='index'),
    
    path('create/', views.create, name='create'),
    
    path('edit/<int:id>', views.edit, name='edit'),
    
    path('edit/update/<int:id>', views.update, name='update'),
    
    path('delete/<int:id>', views.delete, name='delete'),
    
    path('testform-01/', views.test_model_form_01, name='testform-01'),
    
    path('testform-02/', views.test_model_form_02, name='testform-02'),
    
]
