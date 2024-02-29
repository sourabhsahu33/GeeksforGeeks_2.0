from django import forms
from .models import Subject
 

# ============= CGPA Calcualtor Form ============ 
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name','credit', 'grade']