from flask import Flask, render_template, request
from algorithms.fcfs import fcfs
from algorithms.sjf import sjf
from algorithms.priority import priority
from algorithms.rr import round_robin
from algorithms.priority_rr import priority_round_robin
from models.process import Process
app = Flask(__name__)

# Dummy list to hold processes
processes = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global processes
    p1 = Process(1, 0, 12)
    p2 = Process(2, 5, 19)
    p3 = Process(3, 8, 21)
    p4 = Process(4, 11, 13)
    p5 = Process(5, 15, 15)

    processes = [p1, p2, p3, p4, p5]
    # if request.method == 'POST':
    #     # Check if the form data is empty (indicating a page refresh)
    #     if all(value == '' for value in request.form.values()):

    #         print("Here")
    #         processes = []  # Reset the processes list to an empty list
    #     else:
    #         print(request.form)
    #         print("Here 2")
    #         # Get form data
    #         algorithm = request.form['algorithm']
    #         new_process_id = int(request.form['newProcessID'])
    #         new_arrival_time = int(request.form['newArrivalTime'])
    #         new_burst_time = int(request.form['newBurstTime'])
    #         new_priority = int(request.form.get('newPriority', 0))  # Priority is optional

    #         # Append new process to the list
    #         processes.append({'id': new_process_id, 'arrival_time': new_arrival_time, 'burst_time': new_burst_time, 'priority': new_priority})

    #     # Render the entire page with the updated process table
    #     return render_template('index.html', algorithm=algorithm, processes=processes)

    return render_template('index.html', algorithm='fcfs', processes=processes)

if __name__ == "__main__":
    app.run(debug=True)
