import pprint
from mongoengine import connect


def init():
    connect('fyp_data_new', host='178.128.26.214', port=27017)

