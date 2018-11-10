from mongoengine import *
import json

import app.database as db
import app.users.RowData as row_data

db.init()


class User(Document):
    username = StringField(unique=True)
    email = EmailField(unique=True)
    name = StringField(required=True)
    password = StringField(required=True, min_length=4)
    type = StringField(choices=('s', 't', 'p'))
    row_data = MapField(field=StringField())
    predicted = MapField(field=StringField())


def create_user(user):
    # try:
        user = User(user['username'], user['email'], '', user['password'], user['type']).save()
        return {'success': True, 'user': json.loads(user.to_json())}
    # except Exception:
    #     return {'success': False}


def login_user(body):
    try:
        user = User.objects(username=body['username']).first()
        if user['password'] == body['password']:
            res = {'success': True, 'user': json.loads(user.to_json())}
            return res
        else:
            return {'success': False}
    except Exception:
        return {'success': False}


def update_data(body):
    user = User.objects.get(id=body['id'])
    for key, value in body['data'].items():
        user.row_data[key] = str(value)
    newuser = user.save()
    return {'success': True, 'newUser': json.loads(newuser.to_json())}
    