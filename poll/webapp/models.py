from django.db import models

# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=200, null=False, blank=False, verbose_name="Вопрос")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.id}.{self.question}: {self.created_at}"

    class Meta:
        db_table = "polls"
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"

