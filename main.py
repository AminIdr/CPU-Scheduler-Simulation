from flask import Flask, render_template, request, jsonify
from algorithms.fcfs import fcfs
from algorithms.sjf import sjf
from algorithms.priority import priority
from algorithms.rr import round_robin
from algorithms.priority_rr import priority_round_robin
from models.process import Process

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    global processes
    processes = []
    if request.method == 'POST':
        # Retrieve JSON data from the request
        data = request.get_json()

        # Extract the chosen algorithm and list of processes from the data
        algorithm = data.get('algorithm')
        process_data = data.get('processes', [])
        print(data)
        if algorithm == 'rr' or algorithm == 'priority_rr':
            quantum = int(data.get('quantum'))
            print(quantum)

        # Create Process instances for each received process data
        for process_info in process_data:
            process = Process(int(process_info['pid']), int(process_info['arrival_time']), int(process_info['burst_time']))
            if 'priority' in process_info:
                process.priority = int(process_info['priority'])
            processes.append(process)
        
        # Log the received algorithm and processes (for testing purposes)
        print("Received algorithm:", algorithm)
        print("Received processes:", processes)

        scheduler = []
        if algorithm == 'fcfs':
            scheduler = fcfs(processes)
        elif algorithm == 'sjf':
            scheduler = sjf(processes)
        elif algorithm == 'priority':
            scheduler = priority(processes)
        elif algorithm == 'rr':
            scheduler = round_robin(processes, quantum)
        elif algorithm == 'priority_rr':
            scheduler = priority_round_robin(processes, quantum)
        else: 
            return "There was an error receiving the algorithm type from the client."

        for process in scheduler:
            print(process)
            print("###########")
        # Return a success response
        return "Data received successfully.", 200

    return render_template('index.html', algorithm='fcfs', processes=processes)

if __name__ == "__main__":
    app.run(debug=True)
