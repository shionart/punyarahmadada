# Generated by Django 3.1.7 on 2021-04-11 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indonesia', '0002_auto_20210411_2312'),
    ]

    operations = [
        migrations.DeleteModel(
            name='batubara2',
        ),
        migrations.RemoveField(
            model_name='batubara1',
            name='Potensislagging',
        ),
        migrations.AddField(
            model_name='batubara1',
            name='PotensiSlagging',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='batubara1',
            name='KadarAbu',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='batubara1',
            name='NilaiKalor',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='batubara1',
            name='Pemasok',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='batubara1',
            name='TotalMoisture',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='batubara1',
            name='TotalSulfur',
            field=models.CharField(max_length=200),
        ),
    ]
