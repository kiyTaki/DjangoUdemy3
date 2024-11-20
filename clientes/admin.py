from django.contrib import admin
from .models import Person, Documento


# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    fieldsets =(
        ('Dados pessoais', {'fields': ('first_name','last_name')}),
        ('Dados Complementares', {'fields': ('age', 'salary', 'doc')}),
        ('Demais Dados', {
            'classes':('collapse',),
            'fields': ('bio', 'photo')
            }),
    )
    list_filter = ('age', 'salary')

    #fields = [('first_name','last_name'), ('age', 'salary'), 'bio', 'photo', 'doc']
    list_display = ('first_name','last_name', 'age', 'salary', 'bio', 'tem_foto', 'doc')
    search_fields = ('id', 'first_name')

    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Não'
    
    tem_foto.short_description = 'Possui foto?'
        


    



admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)



