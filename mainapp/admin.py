from django.contrib import admin

from .models import User_work, Organizations, Organization_defaulr_wt, UserList, Work_time

class User_workAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'organization', 'login', 'passvord', )
    list_display_links = ('id', 'name')
    search_fields = ('name', 'organization')
    ordering = ('name', 'last_name', 'login')



class OrganizationsAdmin(admin.ModelAdmin):
    list_display = ('id','group', 'email', )   
    search_fields = ('group',) 
    list_filter = ('group', 'email')
    

class Work_TimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'organization', 'start_time', 'end_time','created_ad')
    list_display_links = ('id', 'user')
    search_fields = ('user', 'organization', 'start_time', 'end_time')  
    list_filter = ('user', 'organization', 'start_time', 'end_time') 
     


class UserListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'organization', )
    search_fields = ('name_list','organization' ) 

 
class Organization_defaulr_wtAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_time', 'end_time', )  
    list_display_links = ('id', 'name') 
    search_fields = ('name', 'srart_time', 'end_time')
    

admin.site.register(User_work, User_workAdmin)
admin.site.register(Organizations,OrganizationsAdmin )
admin.site.register(UserList, UserListAdmin)
admin.site.register(Organization_defaulr_wt,Organization_defaulr_wtAdmin )
admin.site.register(Work_time, Work_TimeAdmin)