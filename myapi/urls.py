from django.urls import path
from .import views

urlpatterns=[
    path('',views.apioverview,name='api-overview'),
    path('task-list/',views.taskList,name="api-overview"),
    path('detail-list/<str:pk>',views.details,name="api-details"),
    path('task-create/',views.taskCreate,name="task-create"),
    path('task-update/<str:pk>/',views.taskUpdate,name="task-update"),
    path('task-delete/<str:pk>/',views.taskDelete,name="task-delet")
]