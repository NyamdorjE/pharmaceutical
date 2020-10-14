from django.contrib import admin
from src.courses.models import Subject, Lesson, Course, CourseCategory
from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline

# Register your models here.


class InLineLesson(NestedTabularInline):
    model = Lesson
    extra = 1


class InLineSubject(NestedTabularInline):
    inlines = [InLineLesson]
    model = Subject
    extra = 1
    max_num = 1


class CourseAdmin(NestedModelAdmin):
    inlines = [InLineSubject]
    filter_horizontal = ('students',)
    list_display = ('title', 'description', 'price')
    list_filter = ('title',  'price')
    search_fields = ('title', 'slug')
    fieldsets = (
        (None, {
            "fields": (
                'category', 'title', 'price', 'description', 'image', 'students'
            ),
        }),
    )


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseCategory)
