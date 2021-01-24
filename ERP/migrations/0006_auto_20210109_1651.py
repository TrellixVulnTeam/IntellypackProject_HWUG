# Generated by Django 3.1.4 on 2021-01-09 15:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ERP', '0005_auto_20210108_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dossier',
            name='client',
        ),
        migrations.RemoveField(
            model_name='dossier',
            name='collaborateur',
        ),
        migrations.AddField(
            model_name='dossier',
            name='client_BIC',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='dossier',
            name='client_IBAN',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dossier',
            name='client_RCS',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='dossier',
            name='client_adresse',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='dossier',
            name='client_code_postal',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='dossier',
            name='client_lieu_d_installation',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='dossier',
            name='client_raison_sociale',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dossier',
            name='client_siren',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='dossier',
            name='client_telephone_fixe',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='dossier',
            name='client_telephone_portable',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='dossier',
            name='client_ville',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='dossier',
            name='collaborateur_nom',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='dossier',
            name='collaborateur_numero',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='dossier',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Collaborateur',
        ),
    ]
