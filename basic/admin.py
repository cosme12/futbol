from django.contrib import admin

# Register your models here.
from basic.models import CustomUser, League, Team, Player

#admin.site.site_header = "My Product Inventory "
#admin.site.site_title = "My Product Inventory "


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'id_team', 'last_login']
    #list_filter = ('position', )
    #fields = [('name', 'surname'), ]  # when editting


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'position', 'skill_current', 'skill_max', 'salary']
    list_filter = ('position', )
    #fields = [('name', 'surname'), ]  # when editting

#admin.site.register(CustomUser)
admin.site.register(League)
admin.site.register(Team)
#admin.site.register(Player, PlayerAdmin)
