from src.base.urls import Nurl
from django.urls import include
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _


urlpatterns = [
    Nurl("news/") > "src.news.views.NewsList",
    Nurl("news/<slug:slug>/") > "src.news.views.NewsDetail",
    Nurl("news/") > "src.news.views.NewsList",
    Nurl("sport/") > "src.news.views.SportList",
    Nurl("special/") > "src.news.views.SpecialNews",
    Nurl("research/") > "src.news.views.ResearchNews",
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
