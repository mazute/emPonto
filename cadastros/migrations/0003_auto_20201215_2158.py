# Generated by Django 2.2.12 on 2020-12-16 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_auto_20201215_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='cnpj',
            field=models.CharField(max_length=18, unique=True),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cpf',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Empresa'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='ponto',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Funcionario', verbose_name='Funcionário'),
        ),
    ]