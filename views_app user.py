from django.shortcut import render
from django.http import httpResponse, httpResponseRedirect
from app_users.form import Userform, UserProfileInfoForm 
from django.contrib.auth import authenticate, login, logout
from django import reverse
from django.contrib.auth.decorators import login_required 
# Create your views here 

def Index(request):
	return render(request, 'home.html')

def register(request):

	registered = 'false'

	if request.method == 'POST':
		user_form = Userform(data = request.POST)
		profile_form = UserProfileInfoForm(data = request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.save()

			profile = profile_form.save(commit = 'false')
			profile.user = user 
			profile.save()

			registered = True
		else: 
			print(user_form.errors, profile_form.errors)
	else:
		user_form = Userform()
		profile_form = UserProfileInfoForm()

	return render(request, 'app_users/registration.html'
							'(registered)' (registered),
							'user_form' (user_form), 
							'profile_form' (profile_form)
	)
def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username = username, password = password)

		if user:
			if user.is_active:
				login(request.user)
				return httpResponseRedirect(reverse('Index'))
			else:
				return httpResponse('ACCOUNT IS DEACTIVATED')
		else:
			return httpResponse("Please enter correct id and password")

	else:
		return render(request, 'app_users/login.html')

@login_required
def user_logout(request):
		logout(request)
		return httpResponseRedirect(reverse('Index'))




