from django.contrib import admin

from .models import Course, CourseContent


class CourseContentInline(admin.StackedInline):  # You can also use TabularInline for a compact layout
    model = CourseContent
    extra = 1  # Number of empty forms for adding new files
    fields = ('title', 'file', 'number')  # Fields to display
    ordering = ('number',)  # Order files by their number


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'teacher')  # Display these fields in the course list
    search_fields = ('title', 'category', 'teacher')  # Add search functionality
    inlines = [CourseContentInline]  # Embed the CourseContent form in the Course form
