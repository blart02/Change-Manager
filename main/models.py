
from django.db import models
from django.urls import reverse

# Create your models here.


class Service (models.Model):
    name = models.CharField(max_length=50)

    BUSINESS_UNIT_OPTIONS = (
        ("Group", "Group"),
        ("Insight Healthcare", "Insight Healthcare"),
        ("Mental Health Concern", "Mental Health Concern"),
    )

    business_unit = models.CharField(
        max_length=50, choices=BUSINESS_UNIT_OPTIONS)
    description = models.TextField(null=True, blank=True)
    main_contact_number = models.CharField(
        max_length=18, null=True, blank=True)
    parent_service = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name="child_services")

    def get_absolute_url(self):
        return reverse('service-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name + ', ' + self.business_unit


class Requestor (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_approver = models.BooleanField()
    contact_number = models.CharField(max_length=18)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    line_manager = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL, related_name="staff")

    @property
    def name(self):
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('requestor-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    @property
    def is_approver_str(self):
        if self.is_approver:
            return "Yes"
        else:
            return "No"


class ChangeRequest (models.Model):
    requestor = models.ForeignKey(
        Requestor, on_delete=models.CASCADE, related_name="requestor_changes")
    approver = models.ForeignKey(
        Requestor, on_delete=models.PROTECT, related_name="approver_changes")
    date_requested = models.DateField(auto_now_add=True)

    PRIORITY_OPTIONS = (
        ("Highest", "Highest"),
        ("Very High", "Very High"),
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    )

    priority = models.CharField(max_length=50, choices=PRIORITY_OPTIONS)

    STATUS_OPTIONS = (
        ("New", "New"),
        ("Clinical Assessment", "Clinical Assessment"),
        ("Awaiting Prioritisation", "Awaiting Prioritisation"),
        ("Backlog", "Backlog"),
        ("Development", "Development"),
        ("Testing", "Testing"),
        ("Deployment", "Deployment"),
        ("Complete", "Complete"),
    )

    status = models.CharField(
        max_length=50, choices=STATUS_OPTIONS, default="New")

    title = models.CharField(max_length=50)
    description = models.TextField()
    date_completed = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('change-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class ChangeRequestUpdate (models.Model):
    change_request = models.ForeignKey(ChangeRequest, on_delete=models.CASCADE)
    text = models.TextField()
    date_time_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
