from django import forms
from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    
    knowledge_list = ["казино", "крипта", "криптовалюта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"] 

    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for item in self.knowledge_list:
            if item in cleaned_data:
                raise forms.ValidationError("название содержит недопустимое значение")
        
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for item in self.knowledge_list:
            if item in cleaned_data:
                raise forms.ValidationError("содержание содержит недопустимое значение")
        
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        exclude = ('product',)
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == "is_published":
                continue
            field.widget.attrs["class"] = "form-control"

    