from django.urls import path
from .views import ProductViewSet, main, apiOverview, taskList, taskDetail, taskCreate, taskUpdate, taskDelete, RoomView, CreateRoomView, GetRoom, JoinRoom, UserInRoom, LeaveRoom, UpdateRoom

urlpatterns = [
    path('anotherhi/', main),
    path('products', ProductViewSet.as_view({
         'get': 'list',
         'post': 'create'
         })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('task-overview', apiOverview, name="api-overview"),
    path('task-list', taskList, name="task-list"),
    path('task-detail/<str:pk>/', taskDetail, name="task-detail"),
    path('task-create', taskCreate, name="task-create"),
    path('task-update/<str:pk>/', taskUpdate, name="task-update"),
    path('task-delete/<str:pk>/', taskDelete, name="task-delete"),
    path('room', RoomView.as_view()),
    path('create-room', CreateRoomView.as_view()),
    path('get-room', GetRoom.as_view()),
    path('join-room', JoinRoom.as_view()),
    path('user-in-room', UserInRoom.as_view()),
    path('leave-room', LeaveRoom.as_view()),
    path('update-room', UpdateRoom.as_view())
]
