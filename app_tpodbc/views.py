from django.shortcuts import render, redirect
from django.urls import reverse
from .utils import traer_ciudades, conn, cursor, traer_clientes
# Create your views here.


def index(request):
    return render(request, 'index.html')


def agregar_cliente(request):
    if request.method == 'POST':
        cursor.execute("{call SetAddressAndCustomer(?, ?, ?, ?, ?, ?, ?, ?, ?)}",
                       (request.POST['first-name'], request.POST['last-name'], int(request.POST['store-id']),
                        request.POST['email'], request.POST['address'], request.POST['district'],
                        int(request.POST['city']), request.POST['postal-code'], request.POST['phone']))
        conn.commit()
        return redirect('index')
    ciudades = traer_ciudades()
    context = {'ciudades': ciudades}
    return render(request, 'agregar_cliente.html', context)


def seleccionar_cliente(request):
    if request.method == 'POST':
        return redirect(reverse('modificar_cliente', args=(int(request.POST['customer-id']),)))
    return render(request, 'traer_cliente.html')


def modificar_cliente(request, client_id):
    if request.method == 'GET':
        cursor.execute("{call GetCustomerById(?)}", client_id)
        cliente = traer_clientes(cursor)[0]
        ciudades = traer_ciudades()
        context = {'cliente': cliente, 'ciudades': ciudades}
        return render(request, 'modificar_cliente.html', context)
    if request.method == 'POST':
        cursor.execute("{call ModifyAddressAndCustomer(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}",
                       (request.POST['first-name'], request.POST['last-name'], int(request.POST['store-id']),
                        request.POST['email'], request.POST['address'], request.POST['district'],
                        int(request.POST['city']), request.POST['postal-code'], request.POST['phone'],
                        int(request.POST['address-id']), int(request.POST['customer-id'])))
        conn.commit()
        return redirect('index')
    return render(request, 'index.html')


def buscar_cliente(request):
    if request.method == 'POST':
        first_name = request.POST['first-name'] if request.POST['first-name'] else None
        last_name = request.POST['last-name'] if request.POST['last-name'] else None
        city = int(request.POST['city']) if request.POST['city'] else None
        cursor.execute("{call GetCustomer(?, ?, ?)}", (first_name, last_name, city))
        clientes = traer_clientes(cursor)
        context = {'clientes': clientes}
        return render(request, 'ver_clientes.html', context)
    ciudades = traer_ciudades()
    context = {'ciudades': ciudades}
    return render(request, 'busqueda_clientes.html', context)


def eliminar_cliente(request):
    if request.method == 'POST':
        cursor.execute("{call DeleteCustomer(?)}", (int(request.POST['customer-id'])))
        conn.commit()
        return redirect('index')
    return render(request, 'eliminar_cliente.html')
