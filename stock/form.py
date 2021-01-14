from django import forms
from .models import Stock

class StockModelForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = '__all__'
        widgets = {
            'stock_id': forms.NumberInput(attrs={'class': 'form-control is-valid'}),
            'stock_serial': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'stock_name': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'stock_specmain': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'stock_specsub': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'stock_cnts': forms.NumberInput(attrs={'class': 'form-control is-valid'}),
            'stock_totalcnt': forms.NumberInput(attrs={'class': 'form-control is-valid'}),
            'stock_price': forms.NumberInput(attrs={'class': 'form-control is-valid'}),
            'stock_totalprice': forms.NumberInput(attrs={'class': 'form-control is-valid'}),
            'stock_intime': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'stock_outtime': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'stock_comp': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'stock_compcatgo': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'stock_project': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'stock_warehouse': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'stock_sign': forms.TextInput(attrs={'class': 'form-control is-valid'}),
        }