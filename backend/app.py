from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="../frontend/spoticry/build/", static_url_path="/")

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    input_value = data.get('input_data')

    result = {'message': f'Received: {input_value}'}
    return jsonify(result)

@app.route("/")
def hello():
    return send_from_directory(app.static_folder, "index.html") 
    
if __name__ == "__main__":
    app.run()
