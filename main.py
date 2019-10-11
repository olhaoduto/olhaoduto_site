from flask import Flask,render_template
app = Flask(__name__, static_folder='static')


@app.route('/')
def main_page():
    return 'Olha o duto!'

@app.route('/user/<usuario>')
def user_page(usuario):
    return render_template('index.html', user=usuario)


@app.route('/map')
def map_page():
    return render_template('map.html')

@app.route('/inicio')
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


if __name__ == '__main__':
    app.run()
