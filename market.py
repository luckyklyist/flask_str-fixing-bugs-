from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from model import Item
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

with app.app_context():
    # Create database tables
    db.create_all()

items = [{
        'id': 1,
        'name': 'Phone',
        'barcode': '893212299897',
        'price': 500
    }, {
        'id': 2,
        'name': 'Laptop',
        'barcode': '123985473165',
        'price': 900
    }, {
        'id': 3,
        'name': 'Keyboard',
        'barcode': '231985128446',
        'price': 150
    }]

@app.route("/")
@app.route('/Home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    return render_template('market.html', items=items)


if __name__ == '__main__':
    app.run(debug=True)