

from email import message
from django.shortcuts import redirect, render, HttpResponse, redirect
from . models import certificates, Projects, Tag
import requests
import json
from . models import contactEnquiry
from django.http import HttpResponseRedirect

# Create your views here.

# For Home Page
def homepage(request):
	return render(request, "main/home.html")
	# return HttpResponse('Hello World')

# For About Page
def about(request):
	return render(request, "main/about.html")

# For resume Page
def resume(request):
	if request.method == "GET":
		# result = []

		certificate = certificates.objects.all()

		# for certificate in certificates:
		# 	data = {
		# 		"image" : certificate.image,
		# 		"description" : certificate.description
		# 	}
		# 	result.append(data)
	return render(request, "main/resume.html", {'certificate':certificate})



# For Projects Page
def projects(request):
	if request.method == "GET":
		project = Projects.objects.all()


	return render(request, "main/projects.html", {'project':project} )

# For Blog Page
# def blog(request):
# 	return render(request, "main/blog.html")

# For Contact Page
def contact(request):
	if request.method == "POST":
		name = request.POST['name-1']
		email = request.POST['email']
		desc_msg = request.POST['msg']
		print(name, email, desc_msg)
		
		# recaptcha stuff
		clientkey = request.POST['g-recaptcha-response']
		secretkey = '6Ld8WLkeAAAAAIYwgnvQ2RqY0KwiQUKBGwYpSw3E'

		captchaData = {
			'secret': secretkey,
			'response': clientkey
		}

		r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
		response = json.loads(r.text)
		verify = response['success']
		print('Your response key is:', verify)
		if verify:
			return HttpResponse( '<script> alert("Message send Sucessfully ") </script>' )
		else:
			return HttpResponse( '<script> alert("Message send Sucessfully ") </script>' )
	
	return render(request, "main/contact.html")





#  To save enquiry from contact form

def saveEnquiry(request):
	if request.method == "POST":
		name = request.POST.get('name-1')
		email = request.POST.get('email')
		message = request.POST.get('msg')

		en = contactEnquiry(name=name, email=email, message=message)
		en.save()
		
	return redirect("contact")   

	# return render(request, "main/contact.html")

