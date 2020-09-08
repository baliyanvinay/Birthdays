from django.db import models

# Create your models here.
class Tab_Birthdays(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    dob=models.DateField()
    age=models.IntegerField()

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    class Meta:
        verbose_name_plural = "Tab_Birthdays"