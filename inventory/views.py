from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    LaboratoriosModel,
    MarcasModel,
    TipoActivosModel,
    ActivosModel
)
from .forms import (
  LaboratoriosForm,
  MarcasForm,
  TipoActivosForm,
  ActivosForm
)


def index(request):
    return render(request, 'index.html')


def registros(request):
    return render(request, 'registros.html')


def viejos(request):
    old_items = ActivosModel.objects.filter(estado_uso="VIEJO")
    return render(request, 'filters/viejos.html', {'items': old_items})


def nuevos(request):
    new_items = ActivosModel.objects.filter(estado_uso="NUEVO")
    return render(request, 'filters/nuevos.html', {'items': new_items})


def get_laboratorios(request):
    laboratorios = LaboratoriosModel.objects.all()
    return render(
        request,
        'laboratories/index.html',
        {'laboratorios': laboratorios}
    )


def crearlaboratorios(request):
    formulario = LaboratoriosForm(request.POST or None,)
    if formulario.is_valid():
        formulario.save()
        return redirect('laboratorios')
    return render(
      request, 'laboratories/crear.html', {'formulario': formulario})


def editarlaboratorio(request, id):
    laboratorio = LaboratoriosModel.objects.get(id=id)
    formulario = LaboratoriosForm(
      request.POST or None, instance=laboratorio)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('laboratorios')
    return render(
      request, 'laboratories/editar.html', {'formulario': formulario})


def eliminarLaboratorio(request, id):
    LaboratoriosModel.objects.get(id=id).delete()
    return redirect('laboratorios')


def get_marcas(request):
    marcas = MarcasModel.objects.all()
    return render(
        request,
        'brands/index.html',
        {'marcas': marcas}
    )


def crearmarcas(request):
    if request.method == 'POST':
        formulario = MarcasForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('marcas')
    else:
        formulario = MarcasForm()
    return render(request, 'brands/crear.html', {'formulario': formulario})


def editarmarcas(request, id):
    laboratorio = MarcasModel.objects.get(id=id)
    formulario = MarcasForm(
      request.POST or None, instance=laboratorio)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('marcas')
    return render(
      request, 'brands/editar.html', {'formulario': formulario})


def eliminarmarcas(request, id):
    MarcasModel.objects.get(id=id).delete()
    return redirect('marcas')


def get_tipoequipos(request):
    marcas = TipoActivosModel.objects.all()
    return render(
        request,
        'asset_types/index.html',
        {'marcas': marcas}
    )


def crear_tipoequipos(request):
    if request.method == 'POST':
        formulario = TipoActivosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('tipoequipos')
    else:
        formulario = TipoActivosForm()
    return render(
      request, 'asset_types/crear.html', {'formulario': formulario})


def editar_tipoequipos(request, id):
    laboratorio = TipoActivosModel.objects.get(id=id)
    formulario = TipoActivosForm(
      request.POST or None, instance=laboratorio)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('tipoequipos')
    return render(
      request, 'asset_types/editar.html', {'formulario': formulario})


def eliminarequipo(request, id):
    TipoActivosModel.objects.get(id=id).delete()
    return redirect('tipoequipos')


def activos_list(request):
    activos = ActivosModel.objects.all()
    return render(request, 'equipment/index.html', {'activos': activos})


def activos_create(request):
    if request.method == 'POST':
        form = ActivosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('activos_list')
    else:
        form = ActivosForm()
    return render(request, 'equipment/index.html', {'form': form})


def activos_update(request, pk):
    activo = get_object_or_404(ActivosModel, pk=pk)
    if request.method == 'POST':
        form = ActivosForm(request.POST, request.FILES, instance=activo)
        if form.is_valid():
            form.save()
            return redirect('activos_list')
    else:
        form = ActivosForm(instance=activo)
    return render(request, 'equipment/index.html', {'form': form})


def activos_delete(request, pk):
    ActivosModel.objects.get(id=id).delete()
    return redirect('activos_list')
