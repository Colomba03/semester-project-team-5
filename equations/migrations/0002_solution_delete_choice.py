# Generated by Django 4.0.3 on 2022-03-21 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equations.question')),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
