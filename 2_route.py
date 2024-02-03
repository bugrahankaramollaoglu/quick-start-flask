from flask import Flask

app = Flask(__name__)

@app.route('/')
def entry():
    return 'entry page'


@app.route('/first')
def first():
    return 'first page'


@app.route('/second')
def second():
    return 'second page'

# flask --app 2_route.py run --debugger --reload ile çalıştırıyoruz
# bu sayede sayfa açılınca adres çubuğunda
# http://127.0.0.1:5000/
# http://127.0.0.1:5000/first
# http://127.0.0.1:5000/second diyerek ilgili sayfalara gidebiliyoruz
