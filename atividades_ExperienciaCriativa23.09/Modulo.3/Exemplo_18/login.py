from flask import Blueprint, request, render_template, redirect, url_for

login_user = Blueprint("login", __name__, template_folder="templates")

users= {
    'user1': '1234',
    'user2': '1234'
}

#Cadastro Usuario
@login_user.route('/register_user')
def register_user():
    return render_template("register_user.html")

@login_user.route('/list_users')
def list_users():
    global users
    return render_template("users.html", users=users)

@login_user.route('/add_user',  methods=['GET', 'POST'])
def add_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
    else:
        user = request.args.get('user', None)
        password = request.args.get('password' , None)
    users[user] = password
    return render_template("users.html", users=users)


#Login
@login_user.route('/login', methods = ['POST', 'GET'])
def login():
    return render_template("login.html")

@login_user.route('/validated_user', methods=['POST'])
def validated_user():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        print(user, password)
        if user in users and users[user] == password:
            return render_template('home.html')
        else:
            return '<h1> invalid credentials!</h1>'
    else:
        return render_template('login.html')


# Remover Usuarios
@login_user.route('/remove_user')
def remove_user():
    return render_template("remove_user.html", users=users)
    
@login_user.route('/del_user', methods=['GET', 'POST'])
def del_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
    else:
        user = request.args.get('user', None)
    users.pop(user)
    return render_template("users.html" , users=users)