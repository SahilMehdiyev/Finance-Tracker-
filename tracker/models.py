from django.db import models
from django.contrib.auth.models import AbstractUser
# from tracker.utils.choices import TRANSACTION_TYPE_CHOICES

class User(AbstractUser):
    pass



class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name
    
 
class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=7, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.user.username} - {self.type} - {self.amount}"
    