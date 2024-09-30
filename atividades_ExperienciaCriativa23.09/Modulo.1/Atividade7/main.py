from flask import Flask, render_template
app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sensors')
def sensors():
    sensores = {'Umidade':22, 'Temperatura':23, 'Luminosidade':1034}
    return render_template('sensores.html', sensores=sensores)

@app.route('/actuators')
def actuators():
    atuadores = {'Interruptor':122, 'Lampada':1}
    return render_template('atuadores.html', atuadores=atuadores)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)