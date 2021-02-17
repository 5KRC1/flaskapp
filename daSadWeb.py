from flask import Flask, escape, request, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/payment')
def usrdata():
    return render_template('userdata.html')

if __name__ == "__main__":
    app.run(debug=True)