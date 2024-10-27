from django.urls import path, include
from my_app.views import  SubTaskListCreateView, SubTaskDetailUpdateDeleteView, TaskListCreateView
from rest_framework.routers import DefaultRouter
from my_app.views import CategoryViewSet
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)



router = DefaultRouter()
router.register(r'categories', CategoryViewSet)


urlpatterns =[
    path('tasks/', TaskListCreateView.as_view(), name='task_list_create'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask_list_create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask_detail'),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

