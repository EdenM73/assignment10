from flask import Flask, render_template, url_for, session, request, redirect, Blueprint, flash
import mysql
import mysql.connector
from interact_with_DB import interact_db

assignment10 = Blueprint('assignment10', __name__, static_folder='static', template_folder='templates')


@assignment10.route('/')
def ex10_printusers():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=users)


@assignment10.route('/insert_user', methods=['POST'])
def ex10_insert():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    query = "INSERT INTO users(name , email,password) VALUES ('%s' ,'%s' ,'%s');" % (name, email, password)
    interact_db(query=query, query_type='commit')
    return redirect('/')


@assignment10.route('/delete_user', methods=['POST'])
def ex10_delete():
    user_id = request.form['id']
    query = "DELETE FROM users WHERE id='%s';" % user_id
    interact_db(query=query, query_type='commit')
    return redirect('/')


@assignment10.route('/update_user', methods=['POST'])
def ex10_UPDATE():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    query = "UPDATE users SET name ='%s' ,password='%s' WHERE email='%s';" % (name, password, email)
    interact_db(query=query, query_type='commit')
    return redirect('/')


