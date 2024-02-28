from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Order
from .serializers import OrderSerializer
from escpos.printer import Network

PRINTER_IP = "192.168.178.177"
# Create your views here.
@api_view(['GET'])
def test(request):
    if request.method == "GET":
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)

        # Initialize the printer
        printer = Network(PRINTER_IP)

        # Print a test receipt6
        printer.text("\n\n\n\n\n\n\n")
        printer.text("001\n")
        printer.text("Cola!\n")
        printer.text("Hamburger\n")
        printer.cut()

        # Close the connection
        printer.close()

        return Response(serializer.data)