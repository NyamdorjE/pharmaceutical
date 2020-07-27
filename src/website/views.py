from django.shortcuts import render
from .models import DropMenu, Menu, Mission, Vision, Testimonial, Presidents, CountNumber, faq, partner, aboutpagemission
from src.news.models import Category, News
from src.research.models import Research
from src.courses.models import Course
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _
# Create your views here.


class Homepage(generic.ListView):
    queryset = News.objects.all().order_by('created_on')
    template_name = 'news/homepage.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)
        context['special'] = News.objects.filter(is_special='True')
        context['category'] = Course.objects.all()
        context['news'] = News.objects.all().order_by('-created_on')
        context['menu'] = Menu.objects.all()
        context['dropdown'] = DropMenu.objects.all()
        context['vision'] = Vision.objects.all()
        context['mission'] = Mission.objects.all()
        context['testimonial'] = Testimonial.objects.all()
        context['presidents'] = Presidents.objects.all()
        context['count'] = CountNumber.objects.all()
        context['faq'] = faq.objects.all()
        context['partner'] = partner.objects.all()

        return context

    # def get_context_data(self, **kwargs):
    #     context = super(Homepage, self).get_context_data(**kwargs)
    #     context['category_list'] = Category.objects.all()
    #     context['research'] = Research.objects.all().order_by('-created_on')
    #     context['lesson'] = Courses.objects.all().order_by('-created_on')

    #     return context


class TimeLine(generic.ListView):
    template_name = "news/timeline.html"
    queryset = News.objects.all().order_by('created_on')
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(TimeLine, self).get_context_data(**kwargs)
        context['special'] = News.objects.filter(is_special='True')
        context['category'] = Course.objects.all()
        context['news'] = News.objects.all().order_by('-created_on')

        return context

# class BasePage(TemplateView):
#     queryset = News.objects.all().order_by('-created_on')
#     template_name = "poll/base.html"


class AboutPage(TemplateView):
    template_name = "news/services.html"
    queryset = News.objects.all().order_by('created_on')
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(AboutPage, self).get_context_data(**kwargs)
        context['special'] = News.objects.filter(is_special='True')
        context['category'] = Course.objects.all()
        context['news'] = News.objects.all().order_by('-created_on')
        context['mission'] = aboutpagemission.objects.all()

        return context


class Greetings(TemplateView):
    template_name = "news/greetings.html"
