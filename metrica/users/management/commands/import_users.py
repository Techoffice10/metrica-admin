import csv
from django.core.management.base import BaseCommand
from users.models import User
from django.utils.timezone import make_aware
from datetime import datetime

class Command(BaseCommand):
    help = 'Import users from data.csv'

    def handle(self, *args, **kwargs):
        file_path = 'data.csv'  # Adjust path if needed
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    # Convert date to timezone-aware format
                    user_creation_date = make_aware(
                        datetime.strptime(row['user_creation_date'], '%Y-%m-%d %H:%M:%S')
                    )
                    # Create user record
                    User.objects.create(
                        full_name=row['full_name'],
                        phone_no=row['phone_no'],
                        alt_no=row['alt_no'],
                        company=row['company'],
                        service_type=row['service_type'],
                        location=row['location'],
                        user_name=row['user_name'],
                        port_no=row['port_no'],
                        rdp_password=row['rdp_password'],
                        node=row['node'],
                        internal_ip=row['internal_ip'],
                        email=row['email'],
                        email_password=row['email_password'],
                        pb_id=row['pb_id'],
                        pb_password=row['pb_password'],
                        branch=row['branch'],
                        ext_no=row['ext_no'],
                        notes=row['notes'],
                        user_creation_date=user_creation_date,
                        status=row['status'],
                    )
                    self.stdout.write(f"Successfully added user: {row['full_name']}")
                except Exception as e:
                    self.stdout.write(f"Error adding user {row['full_name']}: {e}")
