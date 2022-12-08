from django.urls import path
from bookApi.views import BookList, BookCreate, BookDetail

urlpatterns = [
    path('', BookCreate.as_view()),
    path('list/', BookList.as_view()),
    path('<int:id>', BookDetail.as_view())
]
