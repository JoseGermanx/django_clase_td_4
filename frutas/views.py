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

def listar_productos(request):
    productos = ['Mouse','Teclado','Monitor']
    return render(request, 'frutas/productos.html', { 'productos': productos })

def error_404_handler(request, exception):
    return render(request, '404_error_handler.html', status=404)

def error_500_handler(request):
    return render(request, '500_error_handler.html', status=500)