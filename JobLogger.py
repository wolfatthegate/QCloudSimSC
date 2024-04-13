class JobLogger(object): 
    """
    Job Logger is to keep track of the life cycle of QJobs
    such as wait_time, number of job completed, etc. 

    """
    def __init__(self): 
        self.num_of_completed_jobs = 0
        self.wait_time = []