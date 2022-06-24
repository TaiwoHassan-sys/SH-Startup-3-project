from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("users", views.UserModelViewSet, basename="users")
router.register("api", views.EmployeeModelViewSet, basename="api")
router.register("vac", views.VacationModelViewSet, basename="vac")


urlpatterns = [
    path('', views.employee_form,name='employee_insert'), # get and post req. for insert operation
    path('<int:id>/', views.employee_form,name='employee_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
    path('list/',views.employee_list,name='employee_list') # get req. to retrieve and display all records
]

urlpatterns += router.urls