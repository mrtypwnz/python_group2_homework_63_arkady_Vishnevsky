# Generated by Django 2.1.7 on 2019-03-07 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20190306_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('discount_from', models.DateTimeField()),
                ('discount_to', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('return_ticket', models.BooleanField(default='False')),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ticket_discount', to='webapp.Discount')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ticket_seat', to='webapp.Seat')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ticket_show', to='webapp.Show')),
            ],
        ),
    ]
