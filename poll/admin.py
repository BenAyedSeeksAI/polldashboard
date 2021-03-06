from django.contrib import admin
from .models import poll,choice
# Register your models here.
class choiceInLine(admin.TabularInline):
    model = choice
    extra = 3

class pollAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}), ]
    inlines = [choiceInLine]

admin.site.register(poll, pollAdmin)


#admin.site.register(poll)
#admin.site.register(choice)

