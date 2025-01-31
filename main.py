from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# Read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)

@app.route('/')
def hello_world():
    return 'Hello, World!'  # Return 'Hello World' in response

@app.route('/students')
def get_students():
    result = []
    pref = request.args.get('pref')  # Get the parameter from URL
    if pref:
        for student in data:  # Iterate dataset
            if student['pref'] == pref:  # Select only the students with a given meal preference
                result.append(student)  # Add matching student to the result
        return jsonify(result)  # Return filtered set if parameter is supplied
    return jsonify(data)  # Return entire dataset if no parameter supplied

@app.route('/students/<id>')
def get_student(id):
    for student in data:
        if student['id'] == id:  # Filter out the students without the specified ID
            return jsonify(student)

@app.route('/stats')
def get_stats():
    stats = {}

    for student in data:
        meal = student.get('pref', 'Unknown')
        program = student.get('programme', 'Unknown')  # Ensure this is the correct field

        # Count meal preferences
        stats[meal] = stats.get(meal, 0) + 1

        # Count study programs
        stats[program] = stats.get(program, 0) + 1

    return jsonify(stats)

# Arithmetic operation routes
@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return jsonify({'operation': 'addition', 'result': a + b})

@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    return jsonify({'operation': 'subtraction', 'result': a - b})

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    return jsonify({'operation': 'multiplication', 'result': a * b})

@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    return jsonify({'operation': 'division', 'result': a / b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

