from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Person, Produto
from .forms import PersonForm
from django.contrib.auth.decorators import login_required

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import View

# Create your views here.

@login_required
def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})

@login_required
def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    
    return render(request, 'person_form.html', {'form': form})

@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    
    return render(request, 'person_form.html', {'form': form})

@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    
    return render(request, 'person_delete_confirm.html', {'form': form})

class PersonList(ListView):
    model = Person


class PersonDetail(DetailView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PersonCreate(CreateView):
    model = Person
    fields = [
        'first_name','last_name', 'age', 'salary', 'bio', 'photo' 
    ]
    success_url = '/clientes/person_list'


class PersonUpdate(UpdateView):
    model = Person
    fields = [
        'first_name','last_name', 'age', 'salary', 'bio', 'photo' 
    ]
    success_url = reverse_lazy('person_list_cbv')

class PersonDelete(DeleteView):
    model = Person
    #success_url = reverse_lazy('person_list_cbv')

    def get_success_url(self):
        return reverse_lazy('person_list_cbv')

class ProdutoBulk(View):
    def get(serf, request):
        produtos = ['Banana', 'Maça', 'Limao', 'Laranja', 'Pera', 'Melancia' ]
        list_produtos = []

        for produto in produtos:
            p = Produto(descricao = produto, preco = 10)
            list_produtos.append(p)
        
        Produto.objects.bulk_create(list_produtos)

        return HttpResponse('Funcionou')
