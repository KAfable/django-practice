from django.db import models


class Question(models.Model):
    # automatically creates an ID and auto increments
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # foreign key to question table, and cascades on deletion
    questions = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
