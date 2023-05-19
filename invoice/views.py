from django.shortcuts import render, get_object_or_404
from .models import Customer, Service, Receipt

def create_invoice(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer_id')
        service_id = request.POST.get('service_id')
        customer = get_object_or_404(Customer, pk=customer_id)
        service = get_object_or_404(Service, pk=service_id)
        receipt = Receipt.objects.create(customer=customer, service=service)
        return render(request, 'invoice/invoice_created.html', {'receipt': receipt})
    
    customers = Customer.objects.all()
    services = Service.objects.all()
    return render(request, 'invoice/create_invoice.html', {'customers': customers, 'services': services})

def view_invoice(request, receipt_id):
    receipt = get_object_or_404(Receipt, pk=receipt_id)
    return render(request, 'invoice/view_invoice.html', {'receipt': receipt})
