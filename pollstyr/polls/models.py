from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Create your models here.





class Question(models.Model):
    
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    voter1 = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    



    # def user_can_vote(self,user):
    #     # return self.question_text
    #     user_votes=user.vote_set.all()
    #     qs=user_votes.filter(Question=self)
    #     if qs.exists():
    #         return False
    #     return True

    # def get_vote_count(self):
    #     return self.get_vote_count()

    # def get_result_dict(self):
    #     res=[]
    #     for choice in self.choice_set.all():
    #         d={}
    #         alert_class=
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Vote(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    vote=models.ForeignKey(User, on_delete=models.CASCADE)
    