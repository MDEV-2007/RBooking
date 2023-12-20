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
    

class Language(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    published_time =  models.DateField()
    isbn = models.CharField(max_length=13)
    genre = models.ManyToManyField(Genre)
    image = models.ImageField(upload_to='book_image/')
    price = models.FloatField(max_length=100)
    # language = models.ForeignKey(Language,on_delete=models.CASCADE, related_name='author')
    format = models.CharField(max_length=150)
    series = models.CharField(max_length=250)
    

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

    def ratings(self):

        def get(rating) -> dict:
            
            filtered = self.reviews.filter(rating=rating)

            return {
                'count': len(filtered),
                'percent': round(len(filtered)  / (len(self.reviews.all()) / 100), 1)
            }

        return {
            '1': get(1),
            '2': get(2),
            '3': get(3),
            '4': get(4),
            '5': get(5)
        }


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    text = models.TextField()


    def __str__(self):
        return f"{self.user.username}'s review for {self.book.title}"