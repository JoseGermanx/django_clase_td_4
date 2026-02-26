from django.shortcuts import render

# Create your views here.

def listar_frutas(request):
    items = ['Manzana','Banana','Naranja', 'Sandía']
    return render(request, 'frutas/lista.html', {'items': items})

def vista_error(request):
    try:
        resultado = 1 / 0
    except ZeroDivisionError as err:
        return render(request, 'frutas/error.html', {'mensaje': err})