from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	with open('settings.txt', encoding='utf8') as config:
                data = config.read()
                settings = json.loads(data)
	return render_template('index.html', **settings)