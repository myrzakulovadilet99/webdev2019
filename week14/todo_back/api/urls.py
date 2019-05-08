from django.urls import path, re_path
from api import views

# urlpatterns = [
#     path('task_lists/', views.task_list),
#     path('task_lists/<int:pk>/', views.task_lists_num),
#     path('task_lists/<int:pk>/tasks', views.task_lists_num_tasks)
# ]

urlpatterns = [
    path('task_lists/', views.TaskListt.as_view()),
    path('task_lists/<int:pk>/', views.TaskListNum.as_view()),
    path('task_lists/<int:pk>/tasks', views.TaskListNumTasks.as_view()),
    path('users/', views.UserList.as_view()),
    # path('task_lists/<int:pk>/tasks', views.task_lists_num_tasks),
    path('login/', views.login),
    path('logout/', views.logout),
]