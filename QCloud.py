import simpy
import random
from helperfun import *

class QCloud(object):

    """
    A quantum cloud or a QCloud has a number of unique devices. Each device has certain properties. 
    QCloud has only one property that is to execute the qjob (or quantum job) that the broker 
    assigns to a certain device. 

    """
    
    def __init__(self, env, num_qdevices):
        """ simulation environment (env) and quantum devices (simpy.PriorityResource)
            are declared at initialization. 
        
        """
        self.env = env
        self.num_qdevices = num_qdevices
        
        self.geneva = simpy.PriorityResource(env=env, capacity=1)
        self.hanoi = simpy.PriorityResource(env=env, capacity=1)
        self.montreal = simpy.PriorityResource(env=env, capacity=1)
        self.mumbai = simpy.PriorityResource(env=env, capacity=1)
        self.toronto = simpy.PriorityResource(env=env, capacity=1)
        
        self.qdevicesList = [self.geneva, self.hanoi, self.montreal, self.mumbai, self.toronto]
        self.qdevicesName = ['geneva', 'hanoi', 'montreal', 'mumbai', 'toronto']
        
        """IBM does not provide specific CLOPS. While IBM does provide various metrics 
           and specifications for their quantum devices, CLOPS is not typically one of them. """
        
        self.CLOPS = {'geneva': random.randint(4000, 5000), 
                      'hanoi': random.randint(4800, 5000), 
                      'montreal': random.randint(4600, 4900), 
                      'mumbai': random.randint(4200, 4800), 
                      'toronto': random.randint(4100, 4800)}
        
        self.life_time = {'geneva': 4000, 
                              'hanoi': 1500, 
                              'montreal': 4500, 
                              'mumbai': 6000, 
                              'toronto': 2000}
        
        self.ori_life_time = {'geneva': 4000, 
                              'hanoi': 1500, 
                              'montreal': 4500, 
                              'mumbai': 6000, 
                              'toronto': 2000}
        
    def execute(self, qjob, qdevID):
        """ execute function take a quantum job (qjob) and process. """
        device_name = self.qdevicesName[qdevID]
        CLOPS = self.CLOPS[device_name] 
        est_time = estimate_time(qjob, self.qdevicesName[qdevID], CLOPS)
        
        printLog(f'Sim time {self.env.now:.2f}: Qjob {qjob._id}\'s estimate time is {est_time:.2f}.', PrintLog = False)
        yield self.env.timeout(est_time)
        
        prob_meas0_prep1 = estimate_success_probability(qjob.num_of_circuit, device_name)

        printLog(f'Sim time {self.env.now:.2f}: Qjob {qjob._id} with {qjob.num_of_qubits} qubits processed with {prob_meas0_prep1 * 100:.2f}% of PST.', PrintLog = False)
        printLog(f'Sim time {self.env.now:.2f}: Qjob {qjob._id} left {device_name}.', PrintLog = False)  
        
        self.life_time[device_name] -= est_time # replace this with shots