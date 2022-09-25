

from django.views.generic import ListView, DetailView, FormView, View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import ServiceForm, RequestorForm, ChangeRequestForm, ChangeRequestUpdateForm, NewUserForm
from .models import Service, Requestor, ChangeRequest, ChangeRequestUpdate
from django.urls import reverse

# Create your views here.


class ServiceListView(ListView):
    model = Service
    template_name = "main/service-list.html"


class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = "main/service-form.html"
    success_url = "/services"


class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = "main/service-form.html"
    success_url = "/services"


class ServiceDeleteView(DeleteView):
    model = Service
    success_url = "/services"
    template_name = "delete-confirmation.html"


class ServiceDetailView(DetailView):
    model = Service
    template_name = "main/service-detail.html"


class RequestorListView(ListView):
    model = Requestor
    template_name = "main/requestor-list.html"


class RequestorCreateView(CreateView):
    model = Requestor
    form_class = RequestorForm
    template_name = "main/requestor-form.html"
    success_url = "/requestors"


class RequestorUpdateView(UpdateView):
    model = Requestor
    form_class = RequestorForm
    template_name = "main/requestor-form.html"
    success_url = "/requestors"


class RequestorDeleteView(DeleteView):
    model = Requestor
    success_url = "/requestors"
    template_name = "delete-confirmation.html"


class RequestorDetailView(DetailView):
    model = Requestor
    template_name = "main/requestor-detail.html"


class ChangeRequestListView(ListView):
    model = ChangeRequest
    template_name = "main/request-list.html"


class ChangeRequestCreate(CreateView):
    model = ChangeRequest
    form_class = ChangeRequestForm
    template_name = "main/request-form.html"
    success_url = '/changes'


class ChangeRequestUpdateView(UpdateView):
    model = ChangeRequest
    form_class = ChangeRequestForm
    template_name = "main/request-form.html"
    success_url = '/changes'


class ChangeRequestDetailView(View):
    def get(self, request, *args, **kwargs):
        view = ChangeRequestView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostChangeRequestUpdate.as_view()
        return view(request, *args, **kwargs)


class ChangeRequestView(DetailView):
    model = ChangeRequest
    template_name = "main/request-detail.html"

    def get_context_data(self, **kwargs):
        context = super(ChangeRequestView, self).get_context_data(**kwargs)
        context['updates'] = ChangeRequestUpdate.objects.filter(
            change_request=self.get_object()).order_by('-date_time_posted')
        context['form'] = ChangeRequestUpdateForm()
        return context


class PostChangeRequestUpdate(SingleObjectMixin, FormView):
    model = ChangeRequest
    form_class = ChangeRequestUpdateForm
    template_name = "main/request-detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(PostChangeRequestUpdate, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        update = form.save(commit=False)
        update.change_request = self.object
        update.save()
        return super().form_valid(form)

    def get_success_url(self):
        change = self.get_object()
        return reverse('change-detail', kwargs={'pk': change.pk}) + '#updates'


class ChangeRequestDeleteView(DeleteView):
    model = ChangeRequest
    success_url = "/changes"
    template_name = "delete-confirmation.html"


class SignUpView(CreateView):
    form_class = NewUserForm
    success_url = '/accounts/login'
    template_name = 'registration/register.html'
