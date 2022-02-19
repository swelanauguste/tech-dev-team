from django.db import models
from django.conf import settings

AUTH_USER = settings.AUTH_USER_MODEL


class TimeStampMixin(models.Model):
    """
    Base model that provides created and modified fields
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        AUTH_USER, on_delete=models.CASCADE, related_name="%(class)s_created"
    )
    modified_by = models.ForeignKey(
        AUTH_USER, on_delete=models.CASCADE, related_name="%(class)s_modified"
    )

    class Meta:
        abstract = True


class Documents(TimeStampMixin):
    """
    Model for storing documents
    """

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    document = models.FileField(upload_to="documents/")
    # uploaded_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
