from flask import Flask, request, jsonify
from uuid import uuid4
import math

app = Flask(__name__)
receipts = {}


def cauculate_points(id: str) -> int:
    point = 0

    receipt = receipts[id]
    retailer = receipt['retailer']
    for char in retailer:
        if char.isalnum():
            point += 1

    if float(receipt['total']) % 1 == 0:
        point += 50

    if float(receipt['total']) % 0.25 == 0:
        point += 25

    point += (len(receipt['items']) // 2) * 5

    for item in receipt['items']:
        if len(item['shortDescription'].strip()) % 3 == 0:
            point += math.ceil(float(item['price']) * 0.2)

    day = receipt['purchaseDate'].split('-')[-1]
    if int(day) % 2 == 1:
        point += 6

    time = receipt['purchaseTime'].split(':')[0]
    if 14 <= int(time) < 16:
        point += 10
    return point


@app.route('/receipts/process', methods=['POST'])
def process():
    if request.is_json:
        try:
            receipt = request.json
            receipt_id = str(uuid4())

            receipts[receipt_id] = receipt
            return jsonify({"id": receipt_id}), 200
        except Exception as e:
            return jsonify({"error": f"Unexpected error: {str(e)}"}), 400
    else:
        return jsonify({"error": "Invalid Content-Type. Expected json"}), 400


@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_points(receipt_id):
    try:
        point = cauculate_points(receipt_id)
        return jsonify({"points": point}), 200
    except Exception as e:
        return jsonify({"error": e}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)