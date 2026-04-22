from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria

# Create your views here.

def index(request):
    productos = Producto.objects.all()[:3]
    categorias = Categoria.objects.all()
    return render(request, 'index.html', {
        'productos': productos,
        'categorias': categorias
    })
   
def producto(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'producto.html', {
        'productos': productos,
        'categorias': categorias
    })

def productos_por_categoria(request, categoria_id):
    categorias = Categoria.objects.all()
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)

    return render(request, 'producto.html', {
        'productos': productos,
        'categorias': categorias,
        'categoria_actual': categoria
    })

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    categorias = Categoria.objects.all()

    return render(request, 'detalle.html', {
        'producto': producto,
        'categorias': categorias
    })

def agregar_carrito(request, id):
    carrito = request.session.get('carrito', {})

    if str(id) in carrito:
        carrito[str(id)] += 1
    else:
        carrito[str(id)] = 1

    request.session['carrito'] = carrito

    return redirect('producto')

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos = []
    total = 0

    for key, cantidad in carrito.items():
        try:
            producto = Producto.objects.get(id=key)
        except Producto.DoesNotExist:
            continue

        subtotal = producto.precio * cantidad

        productos.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal
        })

        total += subtotal

    # 🔥 ESTO FALTABA
    categorias = Categoria.objects.all()

    return render(request, 'carrito.html', {
        'productos': productos,
        'total': total,
        'categorias': categorias   
    })