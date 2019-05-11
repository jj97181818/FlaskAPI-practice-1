from flask import Flask, jsonify, request, render_template
# jsonify: convert dictionary to json

app = Flask(__name__)

stores = [
    {
        'name': 'WasayStore',
        'items': [
            {
                'name': 'chocolate',
                'price': 15
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')


# POST /store data: {name:}
@app.route('/store', methods = ['POST'])
def create_store():
    request_data = request.get_json() # get_json: convert json to dictionary
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if (store['name'] == name):
            return jsonify(store)
    return jsonify({'message':'Can not find the store.'})

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

# POST /store/<string:name>/item {name:, price}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    new_item = {
        'name': request_data['name'],
        'price': request_data['price']
    }
    for store in stores:
        if (store['name'] == name):
            store['items'].append(new_item) 
            return jsonify(new_item)
    return jsonify({'message':'Can not find the store.'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if (store['name'] == name):
            return jsonify({'items': store['items']})
    return jsonify({'message': 'Can not find the store.'})

app.run(port=5000)