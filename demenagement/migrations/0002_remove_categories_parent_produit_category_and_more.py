# Generated by Django 4.1 on 2022-08-24 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demenagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='parent',
        ),
        migrations.AddField(
            model_name='produit',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='demenagement.produit'),
        ),
        migrations.AddField(
            model_name='produit',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='users/%Y/%m/%d/', verbose_name='imagee'),
        ),
    ]
