# Generated by Django 4.2.6 on 2023-11-30 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_application_comments_historicalapplication_comments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authuser',
            options={'managed': False, 'verbose_name': 'Работник', 'verbose_name_plural': 'Работники'},
        ),
        migrations.AlterModelOptions(
            name='labs_cabinets',
            options={'verbose_name': 'Закрепленный за сис. Админом кабинет', 'verbose_name_plural': 'Закрепеленные за сис. Админом кабинеты'},
        ),
        migrations.AlterField(
            model_name='application',
            name='auth_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.authuser', verbose_name='Работник'),
        ),
        migrations.AlterField(
            model_name='application',
            name='worker',
            field=models.ForeignKey(blank=True, limit_choices_to={'groups__name': 'labs'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Сис. Администратор'),
        ),
        migrations.AlterField(
            model_name='historicalapplication',
            name='auth_user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.authuser', verbose_name='Работник'),
        ),
        migrations.AlterField(
            model_name='historicalapplication',
            name='worker',
            field=models.ForeignKey(blank=True, db_constraint=False, limit_choices_to={'groups__name': 'labs'}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Сис. Администратор'),
        ),
        migrations.AlterField(
            model_name='labs_cabinets',
            name='worker',
            field=models.ForeignKey(blank=True, limit_choices_to={'groups__name': 'labs'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Сис. Администратор'),
        ),
    ]
