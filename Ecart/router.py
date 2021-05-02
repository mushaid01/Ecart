from user.viewsets import EmployeeViewset
from rest_framework import routers
router=routers.DefaultRouter()
router.register('pizza',EmployeeViewset)
