from flask import Flask, escape, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'

db = SQLAlchemy(app)

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    postalNum = db.Column(db.Integer, nullable=False)
    street = db.Column(db.String(50), nullable=False)
    houseNum = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.id

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/userdata', methods=['POST', 'GET'])
def usrdata():
        return render_template('userdata.html')

@app.route('/finishOrder', methods=['POST', 'GET'])
def end():
    if request.method == 'POST':
        ime = request.form.get("firstName")
        priimek = request.form.get("lastName")
        mesto = request.form.get("city")
        posta = request.form.get("postalNumber")
        ulica = request.form.get("street")
        hisnaSt = request.form.get("houseNumber")
        drzava = request.form.get("country")

        if not ime or not priimek or not mesto or not posta or not ulica or not hisnaSt or not drzava:
            error_statement = "All form fields required!"
            return render_template('/userdata.html', error_statement=error_statement)

        else:
            firstname = request.form["firstName"]
            surname = request.form["lastName"]
            location = request.form["city"]
            postalCode = request.form["postalNumber"]
            streets = request.form["street"]
            numberOfHouse = request.form["houseNumber"]
            nation = request.form["country"]

            addOrder = Orders(name=firstname, lastName=surname, city=location, postalNum=postalCode, street=streets, houseNum=numberOfHouse, country=nation)


            try:
                db.session.add(addOrder)
                db.session.commit()
                return redirect('/finishOrder')
            except:
                return 'Error'

    else:
        orders = Orders.query.order_by(Orders.date)
        myList = []
        for j in orders:
            myList.append(j.name)
        i = len(myList) - 1
        order = orders[i]
        return render_template('/finishOrder.html', order=order)
    
@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    dataUpdate = Orders.query.get_or_404(id)

    if request.method == 'POST':
        dataUpdate.name = request.form["firstName"]
        dataUpdate.lastName = request.form["lastName"]
        dataUpdate.city = request.form["city"]
        dataUpdate.postalNum = request.form["postalNumber"]
        dataUpdate.street = request.form["street"]
        dataUpdate.houseNum = request.form["houseNumber"]
        dataUpdate.country = request.form["country"]

        try:
            db.session.commit()
            return redirect('/finishOrder')
        except:
            return 'ERROR'
    else:
        return render_template('/update.html', dataUpdate=dataUpdate)

@app.route('/thanks')
def thanks():
    return render_template('/thanks.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
