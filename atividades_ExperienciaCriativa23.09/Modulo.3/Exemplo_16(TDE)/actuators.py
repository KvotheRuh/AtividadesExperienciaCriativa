from flask import Blueprint, request, render_template, redirect, url_for

actuator = Blueprint("actuator",__name__, template_folder="templates")

atuadores = {
    'Interruptor':22, 
    'Lampada':1,
    'Atuador 3':2
    }

# Adicionar Atuadores
@actuator.route('/registrar_actuator')
def register_actuator():
    return render_template("registrar_actuator.html")

@actuator.route('/list_actuator')
def list_actuator():
    global atuadores
    return render_template("atuadores.html", atuadores=atuadores)

@actuator.route('/add_actuator',  methods=['GET', 'POST'])
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

# Remover Atuador
@actuator.route('/remove_actuator')
def remove_actuator():
    return render_template("remove_actuator.html", atuadores=atuadores)
    
@actuator.route('/del_actuator', methods=['GET', 'POST'])
def del_actuator():
    global atuadores
    if request.method == 'POST':
        atuador = request.form['atuador']
    else:
        atuador = request.args.get('atuador', None)
    atuadores.pop(atuador)
    return render_template("atuadores.html" , atuadores=atuadores)


@actuator.route('/actuators')
def actuators():
    return render_template('atuadores.html', atuadores=atuadores)