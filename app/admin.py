from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Member)

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "receiptNumber",)
  
admin.site.register(Member, MemberAdmin)