from flask import Flask, jsonify
# jsonify: convert dictionary to json

app = Flask(__name__)

stores = [
    {
        'name': 'Wasay Store',
        'items': [
            {
                'name': 'chocolate',
                'price': 15
            }
        ]
    }
]

# POST /store data: {name:}
@app.route('/store', methods = ['POST'])
def create_store():
    pass

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store():
    pass

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

# POST /store/<string:name>/item {name:, price}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store():
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store():
    pass    

app.run(port=5000)