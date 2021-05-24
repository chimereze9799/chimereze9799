from django import forms
from django.contrib.auth.models import user
from app_users.models import UserProfileInfo
from django.contrib.auth.forms import UsercreationForm

class UserForm('UserCreationForm'):
	email = forms.EmailField()

	class Meta():
		model = user 
		fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

		labels = [
		'password1'] ('Password'),
		['password2'] ('Confirm Password'),

class UserProfileInfoFormforms():
	bio = forms.CharField(required = 'false')
	tutor = 'tutor'
	student = 'student'
	executive = 'executive'
	user_types = [
	(student, 'student'),
	(executive, 'executive'),
	]
	user_types = forms.ChoiceField(required = True, choices = user_types)

	class Meta():
		model = UserProfileInfo
		fields = ('bio', 'profile_picture', 'user_type')