from django.urls import path
from api import views

# urlpatterns = [
#     path('task_lists/', views.task_list),
#     path('task_lists/<int:num>/', views.task_lists_num),
#     path('task_lists/<int:num>/tasks', views.task_lists_num_tasks)
# ]

urlpatterns = [
    path('task_lists/', views.task_list.as_view()),
    path('task_lists/<int:pk>/', views.task_lists_num.as_view()),
    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    # path('task_lists/<int:num>/tasks/', views.task_lists_num_tasks),
]