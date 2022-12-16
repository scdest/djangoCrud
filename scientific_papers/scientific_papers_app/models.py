from django.db import models

class Paper(models.Model):
    title = models.CharField('Назва', max_length=50)
    author = models.CharField('Автор', max_length=50)
    text = models.TextField('Опис')
    published = models.CharField('Рік видання', max_length=4, default='2022')
    citations_count = models.IntegerField('Кількість цитувань', default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'
