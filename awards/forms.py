from django import forms
from .models import Projects, Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio', 'info')

class UploadForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('project_name','project_photo','description','url')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['followers','following','user']