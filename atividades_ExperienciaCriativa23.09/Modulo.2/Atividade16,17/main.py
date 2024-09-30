from flask import Flask, render_template, request
app= Flask(__name__)
users= {
    'user1': '1234',
    'user2': '1234'
}

sensores = {
    'Umidade': 22, 
    'Temperatura': 23, 
    'Luminosidade': 1034,
    'Sensor 4' : 55}

atuadores = {
    'Interruptor':22, 
    'Lampada':1,
    'Atuador 3':2
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


# Adicionar Sensores
@app.route('/register_sensor')
def register_sensor():
    return render_template("register_sensor.html")

@app.route('/list_sensor')
def list_sensor():
    global sensores
    return render_template("sensores.html", sensores=sensores)

@app.route('/add_sensor',  methods=['GET', 'POST'])
def add_sensor():
    global sensores
    if request.method == 'POST':
        sensor = request.form['sensor']
        leitura = request.form['leitura']
    else:
        sensor = request.args.get('sensor', None)
        leitura = request.args.get('leitura' , None)
    sensores[sensor] = leitura
    return render_template("sensores.html", sensores=sensores)

# Adicionar Atuadores
@app.route('/registrar_actuator')
def register_actuator():
    return render_template("registrar_actuator.html")

@app.route('/list_actuator')
def list_actuator():
    global atuadores
    return render_template("atuadores.html", atuadores=atuadores)

@app.route('/add_actuator',  methods=['GET', 'POST'])
def add_actuator():
    global atuadores
    if request.method == 'POST':
        atuador = request.form['atuador']
        quantidade = request.form['quantidade']
    else:
        atuador = request.args.get('atuador', None)
        quantidade = request.args.get('quantidade' , None)
    atuadores[atuador] = quantidade
    return render_template("atuadores.html", atuadores=atuadores)



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


# Remover Sensores
@app.route('/remove_sensor')
def remove_sensor():
    return render_template("remove_sensor.html", sensores=sensores)
    
@app.route('/del_sensor', methods=['GET', 'POST'])
def del_sensor():
    global sensores
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor', None)
    sensores.pop(sensor)
    return render_template("sensores.html" , sensores=sensores)



# Remover Atuador
@app.route('/remove_actuator')
def remove_actuator():
    return render_template("remove_actuator.html", atuadores=atuadores)
    
@app.route('/del_actuator', methods=['GET', 'POST'])
def del_actuator():
    global atuadores
    if request.method == 'POST':
        atuador = request.form['atuador']
    else:
        atuador = request.args.get('atuador', None)
    atuadores.pop(atuador)
    return render_template("atuadores.html" , atuadores=atuadores)


# Listas de sensores e atuadores
@app.route('/sensors')
def sensors():
    return render_template('sensores.html', sensores=sensores)

@app.route('/actuators')
def actuators():
    return render_template('atuadores.html', atuadores=atuadores)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)