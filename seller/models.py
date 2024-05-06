from django.db import models
from django.forms import ValidationError

from master.models import mainModel
from master.utils.n_UNIQUE.unique_filename import genrate_unique_filename


# Create your models here.
class categoryModel(mainModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class productModel(mainModel):
    DIR_NAME = 'product_images/'
    SUFFIX_WORD = 'pi'
    PREFIX_TABLE_ID_WORD = 'NLO'
    product_id = models.CharField(primary_key=True, max_length=255, blank=True)
    image = models.ImageField(upload_to=genrate_unique_filename)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category_id = models.ForeignKey(categoryModel, on_delete=models.CASCADE)
    mrp_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True)

    def clean(self):
        if self.mrp_price < self.selling_price:
            raise ValidationError("Selling price cannot be greater than MRP price")

  

    def __str__(self):
        return f"{self.category_id.name} - {self.pro_id}"