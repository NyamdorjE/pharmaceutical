from django import forms
from django.shortcuts import render
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField, get_thumbnail


class Menu(models.Model):
    name = models.CharField(max_length=200)
    icon = models.FileField(verbose_name=_(
        "Icon"), upload_to="media/navigation/icon", max_length=100)
    url = models.URLField(verbose_name=_("Url"), max_length=200)
    is_special = models.BooleanField(verbose_name=_("boxed"), default=False)
    position = models.IntegerField(
        verbose_name=_('Menu position'), default="0")

    class Meta:
        verbose_name = "Navigation menu"
        ordering = ['position']

    def __str__(self):
        return self.name


class DropMenu(models.Model):
    parent_id = models.ForeignKey(
        "Menu", verbose_name=_("Dropdown navigation child"), on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255,)

    def __str__(self):
        return self.name


class Vision(models.Model):
    icon = models.FileField(upload_to='media/icon',
                            max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = RichTextField(
        blank=True, null=True, verbose_name=_('Контэнт'))
    position = models.IntegerField(default="0")

    class Meta:
        verbose_name = _("Vision")
        ordering = ['position']

    def __str__(self):
        return self.title


class Mission(models.Model):
    title = RichTextField(blank=True, null=True,
                          verbose_name=_('Mission content'))

    class Meta:
        verbose_name = _('Mission')
        ordering = ['title']

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    title = models.CharField(max_length=255)
    comment = models.CharField(max_length=550)

    class Meta:
        verbose_name = _("Testimonial")
        ordering = ['title']

    def __str__(self):
        return self.title


class Presidents(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media/website/presidents/',
                              height_field=None, width_field=None, max_length=None)
    position = models.IntegerField(default="0")

    class Meta:
        verbose_name = _('Presidents')
        ordering = ['-title']

    def __str__(self):
        return self.title


class CountNumber(models.Model):
    number = models.IntegerField(verbose_name=_('Numbers'))
    description = models.CharField(
        max_length=255, verbose_name=_('Description'))
    position = models.IntegerField(default='0')

    class Meta:
        verbose_name = _('Count number')
        ordering = ['position']


class faq(models.Model):
    question = models.CharField(max_length=500, verbose_name=_('Question'))
    answer = models.CharField(max_length=500, verbose_name=_('Answer'))
    position = models.IntegerField(default='0')

    class Meta:
        verbose_name = _('Faq')
        ordering = ['position']

    def __str__(self):
        return self.question


class partner(models.Model):
    image = models.FileField(upload_to='media/website/presidents/')
    position = models.IntegerField(default='0')

    class Meta:
        verbose_name = _("partner")
        ordering = ['position']


class aboutpagemission(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.CharField(
        max_length=255, verbose_name=_('Description'))
    icon = models.CharField(max_length=255)

    class Meta:
        verbose_name = _("aboutpagemission")
