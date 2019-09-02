from flask import Flask, render_template
from typing import Tuple

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home() -> Tuple[str, int]:
    return render_template('home.jinja')

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
