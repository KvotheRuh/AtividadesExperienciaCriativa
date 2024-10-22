from flask import Blueprint, request, render_template, redirect, url_for

sensor = Blueprint("sensor",__name__, template_folder="templates")

sensores = {
    'Umidade': 22, 
    'Temperatura': 23, 
    'Luminosidade': 1034,
    'Sensor 4' : 55}


# Adicionar Sensores
@sensor.route('/register_sensor')
def register_sensor():
    return render_template("register_sensor.html")

@sensor.route('/list_sensor')
def list_sensor():
    global sensores
    return render_template("sensores.html", sensores=sensores)

@sensor.route('/add_sensor',  methods=['GET', 'POST'])
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

# Remover Sensores
@sensor.route('/remove_sensor')
def remove_sensor():
    return render_template("remove_sensor.html", sensores=sensores)
    
@sensor.route('/del_sensor', methods=['GET', 'POST'])
def del_sensor():
    global sensores
    if request.method == 'POST':
        sensor = request.form['sensor']
    else:
        sensor = request.args.get('sensor', None)
    sensores.pop(sensor)
    return render_template("sensores.html" , sensores=sensores)

# Listas de sensores e atuadores
@sensor.route('/sensors')
def sensors():
    return render_template('sensores.html', sensores=sensores)
