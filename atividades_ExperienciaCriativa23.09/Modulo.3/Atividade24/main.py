from flask import *
from login import login_user
from sensors import sensor
from actuators import actuator
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
import json
from fileinput import filename


#https://wokwi.com/projects/322577683855704658

temperature= 10
huminity= 10

atuadores_values= 1

app= Flask(__name__)
## __name__ is the application name

app.register_blueprint(login_user, url_prefix='/')
app.register_blueprint(sensor, url_prefix='/')
app.register_blueprint(actuator, url_prefix='/')

app.config['MQTT_BROKER_URL'] = 'mqtt-dashboard.com'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = ''  # Set this item when you need to verify username and password
app.config['MQTT_PASSWORD'] = ''  # Set this item when you need to verify username and password
app.config['MQTT_KEEPALIVE'] = 5000  # Set KeepAlive time in seconds
app.config['MQTT_TLS_ENABLED'] = False  # If your broker supports TLS, set it True

mqtt_client= Mqtt()
mqtt_client.init_app(app)

topic_subscribe1 = "/sensor_valor"
topic_subscribe2 = "/envia_mensagem"
topic_subscribe3 = "/actuator"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/tempo_real')
def tempo_real():
    global temperature, huminity
    values = {"temperature":temperature, "huminity":huminity}
    return render_template("tr.html", values=values)

@app.route('/publish')
def publish():
    return render_template('publish.html')

@app.route('/publish_message', methods=['GET','POST'])
def publish_message():
    request_data = request.get_json()
    publish_result = mqtt_client.publish(request_data['topic'], request_data['message'])
    return jsonify(publish_result)


@mqtt_client.on_connect()
def handle_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Broker Connected successfully')
        mqtt_client.subscribe(topic_subscribe1) # sensor valor
        # mqtt_client.subscribe(topic_subscribe2) # envia mensagem
        # mqtt_client.subscribe(topic_subscribe3) # actuator
    else:
        print('Bad connection. Code:', rc)

@mqtt_client.on_disconnect()
def handle_disconnect(client, userdata, rc):
    print("Disconnected from broker")


@mqtt_client.on_message()
def handle_mqtt_message(client, userdata, message):
    global temperature
    new_temperature = float(message.payload.decode())
    if new_temperature != temperature:
        temperature = new_temperature 

        if temperature >= 30:
            mqtt_client.publish("/envia_mensagem", "Temperatura Alta")
        else:
            mqtt_client.publish("/envia_mensagem", "Temperatura Normal")

    

    # if(message.topic==topic_subscribe2):
    #     global huminity
    #     huminity = message.payload.decode()




#Upload Arquivo

@app.route('/upload_arquivo', methods = ['GET'])
def upload_arquivo():
    return render_template("upload_arquivo.html")

@app.route("/upload_file", methods=['POST'])
def upload_file():
    f = request.files['arquivo'] 
    f.save(f'static/imgs/{f.filename}')
    return "Ok!"



#Erro 401

@app.errorhandler(401)
def nao_autorizado(error):
    return render_template('401.html'), 401

#Erro 403

@app.errorhandler(403)
def proibido(error):
    return render_template('403.html'), 403

#Erro 404

@app.errorhandler(404)
def pagina_nao_encontrada(error):
    return render_template('404.html'), 404

#Erro 408

@app.errorhandler(408)
def tempo_esgotado(error):
    return render_template('408.html'), 408

#Erro 429

@app.errorhandler(429)
def muitas_solicitacoes(error):
    return render_template('429.html'), 429

#Erro 500

@app.errorhandler(500)
def erro_servidor(error):
    return render_template('500.html'), 500

#Erro 503

@app.errorhandler(503)
def servico_indisponivel(error):
    return render_template('503.html'), 503
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)