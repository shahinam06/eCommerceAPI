from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# to read products array from products.json file
def load_products_data():
    with open('products.json', 'r', encoding="utf-8") as file:
        return json.load(file)


# to write data to products array in the  products.json file
def save_products_data(products):
    with open('products.json', 'w') as file:
        json.dump(products, file, indent=4)


@app.route('/', methods=['GET'])
def index():
    return "Hello World!"


# to get all the products
@app.route('/products', methods=['GET'])
def get_products():
    data = load_products_data()
    return jsonify(data)


# to get the products  by id
@app.route('/products/<int:product_id>', methods=['GET'])
def get_products_by_id(product_id): 
    products = load_products_data() 
    product = None 
    for p in products:
        if p["id"] == product_id:
            product = p
            break 
    return jsonify(product) if product else ('Product Not Found', '404')


# to create a new product
@app.route('/products', methods=['POST'])
def create_products():
    new_product = request.json
    products = load_products_data()
    products.append(new_product)
    save_products_data(products)
    return(new_product)


# to update an existing product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    products = load_products_data()
    product = None
    for p in products:
        if p["id"] == product_id:
            product = p
            break

    updated_product = request.json 
    product.update(updated_product)
    save_products_data(products)
    return updated_product


#to delete a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def del_product(product_id):
    products = load_products_data()
    updated_list = list(filter(lambda p: p["id"] != product_id, products))
    save_products_data(updated_list)
    return "Deleted Successfully"


app.run(debug=True)