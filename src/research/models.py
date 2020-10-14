from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class ResearchCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Research Category "))

    def __str__(self):
        return self.title


class Research(models.Model):
    category = models.ForeignKey(
        ResearchCategory,
        verbose_name=_("Category"),
        on_delete=models.CASCADE,
        related_name="Research",
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_("Гарчиг"),
    )
    slug = models.SlugField(max_length=255, verbose_name=_("Slug"), unique=True)
    author = models.CharField(max_length=255, verbose_name=_("Үүсгэсэн"))
    content = RichTextField(blank=True, null=True, verbose_name=_("Контэнт"))
    image = models.ImageField(verbose_name=("Зураг"), upload_to="media/research/")
    created_on = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Хэзээ үүсгэсэн")
    )
    updated_on = models.DateTimeField(
        auto_now=True, verbose_name=_("Хэзээ засварласан")
    )

    class Meta:
        verbose_name = _("Судалгаа")
        verbose_name_plural = _("Судалгаа")
        ordering = ["created_on"]

    def __str__(self):
        return self.title


class LawCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Хууль тогтоомж "))

    class Meta:
        verbose_name = _("Legislation category")
        verbose_name_plural = _("Legislation category")
        ordering = ["title"]

    def __str__(self):
        return self.title


class Law(models.Model):
    category = models.ForeignKey(
        LawCategory,
        verbose_name=_("Legislation category"),
        on_delete=models.CASCADE,
        related_name="Law",
        blank=True,
        default="1",
    )
    title = models.CharField(verbose_name=_("Title"), max_length=128)
    pdf_file = models.FileField(
        verbose_name=_("Upload file"), upload_to="pdf_file", null=True, blank=True
    )
    views = models.IntegerField(default=0, editable=False)
    created_at = models.DateTimeField(
        verbose_name=_("Created on"),
        auto_now_add=False,
        default=timezone.now,
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(verbose_name=_("Updated on"), auto_now=True)

    class Meta:
        verbose_name = _("Legislation")
        verbose_name_plural = _("Legislations")
        ordering = ["title"]

    def __str__(self):
        return u"{0}".format(self.title)
