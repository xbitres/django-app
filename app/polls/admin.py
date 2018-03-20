from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date Information',    {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently', 'number_of_choices')
    list_filter = ['pub_date']
    search_fields = ['question_text']

# Register your models here.
admin.site.register(Question, QuestionAdmin)