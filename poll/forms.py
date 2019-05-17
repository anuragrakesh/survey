from django import forms
from .models import Register, Question


class regis_form(forms.ModelForm):
    f_name = forms.CharField(max_length=50, required=True,)
    l_name = forms.CharField(max_length=50, required=True)
    e_mail = forms.EmailField(required=True)
    m_no = forms.IntegerField(required=True)
    sex = forms.ChoiceField(widget=forms.RadioSelect,choices=(('f', 'female'), ('m', 'male')), required=True)
    dob = forms.DateField(widget= forms.SelectDateWidget, required=True)

    class Meta:
        model = Register
        fields = ['f_name', 'l_name', 'e_mail', 'm_no', 'sex', 'dob']


class ques_form(forms.ModelForm):
    ques_desc = forms.CharField(max_length=100)
    opa = forms.CharField(max_length=100)
    opb = forms.CharField(max_length=100)
    opc = forms.CharField(max_length=100)
    opd = forms.CharField(max_length=100)
    ans = forms.CharField(max_length=100)

    class Meta():
        model = Question
        fields = ['ques_desc', 'opa', 'opb', 'opc', 'opd', 'ans']
