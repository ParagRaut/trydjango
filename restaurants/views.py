from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import RestaurantLocation
from django.views.generic import DetailView, ListView, CreateView
from django.db.models import Q

from .forms import RestaurantCreateForm, RestaurantLocationCreateForm


def restaurants_createview(request):
    form = RestaurantLocationCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/restaurants')
    if form.errors:
        print(form.errors)
    template_name = 'restaurants/form.html'
    context = {"form": form}
    return render(request, template_name, context)


class RestaurantCreateView(CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/form.html'
    success_url = '/restaurants'


class RestaurantList(ListView):
    template_name = 'restaurants/restaurantlocation_list.html'

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(Q(category__iexact=slug) | Q(category__icontains=slug))
        else:
            queryset = RestaurantLocation.objects.all()
            return queryset
        return queryset


class RestaurantDetail(DetailView):
    queryset = RestaurantLocation.objects.all()


class HomePage(View):
    template_name = 'home.html'
    context = {'obj_list': [1, 2, 3]}

    def get(self, request):
        return render(request, self.template_name, self.context)


class AboutUs(View):
    template_name = 'about.html'
    context = {'obj_list': [1, 2, 3]}

    def get(self, request):
        return render(request, self.template_name, self.context)


class ContactUs(View):
    template_name = 'contact.html'
    context = {'obj_list': [1, 2, 3]}

    def get(self, request):
        return render(request, self.template_name, self.context)
