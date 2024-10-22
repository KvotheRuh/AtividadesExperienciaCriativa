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
    atuadores = {'Interruptor':2, 'Lampada':4}
    return render_template('atuadores.html', atuadores=atuadores)

@app.route('/quarto')
def quarto():
    quarto = {'Atuadores':'/actuators'}
    return render_template('quarto.html', quarto=quarto)

@app.route('/banheiro')
def banheiro():
    banheiro = {'Sensores':'/sensors'}
    return render_template('banheiro.html', banheiro=banheiro)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)