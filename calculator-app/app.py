from flask import Flask, render_template, request, jsonify
from datetime import datetime
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    filename='calculator_history.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/log', methods=['POST'])
def log_calculation():

    data = request.get_json()

    expression = data.get('expression')
    result = data.get('result')

    logging.info(f"Calculation: {expression} = {result}")

    return jsonify({"message": "History saved successfully"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)