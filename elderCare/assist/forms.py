from django import forms
from tinymce.widgets import TinyMCE
from .models import Section

class TinyMCEWidget(TinyMCE):
	def use_required_attribute(self, *args):
		return False

class SectionForm(forms.ModelForm):
	
	widget=TinyMCEWidget(
		attrs={'required': False, 'cols': 30, 'rows': 10}
	)
    
	class Meta:
		model = Section
		fields = '__all__'

