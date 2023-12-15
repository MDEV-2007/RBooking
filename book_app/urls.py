from django.urls import path
from .views import BookListView, BookDetailView, AuthorDetailView,category

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('books/<int:book_id>/', BookDetailView.as_view(), name='book_detail'),
    path('authors/<int:author_id>/', AuthorDetailView.as_view(), name='author_detail'),
    path('book/category',category,name='category'),

]