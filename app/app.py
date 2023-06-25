from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/items', methods=['GET'])
def get_items():
    items = ['pen', 'iPhone', 'watch', 'USB']
    return jsonify(items)

if __name__ == '__main__':
    app.run()
