from helperfun import *

class Broker(object):
    """ 
    Broker is responsible for assigning quantum jobs (qjobs) to an appropriate qdevice. 
    The goal of a broker is to utilize available quantum devices at QCloud. 
    
    """
    def __init__(self, env, prioritize):
        self.env = env
        self.prioritize = prioritize
        
    def schedule(self, qcloud, qjob, joblogger, PrintLog): 
        
        """
        Schedule layer is where all the qjobs arrive. Broker keeps qjobs in the central queue. 
        By default, broker provides a simple FIFO scheduling algorithm. The users can implement 
        their own scheduling algorithm. 
        
        """
        printLog(f'Sim time {self.env.now:.2f}: {qjob._id} arrives at the central queue.', PrintLog = False)
        arrival_time = self.env.now
        
        if not self.prioritize: 
            qjob.priority = 2
        
        ### scheduling policies
        rotate = False

        if rotate: 
            ## rotate machine        
            qdevID = qjob._id%qcloud.num_qdevices
        else: 
            ## get a random machine
            qdevID = random.randint(0, qcloud.num_qdevices-1)       
        
        ### assign the job to a specific device
        with qcloud.qdevicesList[qdevID].request(priority = qjob.priority) as request:
            yield request
            
            wait_time = self.env.now - arrival_time
            joblogger.wait_time.append(wait_time)
            device_name = qcloud.qdevicesName[qdevID]   
            
            printLog(f'Sim time {self.env.now:.2f}: Qjob {qjob._id} is assigned to {device_name} with priority {qjob.priority}.', PrintLog = False)
            yield self.env.process(qcloud.execute(qjob, qdevID))
            
            joblogger.num_of_completed_jobs += 1
            
            life_time = qcloud.life_time[device_name]
            
            printLog(f'Sim time {self.env.now:.2f}: Life time of {device_name} is {life_time:.2f}.', PrintLog)
            
            if life_time < 0: 
                printLog(f'Sim time {self.env.now:.2f}: Life time of {device_name} is {life_time:.2f}.', PrintLog)
                printLog(f'Sim time {self.env.now:.2f}: Maintenance needed for {device_name}.', PrintLog)
                yield self.env.timeout(900) # maintenance time 
                qcloud.life_time[device_name] = qcloud.ori_life_time[device_name]
                printLog(f'Sim time {self.env.now:.2f}: Maintenance finished for {device_name}.', PrintLog)