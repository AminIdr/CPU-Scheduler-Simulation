# Assuming lower numbers represent higher priority
# Non-preemptive
# Note: Once two processes with the same priority are in the ready queue, it doesn't matter which one arrived first
# However, in our implementation we choose the first arrived one
def priority(processes):
    """
    Simulates Priority Scheduling algorithm.

    Args:
        processes (list): List of Process objects.

    Returns:
        list: List of tuples containing Process objects, turnaround times, and waiting times.
        float: Average turnaround time.
        float: Average waiting time.
        float: CPU utilization.
    """
    # Initialize scheduler and current time
    details = []
    scheduler = []
    current_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0
    total_cpu_time = 0

    # Sort processes based on arrival time and priority
    sorted_processes = sorted(processes, key=lambda x: (x.arrival_time, x.priority))

    # Initialize ready queue
    ready_queue = []

    while sorted_processes or ready_queue:
        # Add arriving processes to the ready queue
        while sorted_processes and sorted_processes[0].arrival_time <= current_time:
            ready_queue.append(sorted_processes.pop(0))

        if ready_queue:
            # Sort ready queue based on priority
            ready_queue.sort(key=lambda x: x.priority)

            # Select the process with highest priority
            selected_process = ready_queue.pop(0)

            details.append([selected_process.pid,current_time, current_time + selected_process.burst_time])
            # Update current time
            current_time += selected_process.burst_time

            # Record process completion time
            selected_process.completion_time = current_time

            # Calculate turnaround time and waiting time
            turnaround_time = selected_process.completion_time - selected_process.arrival_time
            waiting_time = turnaround_time - selected_process.burst_time

            # Update total turnaround time and total waiting time
            total_turnaround_time += turnaround_time
            total_waiting_time += waiting_time

            # Add process to scheduler
            scheduler.append((selected_process, turnaround_time, waiting_time))
            
            # Update CPU utilization time
            total_cpu_time += selected_process.burst_time
        else:
            # If no process is ready, wait until next arrival
            current_time = sorted_processes[0].arrival_time

    # Calculate average turnaround time, average waiting time, and CPU utilization
    num_processes = len(processes)
    avg_turnaround_time = total_turnaround_time / num_processes
    avg_waiting_time = total_waiting_time / num_processes
    cpu_utilization = (total_turnaround_time - total_waiting_time) / current_time * 100

    return scheduler, details, avg_turnaround_time, avg_waiting_time, cpu_utilization
