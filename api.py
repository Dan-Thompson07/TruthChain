from flask import request, jsonify, Flask
import requests
from model import manual_testing
from keys import Keys

url = "https://uploads.pinata.cloud/v3/files"
app = Flask(__name__)
news = input("Enter a news article:\n")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if data:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {Keys.JWT}",
        }
        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            ipfs_hash = response.json()
            return jsonify({"ipfs_hash": ipfs_hash})
        else:
            raise Exception(f"Upload failed: {response.text}")
        

    if __name__ == '__main__':
        app.run(debug=False, host='0.0.0.0', port=5000)
