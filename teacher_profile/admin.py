from django.contrib import admin
from .models import Department, TeacherProfile

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_name', 'dept_id')
    search_fields = ('dept_name', 'dept_id')

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'department', 'email', 'phone_number')
    search_fields = ('full_name', 'department__Dept_name', 'email')
    list_filter = ('department',)

    # Optional: Customize the admin form layout
    fieldsets = (
        (None, {
            'fields': ('department', 'full_name', 'email', 'phone_number', 'address')
        }),
    )
