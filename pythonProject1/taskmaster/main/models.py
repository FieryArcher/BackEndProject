from django.db import models
from django.urls import reverse


class Task(models.Model):
    title = models.CharField('Name', max_length=20)
    definition = models.TextField('Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Story(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    #
    # def get_absolute_url_up(self):
    #     return reverse('update_post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
