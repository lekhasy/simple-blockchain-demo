from flask import Flask, jsonify, request
from blockchain import Blockchain
from jsonify_helper import MyEncoder, to_json_string

app = Flask(__name__)
app.json_encoder = MyEncoder

block_chain = Blockchain(4)

pendingData = []


@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {
        'chain': block_chain.chain,
        'length': len(block_chain.chain)
    }
    return jsonify(response), 200


@app.route('/mine_block', methods=['GET'])
def mine_block():
    global pendingData

    if len(pendingData) == 0:
        return jsonify({
            "message": "pending data is empty, nothing no mine"
        }), 200

    block_chain.create_block(to_json_string(pendingData))
    pendingData = []
    return jsonify({
        "message": "Congratulations, You just mine a new block!",
        "new_block_index": block_chain.get_latest_block().index
    }), 200


@app.route('/is_valid', methods=['GET'])
def is_valid():
    return jsonify({'is_valid': block_chain.is_chain_valid(block_chain.chain)}), 200


@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.form['data']
    pendingData.append(data)
    return jsonify({
        "message": "data added",
        "pending data": pendingData
    }), 200


@app.route('/invalidate', methods=['POST'])
def invalidate():
    block_chain.chain[1].data = "tampered data"
    return jsonify({
        "message": "the data in block 2 has been be tampered"
    }), 200


app.run(host='0.0.0.0', port=5000)
