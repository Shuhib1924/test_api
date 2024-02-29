from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
from escpos.printer import Network

PRINTER_IP = "192.168.178.177"
# Create your views here.
@api_view(['GET', 'POST'])
def test(request):
    if request.method == "GET":
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)

        # # Initialize the printer
        # printer = Network(PRINTER_IP)

        # # Print a test receipt6
        # printer.text("\n\n\n\n\n\n\n")
        # printer.text("001\n")
        # printer.text("Cola!\n")
        # printer.text("Hamburger\n")
        # printer.cut()

        # # Close the connection
        # printer.close()

        return Response(serializer.data)
    
    if request.method =="POST":
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def single_order(request, pk):
    try:
        order = Order.objects.get(id=pk)
    except Order.DoesNotExist():
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)
