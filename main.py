from flask import Flask, render_template, request, jsonify
from algorithms.fcfs import fcfs
from algorithms.sjf import sjf
from algorithms.priority import priority
from algorithms.priority_preemptive import priority_preemptive
from algorithms.rr import rr
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
        if algorithm == 'rr' or algorithm == 'priority_rr':
            quantum = int(data.get('quantum'))

        # Create Process instances for each received process data
        for process_info in process_data:
            process = Process(int(process_info['pid']), int(process_info['arrival_time']), int(process_info['burst_time']))
            if 'priority' in process_info:
                process.priority = int(process_info['priority'])
            processes.append(process)
        
        scheduler = []
        avg_turnaround_time = 0
        avg_waiting_time = 0
        cpu_utilization = 0
        if algorithm == 'fcfs':
            scheduler, avg_turnaround_time, avg_waiting_time, cpu_utilization = fcfs(processes)
        elif algorithm == 'sjf':
            scheduler, avg_turnaround_time, avg_waiting_time, cpu_utilization = sjf(processes)
        elif algorithm == 'priority':
            scheduler, avg_turnaround_time, avg_waiting_time, cpu_utilization = priority(processes)
        elif algorithm == 'priority_p':
            scheduler, _, avg_turnaround_time, avg_waiting_time, cpu_utilization = priority_preemptive(processes)
        elif algorithm == 'rr':
            scheduler, a, avg_turnaround_time, avg_waiting_time, cpu_utilization = rr(processes, quantum)
            print(a)
        elif algorithm == 'priority_rr':
            scheduler, _, avg_turnaround_time, avg_waiting_time, cpu_utilization = priority_round_robin(processes, quantum)
        else: 
            return "There was an error receiving the algorithm type from the client."

        # Create a list of tuples containing scheduler results
        scheduler_results = [(process.pid, process.completion_time, turnaround_time, waiting_time) for process, turnaround_time, waiting_time in scheduler]
        # scheduler_results_json = [(process.pid, turnaround_time, waiting_time) for process, turnaround_time, waiting_time in scheduler_results]
        print(scheduler_results)
        # print(scheduler_results_json)
        # Return the scheduler results as JSON data
        return jsonify({
            'schedulerResults': scheduler_results,
            'avgTurnaroundTime': avg_turnaround_time,
            'avgWaitingTime': avg_waiting_time,
            'cpuUtilization': cpu_utilization
        }), 200

    return render_template('index.html', algorithm='fcfs', processes=processes)

if __name__ == "__main__":
    app.run(debug=True)
