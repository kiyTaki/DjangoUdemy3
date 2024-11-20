from django.contrib import admin
from .models import Venda, ItensDoPedido
from .actions import nfe_emitida, nfe_nao_emitida

class ItemPedidoInLine(admin.TabularInline):
    model = ItensDoPedido
    extra = 1

class VendaAdmin(admin.ModelAdmin):
    list_filter = ('pessoa__doc',)
    search_fields =('id', 'pessoa__first_name', 'pessoa__doc__num_doc')
    #raw_id_fields = ('pessoa',)
    autocomplete_fields = ('pessoa',)
    list_display = ('id', 'pessoa__first_name', 'pessoa__doc__num_doc', 'nfe_emitida')
    actions = [nfe_emitida, nfe_nao_emitida]
    inlines = [ItemPedidoInLine]

    
#    def total(self,obj):
#        return obj.get_total()
#    
#    total.short_descriptio = 'Total'


admin.site.register(Venda, VendaAdmin)
admin.site.register(ItensDoPedido)