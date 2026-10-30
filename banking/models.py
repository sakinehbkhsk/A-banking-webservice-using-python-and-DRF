from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    


class Account(models.Model):
    class AccountStatus(models.TextChoices):
        OPEN = "open", "Open"
        CLOSED = "closed", "Closed"
        BLOCKED = "blocked", "Blocked"
    account_no = models.CharField(max_length=20,unique=True)
    customer= models.ForeignKey("Customer", on_delete=models.CASCADE, related_name='accounts')
    account_status = models.CharField(max_length=10, choices=AccountStatus.choices, default=AccountStatus.OPEN)
    account_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return self.account_no