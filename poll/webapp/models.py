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

class Choice(models.Model):
    text = models.CharField(max_length=1000, null=False, blank=False, verbose_name="Ответ")
    poll = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE, related_name = 'choices', verbose_name="Опрос")

    def __str__(self):
        return f"{self.id}.{self.text}"

    class Meta:
        db_table = "choices"
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"