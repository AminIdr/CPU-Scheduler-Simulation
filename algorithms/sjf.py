def sjf(processes):
    """
    Simulates Shortest Job First (SJF) scheduling algorithm.

    Args:
        processes (list): List of Process objects.

    Returns:
        list: List of tuples containing Process objects, turnaround times, and waiting times.
        list: List of lists containing scheduling details (pid, start time, end time).
        float: Average turnaround time.
        float: Average waiting time.
        float: CPU utilization.
    """
    # Initialize scheduler and current time
    details = []  # Store details of each process execution (pid, start time, end time)
    scheduler = []  # Store scheduling information (process, turnaround time, waiting time)
    current_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0
    total_cpu_time = 0

    # Sort processes based on arrival time
    sorted_processes = sorted(processes, key=lambda x: x.arrival_time)

    # Initialize ready queue
    ready_queue = []

    while sorted_processes or ready_queue:
        # Add arriving processes to the ready queue
        while sorted_processes and sorted_processes[0].arrival_time <= current_time:
            ready_queue.append(sorted_processes.pop(0))

        if ready_queue:
            # Sort ready queue based on burst time
            ready_queue.sort(key=lambda x: x.burst_time)

            # Select the shortest job
            shortest_job = ready_queue.pop(0)
            details.append([shortest_job.pid, current_time, current_time + shortest_job.burst_time])

            # Update current time
            current_time += shortest_job.burst_time

            # Record process completion time
            shortest_job.completion_time = current_time

            # Calculate turnaround time and waiting time
            turnaround_time = shortest_job.completion_time - shortest_job.arrival_time
            waiting_time = turnaround_time - shortest_job.burst_time

            # Update total turnaround time and total waiting time
            total_turnaround_time += turnaround_time
            total_waiting_time += waiting_time

            # Add process to scheduler
            scheduler.append((shortest_job, turnaround_time, waiting_time))
            
            # Update CPU utilization time
            total_cpu_time += shortest_job.burst_time
        else:
            # If no process is ready, wait until next arrival
            current_time = sorted_processes[0].arrival_time

    # Calculate average turnaround time, average waiting time, and CPU utilization
    num_processes = len(processes)
    avg_turnaround_time = total_turnaround_time / num_processes
    avg_waiting_time = total_waiting_time / num_processes
    cpu_utilization = (total_turnaround_time - total_waiting_time) / current_time * 100

    return scheduler, details, avg_turnaround_time, avg_waiting_time, cpu_utilization
