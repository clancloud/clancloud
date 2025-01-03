from flask import Flask
from flask import render_template
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@app.route("/")
@app.route('/<name>')
def hello_world(name=None):
    return render_template('index.html', person=name)

