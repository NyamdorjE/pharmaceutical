from django.http import request
from src.website.models import Carousel


def extras(request):
    carousel = Carousel.objects.all()
    return {"carousel": carousel}
