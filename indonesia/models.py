from django.db import models

# Create your models here.

class batubara1(models.Model):
	Pemasok = models.CharField(max_length=200)
	NilaiKalor = models.IntegerField(null=True)
	TotalMoisture = models.CharField(max_length=200)
	TotalSulfur = models.CharField(max_length=200)
	KadarAbu = models.CharField(max_length=200)
	PotensiSlagging	= models.IntegerField(null=True)

class batubara2(models.Model):
	Pemasok = models.CharField(max_length=200)
	NilaiKalor = models.IntegerField(null=True)
	TotalMoisture = models.CharField(max_length=200)
	TotalSulfur = models.CharField(max_length=200)
	KadarAbu = models.CharField(max_length=200)
	PotensiSlagging	= models.IntegerField(null=True)

class Power(models.Model):
	nama= models.CharField(max_length=9)
	keterangan = models.TextField()

def __str__(self):
	return self.nama