from django.contrib import admin
from .models import *
from simple_history.admin import SimpleHistoryAdmin
from django.utils.html import format_html

admin.site.register(office)
admin.site.register(Status)
admin.site.register(Labs_cabinets)

class ApplicationAdmin(SimpleHistoryAdmin):
    history_list_display = ['Дата', 'Работник', 'Кабинет', 'Статус', 'Коммент']

    def Дата(self, obj):
        return obj.date
    
    def Преподаватель(self, obj):
        return obj.auth_user
        
    def Кабинет(self, obj):
        return obj.number_cab
    
    def Статус(self, obj):
        return obj.status_application
        
    def Коммент(self, obj):
        return obj.comments

admin.site.register(Application, ApplicationAdmin)





