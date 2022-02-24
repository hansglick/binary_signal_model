import numpy as np
import seaborn as sb

class SignalsStory:

    """
    Class Object SignalsStory is able to reconstruct the hierarchical story behind binary events
    """
    
    def __init__(self,data=None):
        
        """
        data : A numpy array that contains events in unix epoch format
        """

        if data is not None:
            self.DATA = np.sort(data)
            self.FIRST = data[0]
            self.LAST = data[-1]
            self.N = len(data)
            self.AMPLITUDE = max(data) - min(data)
        
        
    def __str__(self):

        if hasattr(self, 'DATA'):
            a = "Events : " + str(self.N)
            b = "First : " + str(self.FIRST)
            c = "Last : " + str(self.LAST)
            d = "Amplitude : " + str(self.AMPLITUDE)
            to_be_printed = a + "\n" + b + "\n" + c + "\n" +  d
        else:
        	to_be_printed = "No loaded events, please use Load_Data() or Generate_Data() methods"

        return to_be_printed