from django.shortcuts import render
from django.http import JsonResponse
from .forms import AddressForm


def load_cities(request):
    country_id = request.GET.get("country")
    cities = City.objects.filter(country_id=country_id).order_by("name")
    return JsonResponse(list(cities.values("id", "name")), safe=False)


def address_form(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            # اطلاعات فرم معتبر است
            form.save()
            # انجام عملیات مورد نیاز
    else:
        form = AddressForm()
    return render(request, "your_template.html", {"form": form})
