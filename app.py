from flask import Flask, render_template, url_for , request , redirect , session ,blueprints ,jsonify
import  mysql, mysql.connector
import os, sys

app = Flask(__name__)


# assignment10
from assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

if __name__ == '__main__':
    app.run()
