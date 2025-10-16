from django.urls import path, include
from .views import Tasklist, TaskDetail,TaskCreate,TaskUpdate, TaskDelete , CustomLoginView ,RegisterPage 
from django.contrib.auth.views import LogoutView
from rest_framework.routers import DefaultRouter
from .api_views import Tasklist, RegisterPage, CustomLoginView

router = DefaultRouter()
router.register(r'api/tasks', Tasklist, basename='task')
urlpatterns = [
    path('login/',CustomLoginView.as_view() ,name='login'),
    path('logout/',LogoutView.as_view(next_page='login') ,name='logout'),
    path('register/',RegisterPage.as_view(),name='register'),
    path('',Tasklist.as_view() ,name='tasks'),
    path('task/<int:pk>',TaskDetail.as_view() ,name='task'),
    path('task-create',TaskCreate.as_view() ,name='task-create'),
    path('task-update/<int:pk>',TaskUpdate.as_view() ,name='task-update'),
    path('task-delete/<int:pk>',TaskDelete.as_view() ,name='task-delete'),

    # API URLs
    path('api/register/', RegisterPage.as_view(), name='api-register'),
    path('api/token/', CustomLoginView.as_view(), name='api-token'),
    path('', include(router.urls)),
]
