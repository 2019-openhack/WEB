from django.db import models

# Create your models here.

class word(models.Model):
    word = models.CharField(max_length=100)
    mean = models.CharField(max_length=100)
    sentence = models.CharField(max_length=1000) # 예문
    pron = models.CharField(max_length=100) # 발음 들어간 path -> tts 구현해야함.
 

class Dic(models.Model):
    word = models.ForeignKey(word,on_delete=models.CASCADE) # 일대다관계로 지정
    remind = models.PositiveIntegerField(default=4) # 한번 공부할 때 마다 빼줘야함.
    name = models.CharField(max_length=200,default='') # 단어장 이름 설정 


class User(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField(max_length=70, default="ajs7270@naver.com")
    dic = models.ManyToManyField(Dic)
    half_memory_word = models.PositiveIntegerField(default=4) #내가 지금까지 몇개 단어 외웠나.
    full_memory_word = models.PositiveIntegerField(default=4) #내가 완전히 외운 단어.

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.user_name
 
