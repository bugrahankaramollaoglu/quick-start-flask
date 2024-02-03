from flask import Flask, render_template

# static files genelde js, html, css, resim ve font
# dosyalarını tutan klasördür. flask bunları otomatik olarak
# bulur ve kullanır. bu klasörün adı static olmalıdır.

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
