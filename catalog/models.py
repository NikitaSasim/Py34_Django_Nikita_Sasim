from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="authors/", blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.TextField()
    summary = models.TextField()
    publication_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, default=1.00, decimal_places=2)
    amount = models.IntegerField(null=False)
    genre = models.ManyToManyField(Genre)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_genre(self):
        return ", ".join([genre.name for genre in self.genre.all()])


    def get_date(self):
        return self.publication_date.strftime("%Y")
    get_genre.short_description = "Genre"


