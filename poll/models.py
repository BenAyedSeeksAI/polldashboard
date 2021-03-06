from django.db import models

class poll(models.Model):
    question = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question

class choice(models.Model):
    poll = models.ForeignKey(poll, on_delete=models.CASCADE)
    choice = models.CharField(max_length=250)
    votes = models.IntegerField()

