from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('published time')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Foreign Key
    choice_text = models.CharField(max_length=200) # 답변 항목 문구
    votes = models.IntegerField(default=0) # 투표 카운트

    def __str__(self):
        return self.choice_text