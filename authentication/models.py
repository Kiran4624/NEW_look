from django.db import models
from master.models import mainModel

# Create your models here.
class registerModel(mainModel):
    c_id = models.CharField(primary_key=True,max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=False, null=False)
    mobile = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255)
    is_activate = models.BooleanField(default=False)
    is_added_address = models.BooleanField(default=False)
    otp = models.CharField(max_length=10, default="111111")
   
   

    def __str__(self):
        return f"{self.c_id} - {self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.c_id:
            self.c_id = self.generate_customer_id()
        return super(registerModel, self).save(*args, **kwargs)
    
    def generate_customer_id(self):
        last_customer =registerModel.objects.order_by('-c_id').first()
        if last_customer:
            last_id = int(last_customer.c_id[3:]) 
            new_id = last_id + 1
        else:
            new_id = 1
        return 'CUM{:04d}'.format(new_id)
    
    
class AddressModel(mainModel):

    c_id = models.ForeignKey(registerModel, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    


