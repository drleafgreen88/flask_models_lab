from flask import render_template
from app import app
from models.order_info import orders

@app.route('/')
def index():
    return render_template('index.html', title="Home!", order_info=orders)

@app.route('/<index>')
def order(index):
    return render_template('order.html', title="My Order", order_info=orders[int(index)-1])
    # return render_template('index.html', title="Home!", order_info=orders)