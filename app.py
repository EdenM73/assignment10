from flask import Flask, redirect, url_for, render_template
from flask import request
from flask import session
from flask import jsonify
import requests
import asyncio
import random
from interact_with_DB import *
import mysql, mysql.connector
import os, sys

app = Flask(__name__)

# assignment10
from assignment10.assignment10 import assignment10

app.register_blueprint(assignment10)


# assignment 11
@app.route('/assignment11/users', methods=['GET', 'POST'])
def json_users():
    users = interact_db(query="select * from users", query_type='fetch')
    return_dict = {}
    for user in users:
        return_dict[f'user_{user.name}'] = {
            'first_name': user.name,
            'email': user.email
        }
    return jsonify(return_dict)


def json_users(number):
    res = requests.get(f'https://reqres.in/api/users/{number}')
    res = res.json()
    return res


@app.route('/assignment11/outer_source', methods=['GET', 'POST'])
def backend():
    num = 1
    if "number" in request.args:
        num = int(request.args['number'])
        users = json_users(num)
        return render_template('assignment11.html', users=users)
    else:
        return render_template('assignment11.html')


@app.route('/assignment12/restapi_users', defaults={'user_id': -1})
@app.route('/assignment12/restapi_users/<int:user_id>')
def get_user_func(user_id):
    if user_id == -1:
        user_id = 4
        return_dict = {}
        query = "select * from users WHERE id='%s';" % user_id
        users = interact_db(query=query, query_type='fetch')
        for user in users:
            return_dict[f'user_{user.id}'] = {
                'status': 'success',
                'name': user.name,
                'email': user.email,
            }
    else:
         query = 'select * from users where id=%s;' % user_id
         users = interact_db(query=query, query_type='fetch')
         print(type(user_id))
         if len(users) == 0:
            return_dict = {
             'status': 'failed',
             'message': 'user not found'
                }
         else:
            return_dict = {
                'status': 'success',
                'id': users[0].id,
                'name': users[0].name,
                'email': users[0].email,
             }
    return jsonify(return_dict)


if __name__ == '__main__':
    app.run()
