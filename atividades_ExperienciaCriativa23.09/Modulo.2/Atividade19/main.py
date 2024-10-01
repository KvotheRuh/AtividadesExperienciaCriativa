from flask import Flask, render_template, request
from sensors import sensor
from actuators import actuator

app= Flask(__name__)

app.register_blueprint(sensor, url_prefix='/')
app.register_blueprint(actuator, url_prefix='/')

users= {
    'user1': '1234',
    'user2': '1234'
}


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template("home.html")

#Cadastro Usuario
@app.route('/register_user')
def register_user():
    return render_template("register_user.html")

@app.route('/list_users')
def list_users():
    global users
    return render_template("users.html", users=users)

@app.route('/add_user',  methods=['GET', 'POST'])
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
@app.route('/login', methods = ['POST', 'GET'])
def login():
    return render_template("login.html")

@app.route('/validated_user', methods=['POST'])
def validated_user():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        print(user, password)
        if user in users and users[user] == password:
            return render_template('home.html')
        else:
            return '<h1> invalid credentials!<h1>'
    else:
        return render_template('login.html')


# Remover Usuarios
@app.route('/remove_user')
def remove_user():
    return render_template("remove_user.html", users=users)
    
@app.route('/del_user', methods=['GET', 'POST'])
def del_user():
    global users
    if request.method == 'POST':
        user = request.form['user']
    else:
        user = request.args.get('user', None)
    users.pop(user)
    return render_template("users.html" , users=users)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)