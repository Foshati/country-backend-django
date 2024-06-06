from django import forms
from cities_light.models import Country, City


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["country", "city"]

    country = forms.ModelChoiceField(
        queryset=Country.objects.all(), empty_label="Select a country"
    )
    city = forms.ModelChoiceField(
        queryset=City.objects.none(), empty_label="Select a city"
    )
