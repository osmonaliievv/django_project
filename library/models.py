from django.db import models


class Books(models.Model):
    GENRE_CHOICES = (
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
        ('Фантастика', 'Фантастика'),
    )
    image = models.ImageField(upload_to='book/', verbose_name='загрузите фото', null=True)
    title = models.CharField(max_length=100, verbose_name='напишите название фильма')
    description = models.TextField(verbose_name='Укажите описание', blank=True)
    price = models.PositiveIntegerField(verbose_name='укажите цену', default=400)
    created_at = models.DateTimeField(auto_now_add=True)
    genre_choices = models.CharField(max_length=100, choices=GENRE_CHOICES,
                                     verbose_name='выберите жанр')
    email = models.CharField(max_length=120,
                             verbose_name='Укажите почту')
    director = models.CharField(max_length=100, verbose_name='Укажите автора',
                                default='Иван Иванов')
    trailer = models.URLField(verbose_name='укажите ссылку с YOUTUBE')

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'Список книг'

    def __str__(self):
        return f'{self.title} - {self.price} сом'


class Reviews(models.Model):
    STARTS = (
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
    )
    review_choice = models.ForeignKey(Books,
                                      on_delete=models.CASCADE,
                                      related_name='books')
    created_at = models.DateField(auto_now_add=True)
    comment = models.TextField(verbose_name='Оставьте комментарий')
    stars = models.CharField(max_length=10, choices=STARTS, default='⭐⭐⭐⭐⭐')

    def __str__(self):
        return f'{self.comment} - {self.stars}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Список комментариев'
