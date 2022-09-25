
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import RedirectView
from .views import ChangeRequestCreate, ChangeRequestDeleteView, ChangeRequestListView, ChangeRequestUpdateView, ChangeRequestDetailView, RequestorCreateView, RequestorDeleteView, RequestorDetailView, RequestorUpdateView, ServiceCreateView, ServiceDeleteView, ServiceDetailView, ServiceListView, RequestorListView, ServiceUpdateView

urlpatterns = [
    path("",
         login_required(RedirectView.as_view(url="/changes", permanent=True))),  # redirects from root url to requests default page
    path("changes",
         login_required(ChangeRequestListView.as_view()), name="change-list"),
    path("change/<int:pk>",
         login_required(ChangeRequestDetailView.as_view()), name="change-detail"),
    path("change/new",
         login_required(ChangeRequestCreate.as_view()), name="change-create"),
    path("change/<int:pk>/edit",
         login_required(ChangeRequestUpdateView.as_view()), name="change-update"),
    path("change/<int:pk>/delete",
         login_required(ChangeRequestDeleteView.as_view()), name="change-delete"),
    path("services",
         login_required(ServiceListView.as_view()), name="service-list"),
    path("service/<int:pk>",
         login_required(ServiceDetailView.as_view()), name="service-detail"),
    path("service/new",
         login_required(ServiceCreateView.as_view()), name="service-create"),
    path("service/<int:pk>/edit",
         login_required(ServiceUpdateView.as_view()), name="service-update"),
    path("service/<int:pk>/delete",
         login_required(ServiceDeleteView.as_view()), name="service-delete"),
    path("requestors",
         login_required(RequestorListView.as_view()), name="requestor-list"),
    path("requestor/<int:pk>",
         login_required(RequestorDetailView.as_view()), name="requestor-detail"),
    path("requestor/new",
         login_required(RequestorCreateView.as_view()), name="requestor-create"),
    path("requestor/<int:pk>/edit",
         login_required(RequestorUpdateView.as_view()), name="requestor-update"),
    path("requestor/<int:pk>/delete",
         login_required(RequestorDeleteView.as_view()), name="requestor-delete"),
]
