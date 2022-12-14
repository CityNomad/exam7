from django.db import models
from django.urls import reverse
# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=200, null=False, blank=False, verbose_name="Вопрос")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.id}.{self.question}: {self.created_at}"

    def get_absolute_url(self):
        return reverse("poll_view", kwargs={"pk": self.pk})

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
        verbose_name = "Вариант"
        verbose_name_plural = "Варианты"

class Answer(models.Model):
    poll = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE, related_name = 'answers', verbose_name="Опрос")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    choice = models.ForeignKey('webapp.Choice', on_delete=models.CASCADE, related_name = 'answers', verbose_name="Вариант")

    def __str__(self):
        return f"{self.id}.{self.poll}:{self.choice}"

    class Meta:
        db_table = "answers"
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"