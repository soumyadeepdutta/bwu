from django.db import models

# user, property, forms, likes
class DummyProperty(models.Model):
    country = models.CharField(max_length=5, help_text='Country code')
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text='Price in doller')
    image = models.ImageField(upload_to='images')

    class Meta:
        verbose_name_plural = 'Dummy Properties'

    def __str__(self):
        return self.country + ' ' + str(self.price)