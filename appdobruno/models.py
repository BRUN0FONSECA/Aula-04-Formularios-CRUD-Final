from django.db import models

class Surfistas(models.Model):
  title = models.CharField(max_length=70)
  nacionality=models.CharField(max_length=20)
  WorldTitles=models.IntegerField()
  stance= models.CharField(max_length=20)



class Places(models.Model):
  title=models.CharField(max_length=50)
  country=models.CharField(max_length=50)
  InitialDate=models.DateField()
  FinalDate=models.DateField()

class FSurfistas(models.Model):
  title = models.CharField(max_length=70)
  nacionality=models.CharField(max_length=20)
  WorldTitles=models.IntegerField()
  stance= models.CharField(max_length=20)

  
  
