from django import forms
from django.forms import fields, widgets
from .models import *

from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *


class BookingForm(forms.Form):

    def __init__(self,*args,**kwargs):
        self.pk = kwargs.pop('pk')
        super(BookingForm,self).__init__(*args,**kwargs)
        self.resource = Resource.objects.get(hospital_id = self.pk)

        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'

        self.fields['icu_beds'] = forms.IntegerField(max_value=self.resource.icu_beds, initial=0)
        self.fields['remdesivir'] = forms.IntegerField(max_value=self.resource.remdesivir, initial=0)
        self.fields['vaccine'] = forms.IntegerField(max_value=self.resource.vaccine, initial=0)
        self.fields['ventilators'] = forms.IntegerField(max_value=self.resource.ventilators, initial=0)

        self.helper.layout = Layout(
            
            Fieldset(
                '',
                'icu_beds',
                'remdesivir',
                'vaccine',
                'ventilators'
            ),
        
            FormActions(
                Submit('submit', 'Book')
            ),
            
        )

        self.helper.form_class = 'row mb-3'
        self.helper.label_class = 'col-sm-2 col-form-label'
        self.helper.field_class = 'col-sm-5'


resource_fields = (
    "icu_beds","remdesivir","vaccine", "ventilators", "hospital"
)    

class UpdateResourceForm(forms.ModelForm):
    class Meta:
        # defining which model to use
        model = Resource

        # defining what fields to be filled
        fields = resource_fields
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            
            Fieldset(
                '',
                Field("icu_beds"),
                Field("remdesivir"),
                Field("vaccine"), 
                Field("ventilators"),          
            ),
        
            FormActions(
                Submit('submit', 'Update')
            ),
            
        )
        # self.helper.add_input()


        self.helper.form_class = 'row mb-3'
        self.helper.label_class = 'col-sm-2 col-form-label'
        self.helper.field_class = 'col-sm-5'




hospital_fields = (
    "name", "address", "phonenumber", "image"
)
class AddHospitalForm(forms.ModelForm):
    class Meta:
        # defining which model to use
        model = Hospital

        # defining what fields to be filled
        fields = hospital_fields
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].widget = forms.Textarea(attrs={'rows': 3})
        # self.fields['image'].widget.attrs.update({})

        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            
            Fieldset(
                '',
                Field("name"),
                Field("address"),
                Field("phonenumber"), 
                Field("image"),          
            ),
        
            FormActions(
                Submit('submit', 'Next')
            ),
            
        )

        self.helper.form_class = 'row mb-3'
        self.helper.label_class = 'col-sm-2 col-form-label'
        self.helper.field_class = 'col-sm-5'


class UpdateHospitalForm(forms.ModelForm):
    class Meta:
        # defining which model to use
        model = Hospital

        # defining what fields to be filled
        fields = hospital_fields
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['address'].widget = forms.Textarea(attrs={'rows': 3})
        # self.fields['image'].widget.attrs.update({})

        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            
            Fieldset(
                '',
                Field("name"),
                Field("address"),
                Field("phonenumber"), 
                Field("image"),          
            ),
        
            FormActions(
                Submit('submit', 'Update')
            ),
            
        )

        self.helper.form_class = 'row mb-3'
        self.helper.label_class = 'col-sm-2 col-form-label'
        self.helper.field_class = 'col-sm-5'