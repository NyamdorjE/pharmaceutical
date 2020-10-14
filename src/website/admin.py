from django.contrib import admin
from .models import (
    Menu,
    DropMenu,
    Mission,
    Vision,
    Testimonial,
    Presidents,
    CountNumber,
    faq,
    partner,
    aboutpagemission,
    Carousel,
)

# Register your models here.


admin.site.register(Menu)

admin.site.register(DropMenu)

admin.site.register(Mission)

admin.site.register(Vision)

admin.site.register(Testimonial)

admin.site.register(Presidents)

admin.site.register(CountNumber)

admin.site.register(faq)

admin.site.register(partner)

admin.site.register(aboutpagemission)

admin.site.register(Carousel)