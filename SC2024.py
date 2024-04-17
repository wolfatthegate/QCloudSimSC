import socket
import simpy
import numpy as np
import matplotlib.pyplot as plt
import time
import random
from QJob import QJob
from QCloud import QCloud
from Broker import Broker
from JobLogger import JobLogger
from helperfun import *
from helperfun import INTERVAL
from datetime import datetime

def setup(env, num_machines, joblogger, JOB_LIMIT, PrintLog):
    """Setup initializes a quantum cloud, a broker and job generator generating 
    jobs in approx. every INTERVAL minutes."""
    
    # initialize a quantum cloud
    qcloud = QCloud(env, num_machines)
    
    # initialize a broker
    # set prioritize = True for priority scheduling
    # False for FIFO scheduling
    
    broker = Broker(env = env, prioritize = False)
    
    # Create jobs while the simulation is running
    i = 0
    while i < JOB_LIMIT:
        yield env.timeout(incoming_job_interval())
        i += 1
        qjob = QJob(env, i)
        env.process(broker.schedule(qcloud, qjob, joblogger, PrintLog))   

machine_name = socket.gethostname()
PrintLog = False # Detail Logs
NUM_OF_MACHINE = 5
JOB_LIMIT = 500
MESSAGE = ''
# Preparing data structures for simulation results

data = {key: [] for key in range(1, NUM_OF_MACHINE+1)}
sim_time_taken = {key: [] for key in range(1, NUM_OF_MACHINE+1)}

# Setup and start the simulation

print(f'Machine Name: {machine_name}')
print(f'Number of fixed jobs: {JOB_LIMIT}')
print(f'Simulation Started at {datetime.now()}')
MESSAGE += f'Machine Name: {machine_name}'
MESSAGE += f'Number of fixed jobs: {JOB_LIMIT}\n'
MESSAGE += f'Simulation Started at {datetime.now()}\n'

sim_start_time = time.time()
for j in range(10): 
    for NUM_MAC in range(1, NUM_OF_MACHINE+1): 
        RANDOM_SEED = random.randint(2, 10000)
        random.seed(RANDOM_SEED)  # This helps to reproduce the results

        joblogger = JobLogger()

        # Create an environment and start the setup process
        env = simpy.Environment()
        env.process(setup(env, NUM_MAC, joblogger, JOB_LIMIT, PrintLog))

        # Execute!
        env.run()
        data[NUM_MAC].append(joblogger.wait_time)
        sim_time_taken[NUM_MAC].append(np.round(env.now, 2))

print(f'Simulation Ended at {datetime.now()}')
MESSAGE += f'Simulation Ended at {datetime.now()}\n'

sim_end_time = time.time()
print(f'Elasped time - {sim_end_time-sim_start_time:.5f} seconds ')
MESSAGE += f'Elasped time - {sim_end_time-sim_start_time:.5f} seconds \n'

avg_sim_time_taken = []
std_sim_time_taken = []

for k in sim_time_taken.keys(): 
    avg_sim_time_taken.append(np.round(np.average(sim_time_taken[k]), 2))
    std_sim_time_taken.append(np.round(np.std(sim_time_taken[k]), 2))
    
print(f'sim time taken: {sim_time_taken}')
print(f'average time taken: {avg_sim_time_taken}')
print(f'standard deviation: {std_sim_time_taken}')
print('Simulation completed ===>')

MESSAGE += f'sim time taken: {sim_time_taken}\n'
MESSAGE += f'average time taken: {avg_sim_time_taken}\n'
MESSAGE += f'standard deviation: {std_sim_time_taken}\n'
MESSAGE += 'Simulation completed ===>\n\n'

filename = 'fixed_jobs_sim_data.txt'
with open(filename, 'a') as file:
    file.write(MESSAGE)
