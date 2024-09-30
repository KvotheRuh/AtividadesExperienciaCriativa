from flask import Flask
app= Flask(__name__)
@app.route('/')
def index():
    return """
<html>
<head>
<title>Minha Casa</title>
</head>
<body>
<h2>Minha Casa</h2>
<h3>Menu Principal:</h3>
<ul>
<li><a href="/quarto">Quarto</a></li>
<li><a href="/banheiro">Banheiro</a></li>
</ul>
</body>
</html>
"""


@app.route('/quarto')
def quarto():
    return """
<html>
<head>
<title>Minha Casa</title>
</head>
<body>
<h1>Quarto</h1>
<ul>
<li>Sensor de Umidade</li>
<li>Interruptor</li>
</ul>
<p>Voltar para <a href="/">página inicial</a>!</p>
</body>
</html>
"""

@app.route('/banheiro')
def banheiro():
    return """

<html>
<head>
<title>Minha Casa</title>
</head>
<body>
<h1>Banheiro</h1>
<ul>
<li>Sensor de umidade</li>
<li>Lâmpada inteligente</li>
</ul>
<p>Voltar para <a href="/">página inicial</a>!</p>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)