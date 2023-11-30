from django import forms
from .models import Obra

class Obraform(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ['titulo', 'presupuesto']
        widgets =  {
            'titulo': forms.TextInput(attrs= {'class':'form-control'}),
                  
        }
        
