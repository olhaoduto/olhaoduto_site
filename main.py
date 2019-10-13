
from flask import Flask,render_template
app = Flask(__name__, static_folder='static')




@app.route('/')
def inicio_page():
    return render_template('inicio.html')

@app.route('/sobre')
def sobre_page():
    return render_template('sobre.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/registrar')
def registrar_page():
    return render_template('registrar.html') 

@app.route('/reportar')
def reportar_page():
    return render_template('reportar.html') 

@app.route('/reportarLogado')
def reportarLogado_page():
    return render_template('reportar-membro.html') 
    
@app.route('/mapa')
def map_page():
    return render_template('map.html')

@app.route('/mapa_users')
def map_users_page():
    return render_template('map_users.html')

@app.route('/mapa_heat')
def map_heat_page():
    return render_template('map_heat.html')


@app.route('/sobre')
def about_page():
    return render_template('sobre.html')


@app.route('/termos')
def termos_page():
    return render_template('termos.html')

@app.route('/dashboard')
def dashboard_page():
    return render_template('dashboard.html')

@app.route('/dashboard-criticas')
def dashboardCriticas_page():
    return render_template('dashboard-criticas.html')

@app.route('/dashboard-postos')
def dashboardPostos_page():
    return render_template('dashboard-postos.html')

@app.route('/dashboard-crescimento')
def dashboardCrescimento_page():
    return render_template('dashboard-crescimento.html')

@app.route('/dashboard-unidades-policias')
def dashboardUnidadesPolicias_page():
    return render_template('dashboard-unidades-policias.html')

@app.route('/dashboard-milicias')
def dashboardMilicias_page():
    return render_template('dashboard-milicias.html')    

if __name__ == '__main__':
    app.run()
