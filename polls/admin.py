from django.contrib import admin
from polls.models import Choice,Poll

## elements to interface with the automatic Django administration page

class ChoiceInline(admin.TabularInline):
    """ class to define 'Poll' choice display formatting"""
    model=Choice
    extra=2


class PollAdmin(admin.ModelAdmin):
    """ class to control the display of 'poll' objects on Django admin page"""
    fieldsets=[
       (None,		{'fields':['question']}),
       ('Date Informaiton',	{'fields':['pub_date'], 'classes':['collapse']}),
       ]
    inlines=[ChoiceInline]  ## list choice objects for this poll
    list_display=('question','pub_date','was_published_recently')
    list_filter=['pub_date'] ## adds customizable 'date' filter 
    search_fields = ['question'] ## adds search function for questions
    date_hierarchy='pub_date'  ## 

## registers 'Poll' and 'PollAdmin' classes with Django for use and 
## modification by the 'admin' page
admin.site.register(Poll, PollAdmin)
