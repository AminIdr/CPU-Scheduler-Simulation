from flask import Flask, render_template, request
import json
from models.process import Process

app = Flask(__name__)

# Dummy list to hold processes

@app.route('/', methods=['GET', 'POST'])
def index():
    global processes
    processes = []

    if request.method == 'POST':
        # Retrieve JSON data from the request
        process_data = request.get_json()

        # Create Process instances for each received process data
        for data in process_data:
            process = Process(data['pid'], data['arrival_time'], data['burst_time'])
            if 'priority' in data:
                process.priority = data['priority']
            processes.append(process)

        # Log the received processes (for testing purposes)
        print("Received processes:", processes)

        # Process the received data further as needed
        
        # Return a success response
        return "Processes received successfully.", 200

    return render_template('index.html', algorithm='fcfs', processes=processes)

if __name__ == "__main__":
    app.run(debug=True)
