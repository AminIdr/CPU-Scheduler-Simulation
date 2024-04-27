def sjf(processes):
    """
    Simulates Shortest Job First (SJF) scheduling algorithm.

    Args:
        processes (list): List of Process objects.

    Returns:
        list: List of Process objects representing the order in which processes are scheduled.
    """
    # Initialize scheduler and current time
    scheduler = []
    current_time = 0

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

            # Update current time
            current_time += shortest_job.burst_time

            # Record process completion time
            shortest_job.completion_time = current_time

            # Add process to scheduler
            scheduler.append(shortest_job)
        else:
            # If no process is ready, wait until next arrival
            current_time = sorted_processes[0].arrival_time

    return scheduler
