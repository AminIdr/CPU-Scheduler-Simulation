from utils.generator import generate_processes
from algorithms.fcfs import fcfs
from algorithms.sjf import sjf
from algorithms.priority import priority_scheduling
from algorithms.round_robin import round_robin
from algorithms.priority_rr import priority_round_robin
from models.process import Process
# Generate random input data (processes)
# num_processes = 5
# num_priorities = (1, 3)
# burst_time_range = (3, 10)
# arrival_time_range = (0, 8)
# processes = generate_processes(num_processes, burst_time_range, arrival_time_range)

# for process in processes:
#     print(process)

# print("#####################")
# # Apply Priority scheduling algorithm
# scheduled_processes, curr_time = round_robin(processes, 1)

# # Display scheduled processes
# print("Scheduled Processes (Round Robin Scheduling):")
# for i in range(len(scheduled_processes)):
#     print(scheduled_processes[i], curr_time[i])


# print("#####################")
# # Apply SJF scheduling algorithm
# scheduled_processes = sjf(processes)

# # Display scheduled processes
# print("Scheduled Processes (SJF):")
# for process in scheduled_processes:
#     print(process)

p1 = Process(1, 7, 8, 1)
p2 = Process(2, 0, 9, 2)
p3 = Process(3, 2, 5, 2)
p4 = Process(4, 8, 9, 1)
p5 = Process(5, 7, 5, 4)

processes = [p1, p2, p3, p4, p5]
# Apply Priority scheduling algorithm
# scheduled_processes, curr_time = round_robin(processes, 3)

# # Display scheduled processes
# print("Scheduled Processes (Round Robin Scheduling):")
# for i in range(len(scheduled_processes)):
#     print(scheduled_processes[i], curr_time[i])

# Apply SJF scheduling algorithm
scheduled_processes = priority_round_robin(processes, 2)
for process in scheduled_processes:
    print(process)