from django.db import models
from ckeditor.fields import RichTextField
import uuid
# Create your models here.

class MainSliderModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    background_image = models.ImageField(upload_to='mainslider')
    tagline = RichTextField()
    title = RichTextField()
    description = RichTextField()
    thm_text = RichTextField()
    thm_btn = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)