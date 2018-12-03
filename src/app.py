from flask import Flask, jsonify, request
from kscoin.ksCoin import KSCoin
from helpers.jsonifyHelper import MyEncoder, to_json_string

app = Flask(__name__)
app.json_encoder = MyEncoder

ksCoin = KSCoin()

@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {
        'chain': ksCoin.chain,
        'length': len(ksCoin.chain)
    }
    return jsonify(response), 200


@app.route('/mine_block', methods=['GET'])
def mine_block():
    ksCoin.mine_new_block()
    return jsonify({
        "message": "Congratulations, You just mine a new block!",
        "new_block_index": ksCoin.get_latest_block().index
    }), 200


@app.route('/is_valid', methods=['GET'])
def is_valid():
    return jsonify({'is_valid': ksCoin.is_chain_valid(ksCoin.chain)}), 200


@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.form['data']
    ksCoin.add_transaction(data)
    return jsonify({
        "message": "data added",
        "pending data": ksCoin.get_mempool()
    }), 200


@app.route('/invalidate', methods=['POST'])
def invalidate():
    ksCoin.chain[1].data = "tampered data"
    return jsonify({
        "message": "the data in block 2 has been be tampered"
    }), 200


app.run(host='0.0.0.0', port=5000)
