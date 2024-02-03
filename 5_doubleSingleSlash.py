from flask import Flask

# şu iki url birbirinden farklıdır

app = Flask(__name__)

# decoratori tanimlarken trailing slash kullandigin icin sayfada
# 127.0.0.1:5000/deneme1/
# 127.0.0.1:5000/deneme1
# bu ikisini de kullanabilirsin, ikisi de returnü yazdirir
@app.route('/deneme1/')
def deneme1():
    return 'trailing slash'


# ama bu sayfada sadece
# 127.0.0.1:5000/deneme2 çalışır, sonuna / koyarsan çalışmaz
@app.route('/deneme2')
def deneme2():
    return 'not trailing slash'

if __name__ == '__main__':
    app.run(debug=True)
