from django.contrib import admin

# Register your models here.

from .models import *

# admin.site.site_header="pollstar Admin"
# admin.site.site_title="pollstar Admin Area"
# admin.site.index_header=" Welcome to the pollstar Admin Area"

# class ChoiceInline(admin.TabularInline):
#     model=Choice
#     extra=3

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets=[(None,{'fields':['question_text']}),
#     ('Date Information',{'fields':['pub_date'],'classes':['collapse']}),]
#     inlines=[ChoiceInline]


admin.site.register(Choice)

admin.site.register(Question)
admin.site.register(Vote)
#admin.site.register(User)

# admin.site.register(Question,QuestionAdmin )