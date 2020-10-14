from src.base.urls import Nurl
from django.urls import include
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    Nurl('research/') > 'src.research.views.ResearchList',
    Nurl('research/<slug:slug>/') > 'src.research.views.ResearchDetail',
    Nurl('law/') > 'src.research.views.LawList',
    Nurl('lawdetail/') > 'src.research.views.LawDetail',
    Nurl('lawdetail2/') > 'src.research.views.LawDetail2',
    Nurl('lawdetail3/') > 'src.research.views.LawDetail3',

    # Nurl('law/<slug:slug>/') > 'src.research.views.LawDetail',

]
