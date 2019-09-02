from flask import Flask, render_template, request
from typing import Tuple

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home() -> Tuple[str, int]:
    site = request.args.get('site')
    return render_template('home.jinja', stylesheets=['/static/css/home2.css'] if site == '2' else [])

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
