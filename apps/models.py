from django.db.models import Model, CharField


class Agents(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    email = CharField(max_length=255)
    phone = CharField(max_length=255)
    region = CharField(max_length=255)
