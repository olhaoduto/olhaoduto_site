from flask import Flask,render_template
app = Flask(__name__, static_folder='static')


@app.route('/')
def main_page():
    return 'Olha o duto'

@app.route('/user/<user>')
def user_page(user):
    return render_template('index.html', user=user)



if __name__ == '__main__':
    app.run()
