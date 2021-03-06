from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "Pollster Fam"
admin.site.site_title = "Pollster Fam"
admin.site.index_title = "Welcome to my Practice App"

# this is where you are able to add admin functionality


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}), ]
    inlines = [ChoiceInline]


# on the admin view added Question and Choice CRUD
# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
