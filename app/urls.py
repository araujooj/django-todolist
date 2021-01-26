from django.urls import path

from app.views import todo_list
from app.views import todo_detail_change_and_delete

urlpatterns = [
    path('', todo_list),
    path('<int:pk>/', todo_detail_change_and_delete)
]