from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class MembershipRequest(models.Model):
    MILITARY_BRANCHES = [
        ("Army", "Army"),
        ("Navy", "Navy"),
        ("Air Force", "Air Force"),
        ("Marines", "Marines"),
        ("Coast Guard", "Coast Guard"),
        ("Space Force", "Space Force"),
        ("Other", "Other"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(
        max_length=14,
        validators=[RegexValidator(
            regex=r'^\(\d{3}\) \d{3}-\d{4}$',
            message="Phone number must be in the format (555) 555-5555"
        )]
    )
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(
        max_length=10,
        validators=[RegexValidator(
            regex=r'^\d{5}(-\d{4})?$',
            message="Enter a valid zip code"
        )]
    )
    motorcycle_make = models.CharField(max_length=100)
    motorcycle_model = models.CharField(max_length=100)
    military_service = models.CharField(max_length=3, choices=[("Yes", "Yes"), ("No", "No")])
    military_branch = models.CharField(max_length=20, choices=MILITARY_BRANCHES, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    has_viewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.military_branch if self.military_branch else 'Civilian'}"

class AssistanceRequest(models.Model):

    ASSISTANCE_TYPES = [
        ("Volunteer", "Volunteer"),
        ("Monetary", "Monetary"),
        ("Attend Event", "Attend Event"),
        ("Escort", "Escort"),
        ("Other", "Other"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()])
    phone_number = models.CharField(
        max_length=14,
        validators=[RegexValidator(
            regex=r'^\(\d{3}\) \d{3}-\d{4}$',
            message="Phone number must be in the format (555) 555-5555"
        )]
    )
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(
        max_length=10,
        validators=[RegexValidator(
            regex=r'^\d{5}(-\d{4})?$',
            message="Enter a valid zip code"
        )]
    )
    type_of_assistance = models.CharField(max_length=20, choices=ASSISTANCE_TYPES)
    assistance_description = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    has_viewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.city}, {self.state}"
