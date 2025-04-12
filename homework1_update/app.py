from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

applications = {}  # Store applications in memory
application_counter = 1  # Unique application ID counter

statuses = ["not found", "received", "processing", "accepted", "rejected"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apply', methods=['POST'])
def apply():
    global application_counter
    data = request.json
    app_id = application_counter
    applications[app_id] = {"name": data["name"], "zipcode": data["zipcode"], "status": "received"}
    application_counter += 1
    return jsonify({"application_id": app_id})

@app.route('/status/<int:app_id>', methods=['GET'])
def check_status(app_id):
    if app_id in applications:
        return jsonify({"status": applications[app_id]["status"]})
    return jsonify({"status": "not found"})

@app.route('/update_status', methods=['POST'])
def update_status():
    data = request.json
    app_id = data["application_id"]
    new_status = data["status"]

    if app_id in applications and new_status in statuses:
        applications[app_id]["status"] = new_status
        return jsonify({"message": "Status updated successfully"})
    return jsonify({"message": "Invalid application ID or status"}), 400

if __name__ == '__main__':
    app.run(debug=True)
