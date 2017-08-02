
from datetime import datetime
import time

class Check(object):
    """A base class for all checks"""
    def __init__(self,servicename):
        super(Check, self).__init__()
        self.servicename = servicename
    def run_check(self,*args,**kwargs):
        result = {'name':self.servicename,'checktype':self.__class__.__name__,'result':'OK','timestamp':self.get_current_epoch_millis()}
        return result
        

    def get_current_epoch_millis(self):
        now = datetime.now()
        # stupid way to get the epoch time in milliseconds but than it is bigger than an int
        timestamp = str(time.mktime(now.timetuple()))[:-2] + str(int(now.microsecond * 1e-3))
        return timestamp