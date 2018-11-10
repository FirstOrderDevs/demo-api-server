import pprint
from mongoengine import connect


def init():
    connect('fyp_data')

