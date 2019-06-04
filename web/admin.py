from django.contrib import admin
from .models import NlpReponse
from .models import Student

# Register your models here.
# @admin.register(NlpReponse)
# class NlpTypeAdmin(admin.ModelAdmin):
#     list_display = ('pk','taskId','callId','timestamp','code','msg')

@admin.register(Student)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')