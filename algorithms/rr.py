from queue import Queue

def rr(processes, quantum):
    """
    Simulates Round Robin (RR) scheduling algorithm using a simple queue.

    Args:
        processes (list): List of Process objects.
        quantum (int): Time quantum for each process.

    Returns:
        list: List of Process objects representing the order in which processes are scheduled.
    """
    # Initialize scheduler and current time
    scheduler = []
    quantum_details = []
    current_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0
    total_cpu_time = 0


    # Create a queue for ready queue
    ready_queue = Queue()

    # Sort processes based on arrival time
    sorted_processes = sorted(processes, key=lambda x: x.arrival_time)

    # Initialize index to track next process to arrive
    next_process_index = 0
    original_burst_times = {process.pid:process.burst_time for process in sorted_processes}

    # Loop until all processes are completed
    while not ready_queue.empty() or next_process_index < len(sorted_processes):
        # Add arriving processes to the ready queue
        while next_process_index < len(sorted_processes) and sorted_processes[next_process_index].arrival_time <= current_time:
            ready_queue.put(sorted_processes[next_process_index])
            next_process_index += 1

        # Execute process from the front of the queue
        if not ready_queue.empty():
            current_process = ready_queue.get()

            # Check if a new process arrives during execution
            while next_process_index < len(sorted_processes) and sorted_processes[next_process_index].arrival_time <= current_time + quantum:
                ready_queue.put(sorted_processes[next_process_index])
                next_process_index += 1

            # Update current time based on burst time or remaining time quantum
            execution_time = min(quantum, current_process.burst_time)
            current_time += execution_time

            # Subtract burst time from process burst time
            current_process.burst_time -= execution_time

            # Record process completion time if completed
            if current_process.burst_time <= 0:
                current_process.completion_time = current_time
                turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.burst_time = original_burst_times[current_process.pid]
                waiting_time = turnaround_time - current_process.burst_time
                # Update total turnaround time and total waiting time
                total_turnaround_time += turnaround_time
                total_waiting_time += waiting_time
                # Add process to scheduler
                scheduler.append((current_process, turnaround_time, waiting_time))

            # Add process back to ready queue if burst time remains
            else:
                ready_queue.put(current_process)

            # Add process to scheduler
            quantum_details.append([current_process.pid,current_time - execution_time,current_time])

        # If no process is ready, wait until next arrival
        else:
            current_time = sorted_processes[next_process_index].arrival_time
        
    # Calculate average turnaround time, average waiting time, and CPU utilization
    num_processes = len(processes)
    avg_turnaround_time = total_turnaround_time / num_processes
    avg_waiting_time = total_waiting_time / num_processes
    cpu_utilization = (total_turnaround_time - total_waiting_time) / current_time * 100
    

    return scheduler,quantum_details,avg_turnaround_time, avg_waiting_time, cpu_utilization