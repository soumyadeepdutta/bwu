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


class Response(models.Model):
    age = models.CharField(max_length=20,  verbose_name='Property Age')
    bhk = models.IntegerField()
    typ = models.CharField(max_length=20, blank=True, null=True)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Response Form'
        verbose_name_plural = 'Response Forms'


    def __str__(self):
        return self.country + ' ' + self.area


class User(models.Model):
    name = models.CharField(max_length=120, verbose_name='User name')
    email = models.EmailField(verbose_name='Email')
    contact_no = models.IntegerField(verbose_name='Contact Number')
    address = models.TextField(verbose_name='Address', max_length=255, blank=True, null=True)
    city = models.CharField(verbose_name='City', max_length=100, blank=True, null=True)
    pin_code = models.IntegerField()
    state=models.CharField(max_length=80, blank=True, null=True)
    country = models.CharField(max_length=80, blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    is_agent = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name + ' ' + self.email