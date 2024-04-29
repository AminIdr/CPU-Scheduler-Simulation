def fcfs(processes):
    """
    Simulates First-Come, First-Served (FCFS) scheduling algorithm.

    Args:
        processes (list): List of Process objects.

    Returns:
        list: List of tuples containing Process objects, turnaround times, and waiting times.
        float: Average turnaround time.
        float: Average waiting time.
        float: CPU utilization.
    """
    # Sort processes based on arrival time
    sorted_processes = sorted(processes, key=lambda x: x.arrival_time)

    # Initialize scheduler and current time
    details = []
    scheduler = []
    current_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0
    total_cpu_time = 0

    # Schedule processes in order of arrival
    for process in sorted_processes:
        # If process arrives after current time, wait until it arrives
        if process.arrival_time > current_time:
            total_cpu_time += process.arrival_time - current_time
            current_time = process.arrival_time
        else:
            total_cpu_time += 0  # No idle CPU time

        details.append([process.pid,current_time, current_time + process.burst_time])

        # Update current time to finish time of this process
        current_time += process.burst_time
        # Record process completion time
        process.completion_time = current_time
        # Calculate turnaround time and waiting time
        turnaround_time = process.completion_time - process.arrival_time
        waiting_time = turnaround_time - process.burst_time
        # Update total turnaround time and total waiting time
        total_turnaround_time += turnaround_time
        total_waiting_time += waiting_time
        # Add process to scheduler
        scheduler.append((process, turnaround_time, waiting_time))

    # Calculate average turnaround time, average waiting time, and CPU utilization
    num_processes = len(processes)
    avg_turnaround_time = total_turnaround_time / num_processes
    avg_waiting_time = total_waiting_time / num_processes
    cpu_utilization = (total_turnaround_time - total_waiting_time) / current_time * 100

    return scheduler,details, avg_turnaround_time, avg_waiting_time, cpu_utilization
