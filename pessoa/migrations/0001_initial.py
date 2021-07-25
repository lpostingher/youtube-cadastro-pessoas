# Generated by Django 3.2.5 on 2021-07-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=256)),
                ('data_nascimento', models.DateField(null=True)),
                ('ativa', models.BooleanField(default=True)),
            ],
        ),
    ]
