# Generated by Django 3.1.2 on 2020-10-27 04:00

from decimal import Decimal
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import myapp.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.IntegerField(default=myapp.models.from_category_10, primary_key=True, serialize=False)),
                ('category_name_en', models.CharField(choices=[('onlinecasino', 'Online-Casino'), ('sportsbet', 'Sports-Bet'), ('slotmachine', 'Slot-Machine')], max_length=255)),
                ('category_name_de', models.CharField(choices=[('onlinecasino', 'Online-Casino'), ('sportwetten', 'Sportwetten'), ('automaten', 'Automaten')], max_length=255)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('changed_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.IntegerField(default=myapp.models.from_country_10, primary_key=True, serialize=False)),
                ('country_name_en', models.CharField(choices=[('austria', 'Austria'), ('germany', 'Germany'), ('switzerland', 'Switzerland')], max_length=255)),
                ('country_name_de', models.CharField(choices=[('osterreich', 'Österreich'), ('deutschland', 'Deutschland'), ('schweiz', 'Schweiz')], max_length=255)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('changed_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinanceType',
            fields=[
                ('financetype_id', models.IntegerField(default=myapp.models.from_finance_10, primary_key=True, serialize=False)),
                ('financetype_name_en', models.CharField(choices=[('partfinanced', 'Part-Financed'), ('percentagefinanced', 'Percentage-Financed'), ('fullyfinanced', 'Fully-Financed')], max_length=255)),
                ('financetype_name_de', models.CharField(choices=[('teilfinanzierung', 'Teilfinanzierung'), ('prozentfinanzierung', 'Prozentfinanzierung'), ('vollfinanzierung', 'Vollfinanzierung')], max_length=255)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('changed_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.IntegerField(default=myapp.models.from_100, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('telephone1', phonenumber_field.modelfields.PhoneNumberField(help_text='Contact phone number', max_length=128, region=None)),
                ('telephone2', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Contact phone number2', max_length=128, region=None)),
                ('email1', models.EmailField(max_length=254)),
                ('email2', models.EmailField(max_length=254)),
                ('street', models.CharField(max_length=255)),
                ('town', models.CharField(max_length=255)),
                ('postalcode', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('changed_date', models.DateTimeField(auto_now_add=True)),
                ('agree_condition', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.IntegerField(default=myapp.models.from_10, primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(17)])),
                ('state_name', models.CharField(choices=[('new', 'New'), ('processing', 'Processing'), ('waiting', 'Waiting'), ('lawsuitfiled', 'Lawsuit Filed'), ('won', 'Won'), ('inactive', 'Inactive'), ('lost', 'Lost')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lawyer',
            fields=[
                ('lawyer_id', models.IntegerField(default=myapp.models.from_200, primary_key=True, serialize=False)),
                ('fees_per_hour', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fees_per_service', models.DecimalField(decimal_places=2, max_digits=6)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('changed_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=1000, null=True)),
                ('person_id', models.OneToOneField(blank=True, db_column='person_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.person')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.IntegerField(default=myapp.models.from_300, primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('changed_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=1000, null=True)),
                ('person_id', models.OneToOneField(db_column='person_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.person')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('currency_id', models.IntegerField(default=myapp.models.from_1000, primary_key=True, serialize=False)),
                ('currency_name', models.CharField(max_length=100)),
                ('currency_short', models.CharField(choices=[('eur', 'EUR'), ('usd', 'USD'), ('chf', 'CHF')], max_length=100)),
                ('currency_symbol', models.CharField(max_length=100)),
                ('country_id', models.ForeignKey(db_column='country_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.country')),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('case_id', models.IntegerField(default=myapp.models.from_400, primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('changed_date', models.DateTimeField(auto_now_add=True)),
                ('customer_amount_lost', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('case_amount_claim', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True)),
                ('case_amount_won', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True)),
                ('case_amount_lost', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True)),
                ('lawyer_fees', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True)),
                ('court_fees', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True)),
                ('other_fees', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True)),
                ('earnings_from_claim', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True)),
                ('money_earned_netto', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True)),
                ('customer_loss_evidence', models.BooleanField()),
                ('customer_signed_contract', models.BooleanField()),
                ('lawyer_sent_letter_to_vendor', models.BooleanField()),
                ('fee_paid_to_lawyer', models.BooleanField()),
                ('lawyer_assigned', models.BooleanField()),
                ('lawsuit_has_been_filed', models.BooleanField()),
                ('lawsuit_won', models.BooleanField()),
                ('comment', models.CharField(max_length=1000, null=True)),
                ('customer_wants_financing', models.BooleanField()),
                ('is_customer_already', models.BooleanField()),
                ('customer_played_where', models.CharField(max_length=300, null=True)),
                ('customer_lost_amounttxt', models.CharField(max_length=200, null=True)),
                ('customer_message', models.CharField(max_length=1000, null=True)),
                ('category_id', models.ForeignKey(blank=True, db_column='category_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.category')),
                ('country_id', models.ForeignKey(blank=True, db_column='country_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.country')),
                ('currency_id', models.ForeignKey(db_column='currency_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.currency')),
                ('customer_id', models.ForeignKey(db_column='customer_id', on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
                ('financetype_id', models.ForeignKey(blank=True, db_column='financetype_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.financetype')),
                ('lawyer_id', models.OneToOneField(db_column='lawyer_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.lawyer')),
                ('state_id', models.ForeignKey(db_column='state_id', default='new', null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.state')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('admin', 'ADMIN'), ('user', 'USER')], default='admin', max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('changed_date', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('person_id', models.OneToOneField(db_column='person_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.person')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]