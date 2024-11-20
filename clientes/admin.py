from django.contrib import admin
from .models import Person, Documento, Venda, Produto
from .actions import nfe_emitida, nfe_nao_emitida

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
        

class VendaAdmin(admin.ModelAdmin):
    list_filter = ('pessoa__doc',)
    search_fields =('id', 'pessoa__first_name', 'pessoa__doc__num_doc')
    #raw_id_fields = ('pessoa',)
    autocomplete_fields = ('pessoa',)
    list_display = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc', 'nfe_emitida')
    actions = [nfe_emitida, nfe_nao_emitida]
    filter_vertical = ['produtos', ]



admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto)
