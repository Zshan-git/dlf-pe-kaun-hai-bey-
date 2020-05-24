from django import  forms
from .models import Orders

class Ordersform(forms.ModelForm):
    Item = forms.CharField(label = 'Item', widget = forms.TextInput(attrs={"placeholder":"Food?"}))
    quantity = forms.IntegerField(label = 'Quantity', initial = 1)
    Price = forms.IntegerField(label = 'Price', initial = 0)
    class Meta:
        model = Orders
        fields = [
            'Item',
            'quantity',
            'Accepted',
            'Price',
        ]
    def clean_Quantity(self, *args, ** kwargs):
        Quantity = self.cleaned_data.get("quantity")
        if Quantity > 0:
            return Quantity
        else:
            raise forms.ValidationError("Enter a valid quantity")

    def clean_Price(self, *args, ** kwargs):
        Price = self.cleaned_data.get("Price")
        if Price > 0:
            return Price
        else:
            raise forms.ValidationError("Enter a valid price")