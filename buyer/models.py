from django.db import models
from master.models import mainModel
from authentication.models import registerModel
from seller.models import productModel

class cartModel(mainModel):
    c_id = models.ForeignKey(registerModel, on_delete=models.CASCADE)
    pro_id = models.ForeignKey(productModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class ContactModel(mainModel):

    STATUS_CHOICES = (
        ('resolved', 'Resolved'),
        ('unresolved', 'Unresolved'),
        ('on_working', 'On Working')
    )


    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, default='unresolved', max_length=255)