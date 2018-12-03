from django.db import models

class Location(models.Model):
    locName = models.CharField(max_length=50)

    def __str__(self):
        return self.locName

class Department(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    deptName = models.CharField(max_length=50)

    def __str__(self):
        return self.deptName

class Category(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    catName = models.CharField(max_length=50)

    def __str__(self):
        return self.catName

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subCatName = models.CharField(max_length=50)

    def __str__(self):
        return self.subCatName
