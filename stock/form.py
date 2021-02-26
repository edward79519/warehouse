from django import forms
from .models import Stock, Stock2, Project, Company, Inaunit, Warehouse

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
            'stock_intime': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'stock_outtime': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'stock_comp': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'stock_compcatgo': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'stock_project': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'stock_warehouse': forms.TextInput(attrs={'class': 'form-control is-valid'}),
            'stock_sign': forms.TextInput(attrs={'class': 'form-control is-valid'}),
        }


class Stock2ModelForm(forms.ModelForm):

    class Meta:
        model = Stock2
        exclude = ['stock_isvalid']
        widgets = {
            'stock_change': forms.RadioSelect(attrs={'class': 'custom-control-input'}),
            'stock_sn': forms.TextInput(attrs={'class': 'form-control'}),
            'stock_item': forms.TextInput(attrs={'class': 'form-control'}),
            'stock_specmain': forms.TextInput(attrs={'class': 'form-control'}),
            'stock_specsub': forms.TextInput(attrs={'class': 'form-control'}),
            'stock_cnt': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_currency': forms.Select(attrs={'class': 'custom-select'}),
            'stock_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock_time': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'stock_comp': forms.Select(attrs={'class': 'custom-select'}),
            'stock_inaunit': forms.Select(attrs={'class': 'custom-select'}),
            'stock_proj': forms.Select(attrs={'class': 'custom-select'}),
            'stock_warehouse': forms.Select(attrs={'class': 'custom-select'}),
            'stock_sign': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProjectModelForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'proj_id': forms.TextInput(attrs={'class': 'form-control'}),
            'proj_name': forms.TextInput(attrs={'class': 'form-control'}),
            'proj_owner': forms.TextInput(attrs={'class': 'form-control'}),
            'proj_remark': forms.Textarea(attrs={'class': 'form-control'}),
            'proj_status': forms.Select(attrs={'class': 'custom-select'}),
            'proj_isvalid': forms.CheckboxInput(attrs={'class': 'custom-control-input'}),
            'proj_uptime': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'proj_downtime': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class CompanyModelForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'comp_id': forms.TextInput(attrs={'class': 'form-control'}),
            'comp_name': forms.TextInput(attrs={'class': 'form-control'}),
            'comp_spon': forms.TextInput(attrs={'class': 'form-control'}),
            'comp_tel': forms.TextInput(attrs={'class': 'form-control'}),
            'comp_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'comp_remark': forms.Textarea(attrs={'class': 'form-control'}),
        }


class InaunitModelForm(forms.ModelForm):

    class Meta:
        model = Inaunit
        fields = '__all__'
        widgets = {
            'ina_id': forms.TextInput(attrs={'class': 'form-control'}),
            'ina_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ina_shortname': forms.TextInput(attrs={'class': 'form-control'}),
            'ina_remark': forms.TextInput(attrs={'class': 'form-control'}),
            'ina_isvalid': forms.HiddenInput(),
        }


class WarehouseModelForm(forms.ModelForm):

    class Meta:
        model = Warehouse
        fields = '__all__'
        widgets = {
            'house_id': forms.TextInput(attrs={'class': 'form-control'}),
            'house_name': forms.TextInput(attrs={'class': 'form-control'}),
            'house_sponsor': forms.TextInput(attrs={'class': 'form-control'}),
            'house_loc': forms.TextInput(attrs={'class': 'form-control'}),
            'house_remark': forms.TextInput(attrs={'class': 'form-control'}),
            'house_isvalid': forms.HiddenInput(),
        }