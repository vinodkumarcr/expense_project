from django.db import models

class Catagorie(models.Model):
    Name=models.CharField(max_length=100)


    def __str__(self):
        return self.Name


class Expense(models.Model):
    Catagory=models.ForeignKey(Catagorie,on_delete=models.CASCADE)
    Date=models.DateField(auto_now_add=False)
    Money=models.DecimalField(max_digits=8,decimal_places=2)
    Amount=models.DecimalField(max_digits=8,decimal_places=2,default=0)
    Place=models.CharField(max_length=100)


    def __str__(self):
        return self.Place

    def yes(self):
        return self.Date.strftime('%b %e %Y')

class Total(models.Model):
    Total_money=models.DecimalField(max_digits=8,decimal_places=2)
    My_share=models.DecimalField(max_digits=8,decimal_places=2)
    Friends_share=models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return str(self.Total_money)

class Totals(models.Model):
    Final_amount=models.DecimalField(max_digits=8,decimal_places=2)

    def __str__(self):
        return str(self.Final_amount)


class Share(models.Model):
    Catagory=models.ForeignKey(Catagorie,on_delete=models.CASCADE)
    Date=models.DateField(auto_now_add=False)
    Money=models.DecimalField(max_digits=8,decimal_places=2)
    Count=models.IntegerField()
    Place=models.CharField(max_length=20)


    def __str__(self):
        return self.Place
