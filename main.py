from utils.generator import generate_processes
from algorithms.fcfs import fcfs
from algorithms.sjf import sjf
from algorithms.priority import priority_scheduling
from algorithms.round_robin import round_robin
from algorithms.priority_rr import priority_round_robin
from models.process import Process
# Generate random input data (processes)
# num_processes = 5
# num_priorities = (1, 6)
# burst_time_range = (3, 10)
# arrival_time_range = (0, 8)
# processes = generate_processes(num_processes, burst_time_range, arrival_time_range, num_priorities)

# for process in processes:
#     print(process)

print("#####################")
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

p1 = Process(1, 0, 12, 3)
p2 = Process(2, 5, 19, 3)
p3 = Process(3, 8, 21, 5)
p4 = Process(4, 11, 13, 2)
p5 = Process(5, 15, 15, 3)

processes = [p1, p2, p3, p4, p5]
# Apply Priority scheduling algorithm
scheduled_processes, curr_time = priority_round_robin(processes, 4)

# # Display scheduled processes
print("Scheduled Processes (Round Robin Scheduling):")
for i in range(len(scheduled_processes)):
    print(scheduled_processes[i], curr_time[i])



# p1 = Process(1, 6, 10, 2)
# p2 = Process(2, 4, 3, 4)
# p3 = Process(3, 3, 3, 1)
# p4 = Process(4, 2, 6, 2)
# p5 = Process(5, 5, 4, 2)
# processes = [p1, p2, p3, p4, p5]
# scheduled_processes = priority_preemptive(processes)
# for process in scheduled_processes:
#     print(process)  
# scheduled_processes, curr_time = priority_round_robin(processes, 2)
# for i in range(len(scheduled_processes)):
#     # print("het")
#     print(scheduled_processes[i], curr_time[i])