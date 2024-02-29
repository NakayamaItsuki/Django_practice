from django.db import models


class Memo(models.Model):
    # メモのモデル
    title = models.CharField('タイトル', max_length=100)
    text = models.TextField('本文')

    def __str__(self):
        return self.title