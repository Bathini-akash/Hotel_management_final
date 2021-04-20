from django.contrib import admin
from .models import Guest, Member,MemberPhone,MemberPass

admin.site.register(Guest)
admin.site.register(Member)
admin.site.register(MemberPhone)
admin.site.register(MemberPass)
# Register your models here.
