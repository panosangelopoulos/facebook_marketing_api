from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def hello_world():
    return render_template('login.html')


app.config['DEBUG'] = True
if __name__ == '__main__':
    app.run()
