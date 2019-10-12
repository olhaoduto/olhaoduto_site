
from flask import Flask,render_template
app = Flask(__name__, static_folder='static')




@app.route('/')
def inicio_page():
    return render_template('inicio.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/registrar')
def registrar_page():
    return render_template('registrar.html') 

@app.route('/reportar')
def reportar_page():
    return render_template('reportar.html') 

@app.route('/mapa')
def map_page():
    return render_template('map.html')

@app.route('/sobre')
def about_page():
    return render_template('sobre.html')


@app.route('/termos')
def termos_page():
    return render_template('termos.html')


if __name__ == '__main__':
    app.run()
