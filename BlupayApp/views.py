# Create your views here.
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader

from models import Collector_Logs,Company,Terminal,Collector,Customer,Transaction_Type,Transaction,PoweredBy
from models import Terminal,Collector,Customer,Transaction_Type,Transaction


from datetime import date

import datetime, random, sha, hashlib


def get_post_login(request,t_id,uname,pword):
	try:
		collector = Collector.objects.get(username=uname)
		if collector.password==pword:
			log = Collector_Logs(name=str(collector.name), c_Username=str(uname), company=str(collector.company),terminal_id=t_id)
			log.save()
			return HttpResponse("Collector Exists!!")
		else:
			return HttpResponseForbidden("Forbidden!!, Collector does not exist!!")
	except Collector.DoesNotExist:	
		return HttpResponseForbidden("Forbidden!!, Collector does not exist!!")




def get_post_function(request,t_id,rf_id,amt=0.0,l_or_s_or_c=None,date_time=None):
	loan_balance = 0.0
	savings_balance = 0.0
	try:
		customer = Customer.objects.get(RfCard_id=rf_id)
		if int(l_or_s_or_c) == 0: #i.e loan

			loan_amt = float(customer.loanAmount) - float(amt)
			trans_type = 'Loan'
			customer.loanAmount = loan_amt
			customer.save()
			
		elif int(l_or_s_or_c) == 1: #i.e savings
			savings_balance = float(customer.savingsAmount) + float(amt)
			trans_type = 'Savings'
			customer.savingsAmount = savings_balance
			customer.save()
		
		elif int(l_or_s_or_c) == 2: #i.e collections
			collection_amt = float(customer.collectionAmount) - float(amt)
			trans_type = 'Collections'
			customer.collectionAmount = collection_amt
			customer.save()

		else:
			return HttpResponseForbidden("You do not have permission!!")
          
               
   		#random codes from online
		#random_number = User.objects.make_random_password(length=20, allowed_chars='123456789')

		#while User.objects.filter(userprofile__temp_password=random_number):
    		#	random_number = User.objects.make_random_password(length=10, allowed_chars='123456789')
		
			
		
               # key = hashlib.new(str(random.random()))
		trans_id_gen = random.randint(1,1000000000000)
            	#trans_id_gen = hashlib.new('TRANS'+str(key)).hexdigest()

               

		trans = Transaction(transaction_type=trans_type,paymentAmount = float(amt),terminal_id = t_id,transaction_id = trans_id_gen,RfCard_id =  rf_id,status=l_or_s_or_c, company=customer.company, customer_name=customer.name, collector_id = str(request.user.username))
		trans.save()
		#return HttpResponse('Name: '+str(customer.name)+'<br/>'+ 'Amount Paid: GHS '+str(trans.paymentAmount)+'<br/>'+ 'Loan Balance: GHS '+ str(customer.loanAmount)+'<br/>'+'Transaction Type: '+ trans_type+'<br/>'+'Transaction Id: '+str(trans_id_gen)+'<br/>')
		#print 'blupay1'
                pwdBy = PoweredBy.objects.get(pk=1)
		if trans_type == 'Loan':
			return HttpResponse('<b>'+str(customer.company)+'</b></br></br>LOAN REPAYMENT RECEIPT<br/>***************************</br>'+'Name: '+str(customer.name)+'<br/>'+ 'Amount Paid: GHS '+str(trans.paymentAmount)+'<br/>'+ 'Loan Balance: GHS '+ str(customer.loanAmount)+'<br/>'+'Transaction Id: '+str(trans_id_gen)+'<br/>'+'Timestamp: '+str(trans.date_created)+'<br/>***************************</br>Powered by <b>'+pwdBy.poweredByName+'&#0174;</b>')
			#return HttpResponseRedirect('https://dev.jallohenterprise.co.uk/visiontekconnect.php?userid=visiontek&password=12345&amount='+str(customer.loanAmount))
		elif trans_type == 'Savings':
			return HttpResponse('<b>'+str(customer.company)+'</b></br></br>SAVINGS RECEIPT<br/>***************************</br>'+'Name: '+str(customer.name)+'<br/>'+ 'Amount Paid: GHS '+str(trans.paymentAmount)+'<br/>'+ 'Savings Balance: GHS '+ str(customer.savingsAmount)+'<br/>'+'Transaction Id: '+str(trans_id_gen)+'<br/>'+'Timestamp: '+str(trans.date_created)+'<br/>***************************</br>Powered by <b>'+pwdBy.poweredByName+'&#0174;</b>')
			#return HttpResponseRedirect('https://dev.jallohenterprise.co.uk/visiontekconnect.php?userid=visiontek&password=12345&amount='+str(customer.savingsAmount))
		else:
			return HttpResponse('<b>'+str(customer.company)+'</b></br></br>COLLECTION REPAYMENT RECEIPT<br/>***************************</br>'+'Name: '+str(customer.name)+'<br/>'+ 'Amount Paid: GHS '+str(trans.paymentAmount)+'<br/>'+ 'Collection Balance: GHS '+ str(customer.collectionAmount)+'<br/>'+'Transaction Id: '+str(trans_id_gen)+'<br/>'+'Timestamp: '+str(trans.date_created)+'<br/>***************************</br>Powered by <b>'+pwdBy.poweredByName+'&#0174;</b>')

	except Customer.DoesNotExist:	
		return HttpResponseForbidden("Forbidden!!, Customer does not exist!!")

