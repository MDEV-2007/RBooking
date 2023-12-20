from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.http import HttpResponse

from .models import Author,Book,Review,Genre


class BookListView(View):
    template_name = 'home.html'

    def get(self, request):
        books = sorted([x for x in Book.objects.all() if x.get_rating() >= 3.5], key=lambda x: x.rating, reverse=True)
        return render(request, self.template_name, {'books': books})


class BookDetailView(View):
    template_name = 'books/detail.html'
    def get(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        reviews = Review.objects.filter(book=book)
        genre = Genre.objects.filter(book=book)
        return render(request, self.template_name, {'book': book, 'reviews': reviews,'genre':genre})


    def post(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        text = request.POST.get('text')
        rating = request.POST.get('rating')
        
        if text and rating:
            Review.objects.create(book=book, user=request.user, text=text, rating=rating)
        else:
            return HttpResponseForbidden("Invalid form submission")

        return redirect('book_detail', book_id=book_id)


class AuthorDetailView(View):
    template_name = 'books/author_page.html'
    def get(self, request, author_id):
        author = get_object_or_404(Author, pk=author_id)
        books = Book.objects.filter(author=author)
        return render(request, self.template_name, {'author': author, 'books': books})
    



def category(request):
    genre = request.GET.get('genre')
    queryset = Book.objects.all()
    genres = Genre.objects.all()
    
    if genre:
        queryset = queryset.filter(genre=Genre.objects.get(name=genre))
   
    # queryset = [x for x in queryset if x.rating >= 3.7] 
    
    books = sorted(queryset, key=lambda x: x.rating, reverse=True)
    
    
    return render(request, 'books/category.html', {'books': books,'genre':genres})
