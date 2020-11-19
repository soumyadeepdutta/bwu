from django.db import models

# user, property, forms, likes
class DummyProperty(models.Model):
    country = models.CharField(max_length=5, help_text='Country code')
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text='Price in doller')
    image = models.CharField(max_length=255, default='https://images.unsplash.com/photo-1579700432983-39c5fb5815e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1486&q=80')

    class Meta:
        verbose_name_plural = 'Dummy Properties'

    def __str__(self):
        return self.country + ' ' + str(self.price)