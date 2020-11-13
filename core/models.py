from django.db import models


class FindHome(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.TextField(max_length=255)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=15)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Finding Home'

    def __str__(self):
        return self.name + ' ' + self.country + ' ' + self.email


class SellHome(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    location = models.TextField(max_length=255)
    age = models.FloatField()
    type = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Selling Home'

    def __str__(self):
        return self.name + ' ' + self.type + ' ' + self.email


class GeneralEnquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address = models.TextField(max_length=255)
    query = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = 'General Queries'

    def __str__(self):
        return self.name + ' ' + str(self.query)[:10]


class FindAgent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    location = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = 'Finding Agents'

    def __str__(self):
        return self.name + ' ' + self.email


class BecomeAnAgent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    location = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = 'Become Agents'

    def __str__(self):
        return self.name + ' ' + self.email
