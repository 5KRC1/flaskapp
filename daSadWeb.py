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

@app.route('/userdata')
def usrdata():
    return render_template('userdata.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)