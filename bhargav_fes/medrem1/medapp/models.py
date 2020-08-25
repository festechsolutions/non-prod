from django.db import models
from django.contrib.auth.models import User


class Meddata(models.Model):
    
    Med_Name=models.CharField(max_length=200)
    Med_Dur=models.CharField(max_length=200)
    Mrg_med=models.TimeField(auto_now_add=False, auto_now=False)
    noon_med=models.TimeField(auto_now_add=False, auto_now=False)
    evng_med=models.TimeField(auto_now_add=False, auto_now=False,)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def timereturn(self):
    	
    	return self.evng_med.strftime("%H:%m %p ")
    
