import json
from flask import Flask,render_template, request

# Define a new Flask instance called "app"
app = Flask(__name__, static_url_path='/static', static_folder='static')

# Define a list of dictionaries to represent products
product_list = [
    {
        'id': 1,
        'name': 'Cola',
        'price': 10.99,
        'description': 'Description of Product 1',
        'image_url': '/Image/71YBmiSj-cL.jpg', 
        'quant': 10  
    },
    {
        'id': 2,
        'name': 'XL',
        'price': 19.99,
        'description': 'Description of Product 2',
        'image_url': '/Image/xl.jpg',
        'quant': 10 
    },
    {
        'id': 3,
        'name': 'Water',
        'price': 5.49,
        'description': 'Description of Product 3',
        'image_url': '/Image/waret.webp',
        'quant': 10 
    }
    ]

# Functions to save/load "Cart" list from/into a json file
def save_cart_to_json():
    with open('cart.json', 'w') as json_file:
        json.dump(cart, json_file)
        
def load_cart_from_json():
    try:
        with open('cart.json', 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return []

# Load the cart data when the application starts
cart = load_cart_from_json()

# calculate the total price of the cart - needs implement
# def total_price():
    # total = 0
    # for item in cart:
        # total = total + item.price
    # return total
        
# the endpoints functions
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/shop')
def shop():
    cart.append(request.args.get('product_selected'))
    # total = total_price()
    save_cart_to_json()
    return render_template('shop.html', product_list=product_list, cart = cart)
     

if __name__ == '__main__':
    app.run(debug=True, port=9000)
