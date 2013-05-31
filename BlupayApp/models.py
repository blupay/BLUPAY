from django.contrib import admin
from django.db import models


from django.utils.timezone import now

class PoweredBy(models.Model):
	poweredByName = models.CharField(max_length=20)
	date_added = models.DateTimeField(auto_now_add=True)
      	date_updated = models.DateTimeField(auto_now=True)

class Collector_Logs(models.Model):
	name = models.CharField(max_length=20)
	c_Username = models.CharField(max_length=8)
	terminal_id = models.CharField(max_length=15)
	company = models.CharField(max_length=20)
	date_added = models.DateTimeField(auto_now_add=True)
      	date_updated = models.DateTimeField(auto_now=True)

	
	def __unicode__(self):
		return self.name
	

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=20)
	address = models.TextField(max_length=100)
	website = models.URLField(blank=True, null=True)
	telephone = models.CharField(max_length=10)
	date_added = models.DateTimeField(auto_now_add=True)
      	date_updated = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name = "Company"
		verbose_name_plural = "Companies"


class Terminal(models.Model):
	terminal_id = models.CharField(max_length=15)
	terminal_serial_no = models.CharField(max_length = 20)
	date_added = models.DateTimeField(auto_now_add=True)
      	date_updated = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.terminal_id
		

class Collector(models.Model):
	name = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=10, unique=True)
	username = models.CharField(primary_key=True, max_length=8)
	password = models.CharField(max_length=8)
	company = models.ForeignKey(Company)
	phone_number = models.PositiveIntegerField(unique=True)
	username = models.CharField(max_length=8,unique=True)
	password = models.CharField(max_length=8)
	residential_address = models.TextField(max_length=100)
	next_of_kin = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
      	date_updated = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.username


#CUSTOMER MODEL
class Customer(models.Model):
	name = models.CharField(max_length=20)
	telephone = models.CharField(max_length=10)
	telephone = models.PositiveIntegerField()
	address = models.TextField(max_length=100)
	date_added = models.DateTimeField(auto_now_add=True)
	RfCard_id = models.CharField(max_length =14)
      	date_updated = models.DateTimeField(auto_now=True)
	company = models.ForeignKey(Company)	
	account_number = models.CharField(max_length =12)
	savingsAmount = models.FloatField(null = True,default=0.0)
        loanAmount =  models.FloatField(null = True,default=0.0)
	collectionAmount =  models.FloatField(null = True,default=0.0)
	account_number = models.BigIntegerField(unique=True,null=False)
	savingsAmount = models.FloatField(null = True,default=0.0)
        loanAmount =  models.FloatField(null = True,default=0.0)
	#loanBalance = models.FloatField(null = True,default=loanAmount)
        
	def __unicode__(self):
		return self.name



#TRANSACTION TYPE MODEL
class Transaction_Type(models.Model):
	trans_type_name = models.CharField(max_length=20,unique=True)
	description = models.TextField(max_length=100,null=True)
	date_added = models.DateTimeField(auto_now_add=True)
      	date_updated = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.trans_type_name


class Transaction(models.Model):
	transaction_type=models.CharField(max_length=15)
	transaction_type=models.CharField(max_length=7)
	paymentAmount = models.FloatField(null = True,default=0.0)
	date_created = models.DateTimeField(auto_now_add=True)
      	date_updated = models.DateTimeField(auto_now=True)
	#customer = models.ForeignKey(Customer,related_name='transactions')
	collector_id = models.CharField(max_length=6)
        terminal_id = models.CharField(max_length = 15)
        terminal_id = models.CharField(max_length = 6)
        transaction_id = models.CharField(max_length = 20)
	RfCard_id = models.CharField(max_length =14)
	customer_name = models.CharField(max_length=20)
	status = models.PositiveIntegerField() # 0 means loans and 1 means saving
	company = models.ForeignKey(Company)
	

	def __unicode__(self):
		return self.transaction_id


class TransactionInline(admin.TabularInline):
	model = Transaction
#class CustomerInline(admin.TabularInline):
	#model = Customer


class PoweredByAdmin(admin.ModelAdmin):
	list_display = ('poweredByName','date_added','date_updated')
	list_filter = ('date_added','poweredByName')
	search_fields = ('poweredByName',)
	#inlines = [TransactionInline]
        ordering = ('-date_added',)

class Collector_LogsAdmin(admin.ModelAdmin):
	list_display = ('name','c_Username','date_added','date_updated','company')
	list_filter = ('date_added','c_Username','company')
	search_fields = ('c_Username','name','company')
	#inlines = [TransactionInline]
        ordering = ('-date_added',)

class CompanyAdmin(admin.ModelAdmin):
	list_display = ('name','address','website','telephone')
	list_filter = ('date_added','name')
	search_fields = ('name','website')
	ordering = ('-date_added',)

class CollectorAdmin(admin.ModelAdmin):
	list_display = ('name','phone_number','username','residential_address','next_of_kin','date_added','date_updated','company')
	list_filter = ('date_added','username')
	search_fields = ('username','name','company')

class CollectorAdmin(admin.ModelAdmin):
	list_display = ('name','phone_number','username','password','residential_address','next_of_kin','date_added','date_updated')
	list_filter = ('date_added','username')
	search_fields = ('username','name')
	#inlines = [TransactionInline]
        ordering = ('-date_added',)

class CustomerAdmin(admin.ModelAdmin):
	list_display =('name','telephone','address','account_number','RfCard_id','savingsAmount','loanAmount','collectionAmount','company','date_added','date_updated',)
	list_filter = ('date_added','account_number')
	search_fields = ('account_number','name','company')
	list_display = ('name','telephone','address','account_number','RfCard_id','savingsAmount','loanAmount','date_added','date_updated',)
	list_filter = ('date_added','account_number')
	search_fields = ('account_number','name')
	#inlines = [TransactionInline]
	ordering = ('-date_added',)

class Transaction_TypeAdmin(admin.ModelAdmin):
	list_display = ('trans_type_name','description')
	list_filter = ('date_added','trans_type_name')
	search_fields = ('trans_type_name','description')
	#inlines = [TransactionInline]
	ordering = ('-date_added',)

class TransactionAdmin(admin.ModelAdmin):
	list_display=('transaction_type','transaction_id','customer_name','paymentAmount',
			'terminal_id','collector_id','RfCard_id','status','company','date_created','date_updated')
	list_filter = ('date_created','transaction_type')
	search_fields = ('transaction_type','customer_name','company')
	list_filter = ('date_created','transaction_type')
	search_fields = ('transaction_type','customer_name')
	ordering = ('-date_created',)

class TerminalAdmin(admin.ModelAdmin):
	list_display = ('terminal_id','terminal_serial_no','date_added','date_updated')
	list_filter = ('terminal_id','terminal_serial_no')
	search_fields = ('terminal_id','terminal_serial_no')
	ordering = ('-date_added',)	



admin.site.register(PoweredBy,PoweredByAdmin)
admin.site.register(Collector_Logs,Collector_LogsAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(Terminal,TerminalAdmin)
admin.site.register(Collector,CollectorAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Transaction_Type,Transaction_TypeAdmin)
admin.site.register(Transaction,TransactionAdmin)


