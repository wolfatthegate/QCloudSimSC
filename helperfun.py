import math
from QJob import QJob
import random
import numpy as np

from geneva_noise_index_0 import geneva_noise_index_0 # To be deleted. Don't use
from hanoi_noise_index_0 import hanoi_noise_index_0 # To be deleted. Don't use

INTERVAL = 10

### IMPORT NOISE DATA
geneva_noise = np.genfromtxt('PST/geneva_PST.csv')
hanoi_noise = np.genfromtxt('PST/hanoi_PST.csv')
montreal_noise = np.genfromtxt('PST/montreal_PST.csv')
mumbai_noise = np.genfromtxt('PST/mumbai_PST.csv')
toronto_noise = np.genfromtxt('PST/toronto_PST.csv')

def estimate_time(qjob: QJob, device_name: str, CLOPS: int) -> float:
    
    """ A simple rather a dummy model to estimate the run time of a quantum job. 
        An accurate model to be replaced. Coefficient can be adjusted based on 
        the caliberation of the machine setup. 
    
        Source: Scholten, Travis et al. A Model for Circuit Execution Runtime 
        And Its Implications for Quantum Kernels At Practical Data Set Sizes. 
        https://arxiv.org/pdf/2307.04980.pdf
        
     """
    
    ALPHA_1 = 0.02 # some scaling parameter
    
    M = 100 # parameterized quantum volume circuits
    K = 10 # time parameters of each circuit are updated
    S = qjob.num_of_shots # typically 100 shots
    V = qjob.V # quantum volume
    D = math.log2(V) 
     
    T = M*D*K*S/(CLOPS) * ALPHA_1
    
    return T


""" implement a model for incoming job interval """

def incoming_job_interval(): 
    """ return interval between incoming jobs. 
    """
    
    return random.expovariate(1/INTERVAL)


""" estimate success probability """

def estimate_success_probability(num_of_circuits: int, device_name: str) -> float: 
    # default random integer within a range 
    # or implement your own model 
    
    if device_name == 'geneva': 
        return geneva_noise[num_of_circuits] if geneva_noise[num_of_circuits] is not None else 0.0
    if device_name == 'hanoi': 
        return hanoi_noise[num_of_circuits] if hanoi_noise[num_of_circuits] is not None else 0.0
    if device_name == 'montreal':
        return montreal_noise[num_of_circuits] if montreal_noise[num_of_circuits] is not None else 0.0
    if device_name == 'mumbai':     
        return mumbai_noise[num_of_circuits] if num_of_circuits < 2750 else 0.0
    if device_name == 'toronto': 
        return toronto_noise[num_of_circuits] if toronto_noise[num_of_circuits] is not None else 0.0
    
    return 0.0


def printLog(message: str, PrintLog: bool): 
    if PrintLog: 
        print(message)