from django.db import models
from accounts.models import User

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_time =  models.DateField()
    isbn = models.CharField(max_length=13)
    genre = models.ManyToManyField(Genre)
    image = models.ImageField(upload_to='book_image/')

    def __str__(self):
        return self.title

    @property
    def rating(self):
        ratings = [x.rating for x in self.reviews.all()]
        if len(ratings) != 0:
            return round(sum(ratings) / len(ratings), 1)
        else:
            return 0

    @property
    def range(self):
        return range(int(self.rating))

    @property
    def xrange(self):
        return range(5 - int(self.rating))


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    text = models.TextField()


    def __str__(self):
        return f"{self.user.username}'s review for {self.book.title}"