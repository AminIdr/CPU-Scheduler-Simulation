from models.process import Process
import random

def generate_processes(num_processes, burst_time_range, arrival_time_range, priority_range=None):
    """
    Generates input data for processes with random attributes.

    Args:
        num_processes (int): Number of processes to generate.
        burst_time_range (tuple): Range for burst times (min, max).
        arrival_time_range (tuple): Range for arrival times (min, max).
        priority_range (tuple, optional): Range for process priorities (min, max). Defaults to None.

    Returns:
        list: List of Process objects representing the generated processes.
    """
    processes = []
    for pid in range(1, num_processes + 1):
        arrival_time = random.randint(arrival_time_range[0], arrival_time_range[1])
        burst_time = random.randint(burst_time_range[0], burst_time_range[1])
        priority = None
        if priority_range:
            priority = random.randint(priority_range[0], priority_range[1])
        processes.append(Process(pid, arrival_time, burst_time, priority))
    return processes
