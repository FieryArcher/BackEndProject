from django.db import models


# Create your models here.

class Words(models.Model):
    TIMER = [
        ('past', 'PAST'),
        ('present', 'PRESENT'),
        ('future', 'FUTURE'),
    ]

    word = models.CharField(verbose_name="Word", max_length=100)
    timer = models.CharField(verbose_name="Timer", max_length=10, choices=TIMER)

    def __str__(self):
        return self.timer + " " + self.word
