from django.forms import ModelForm

from drugshop.models import product, stock, review


class productForm(ModelForm):
    class Meta:
        model = product
        fields = ('reference', 'name', 'price', 'description', 'cart', 'image')
        exclude = ('user',)


class productOffer(ModelForm):
    class Meta:
        model = product
        fields = ('discount',)
        exclude = ('user',)


class reviewForm(ModelForm):
    class Meta:
        model = review
        fields = "__all__"
        exclude = ('user',)


class stockForm(ModelForm):
    class Meta:
        model = stock
        fields = "__all__"
        exclude = ('user',)

