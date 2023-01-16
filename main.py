from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from Flask!'


def game(): 
  return render_template


app.run(host='0.0.0.0', port=81)



# Anforderungen
  # 