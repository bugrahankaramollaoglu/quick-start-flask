from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>bbb<p>ccc<p>aaaa"

# çalıştırmak için terminalde:
# flask --app 1_start.py run --debugger --reload
# diyoruz. --debugger is like hotReload in flutter
# eğer .py dosyasının adı app ya da wsgi ise --app demene gerek kalmaz (kalıyor)
# ya da direkt kodda
# if __name__ == '__main__':
# 	app.run(debug=True)
# dersek de yetiyor


# http://127.0.0.1:5000 demek senin lokal bilgisayarından (127.0~)
# 5000 portundan ulaşmaya çalışıyosun demek. 5000 portu flask'ın default portu.
