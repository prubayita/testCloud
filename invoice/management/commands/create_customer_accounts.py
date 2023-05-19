from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from invoice.models import Customer

class Command(BaseCommand):
    help = 'Create customer accounts'

    def handle(self, *args, **options):
        customers = Customer.objects.all()
        for customer in customers:
            username = customer.email  # You can choose a different field as the username if desired
            password = User.objects.make_random_password()  # Generate a random password
            user = User.objects.create_user(username=username, password=password)
            # Associate the customer with the user account
            customer.user = user
            customer.save()
            self.stdout.write(self.style.SUCCESS(f"Created account for customer {customer.name}: username - {username}, password - {password}"))
