import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

# Fake Pop Script
import random
from first_app.models import Topic, Webpage, Person, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ["Social", "Search", "Marketplace", "News", "Games"]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        top = add_topic()

        # create fake data for the entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_webpage_name = fakegen.company()
        fake_person_name = fakegen.name()  # Generate fake name for person

        # create a new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_webpage_name)[0]

        # create a fake access record
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

        # Create a new Person entry (with fake name, email, and text)
        person = Person.objects.get_or_create(name=fake_person_name)[0]
        person.save()  # Save the person object to the database

        # Relate Person to AccessRecord (optional, if you want each AccessRecord to have a Person)
        acc_rec.person = person
        acc_rec.save()

if __name__ == '__main__':
    print("Populating script...")
    populate(20)  # Populate with 20 entries
    print("Populating complete!")
