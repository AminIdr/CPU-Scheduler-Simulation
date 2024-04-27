from flask import Flask, render_template, request
from algorithms.fcfs import fcfs
from algorithms.sjf import sjf
from algorithms.priority import priority
from algorithms.rr import round_robin
from algorithms.priority_rr import priority_round_robin

app = Flask(__name__)

# Dummy list to hold processes
processes = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global processes

    if request.method == 'POST':
        # Check if the form data is empty (indicating a page refresh)
        if all(value == '' for value in request.form.values()):
            processes = []  # Reset the processes list to an empty list

        # Get form data
        algorithm = request.form['algorithm']
        new_process_id = int(request.form['newProcessID'])
        new_arrival_time = int(request.form['newArrivalTime'])
        new_burst_time = int(request.form['newBurstTime'])

        if algorithm == "rr" or algorithm == "priority_rr":
            new_quantum = int(request.form['quantum'])
        else:
            new_quantum = 0

        if algorithm == "priority" or algorithm == "priority_rr":
            new_priority = int(request.form['newPriority'])
        else:
            new_priority = None
            
        # Append new process to the list
        processes.append({'pid': new_process_id, 'arrival_time': new_arrival_time, 'burst_time': new_burst_time, 'priority': new_priority})

        # Render the entire page with the updated process table
        return render_template('index.html', algorithm=algorithm, processes=processes, quantum=new_quantum)

    return render_template('index.html', algorithm='fcfs', processes=processes)

if __name__ == "__main__":
    app.run(debug=True)
