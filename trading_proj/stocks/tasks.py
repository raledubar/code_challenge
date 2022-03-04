from tkinter import N
from celery import shared_task
from .models import Toy
from celery.decorators import periodic_task
from celery.task.schedules import crontab

@shared_task
def create_toy_object(value):
    Toy.objects.create(value=value)


@periodic_task(run_every=(crontab(minute='*/1')))
def run_create_objs():
    create_toy_object.delay(int('123'))