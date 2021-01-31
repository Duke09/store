from django.urls import path

from .views import PizzeriaCreateApiView, PizzeriaDestroyApiView, PizzeriaUpdateApiView, PizzzeriaListApiView, PizzeriaRetrieveApiView

urlpatterns = [
    path('', PizzzeriaListApiView.as_view(), name='pizzeria_list'),
    path('<int:id>/', PizzeriaRetrieveApiView.as_view(), name='pizzeria_detail'),
    path('create/', PizzeriaCreateApiView.as_view(), name='pizzeria_create'),
    path('update/<int:id>/', PizzeriaUpdateApiView.as_view(), name='pizzeria_update'),
    path('delete/<int:id>/', PizzeriaDestroyApiView.as_view(), name='pizzeria_delete')
]