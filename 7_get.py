from flask import Flask
from flask import request

# there are many http methods, the most common are GET and POST
# by default, a route only answers to GET requests
# you can use the methods argument of the route() decorator to handle different HTTP methods.

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return doTheLogin()
    else:
        return showTheLoginForm()


""" # or you can separate them like

@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()

 """
