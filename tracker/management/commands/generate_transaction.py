import random
from faker import Faker
from django.core.management.base import BaseCommand
from tracker import models as tracker_models



class Command(BaseCommand):
    help = 'Generates transaction for testing'

    def handle(self,*args,**kwargs):
        fake = Faker()

        categories = [
            "Bills",
            "Food",
            "Clothes",
            "Medical",
            "Housing",
            "Salary",
            "Social",
            "Transport",
            "Vacation",
        ]

        for category in categories:
            tracker_models.Category.objects.get_or_create(
                name=category
            )
        user = tracker_models.User.objects.filter(username='sahil').first()
        if not user:
            user = tracker_models.User.objects.create(
                username='sahil',password='test'
            )
        categories = tracker_models.Category.objects.all()
        types = [x[0] for x in tracker_models.Transaction.TRANSACTION_TYPE_CHOICES]
        for i in range(20):
            tracker_models.Transaction.objects.create(
                category=random.choice(categories),
                user=user,
                amount=random.uniform(1, 2500),
                date=fake.date_between(start_date='-1y', end_date='today'),
                type=random.choice(types)
            )