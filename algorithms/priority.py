# Assuming lower numbers represent higher priority
# Non-preemptive
# Note: Once two processes with the same priority are in the ready queue, it doesn't matter which one arrived first
# However, in our implementation we choose the first arrived one
def priority_scheduling(processes):
    """
    Simulates Priority Scheduling algorithm.

    Args:
        processes (list): List of Process objects.

    Returns:
        list: List of Process objects representing the order in which processes are scheduled.
    """
    # Initialize scheduler and current time
    scheduler = []
    current_time = 0

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

            # Update current time
            current_time += selected_process.burst_time

            # Record process completion time
            selected_process.completion_time = current_time

            # Add process to scheduler
            scheduler.append(selected_process)
        else:
            # If no process is ready, wait until next arrival
            current_time = sorted_processes[0].arrival_time

    return scheduler
