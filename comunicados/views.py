from django.shortcuts import render
from .models import Comunicado, Categoria

def comunicados_filter(request):
    niveles = Comunicado.NIVEL_CHOICES
    categorias = Categoria.objects.all()

    nivel_seleccionado = request.GET.get('nivel')
    categoria_seleccionada = request.GET.get('categoria')

    comunicados = Comunicado.objects.all().order_by('-fecha_envio')

    if nivel_seleccionado:
        comunicados = comunicados.filter(nivel=nivel_seleccionado)

    if categoria_seleccionada:
        comunicados = comunicados.filter(categoria__id=categoria_seleccionada)

    return render(request, 'comunicados_filter.html', {'comunicados': comunicados, 'niveles': niveles, 'categorias': categorias})


