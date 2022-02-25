import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

class SignalsStory:

	"""
	Class Object SignalsStory is able to reconstruct the hierarchical story behind binary events
	"""
	
	def __init__(self,data=None):
		
		"""
		data : A numpy array that contains events in unix epoch format
		"""

		self.Data_Loadder(data)


	def See(self,filter_boolean=False,dims = (16,6)):

		"""
		Plot the events data
		filter_boolean : if True, plot the events data of the DATA_FILTERED attribut
		"""

		if not filter_boolean:
			df = self.Data_To_Dataframe()		
		else:
			df = self.DATA_FILTERED

		plt.figure(figsize=dims)
		sns.scatterplot(x=df.ts,y=df.level,s=100,alpha=0.25)


	def Data_Filter(self,interval):

		"""
		Create a filtered version of DATA attribut
		interval : Either a list of two YYYY-MM-DD HH:MM:SS timestamps format that represent the limits of filtered events
		interval : Either a boolean pandas series that represent the filtered events
		Limits ara within
		"""

		df = self.Data_To_Dataframe()


		if len(interval)>0:
			if isinstance(interval[0], str) and len(interval)==2:
			    print("interval seen as a list of two YYYY-MM-DD HH:MM:SS timestamps format")
			    df["ts_str"] = pd.to_datetime(df.ts,unit="s")
			    start,end = interval
			    filtera = df.ts_str >= start
			    filterb = df.ts_str <= end
			    myfilter = filtera & filterb
			    self.DATA_FILTERED = df[myfilter]
			    print("DATA_FILTERED attribut has been created")

			elif isinstance(interval[0],np.bool_) and len(interval) == len(self.DATA):
			    print("interval seen as a boolean pandas series")
			    self.DATA_FILTERED = df[interval]
			    print("DATA_FILTERED attribut has been created")

			else:
				print("Filter format is not correct, no filtered attribut have been created")
		else:
			print("Filter format is not correct, no filtered attribut have been created")




	def Data_Loadder(self,data):
		
		"""
		data : A numpy array that contains events in unix epoch format
		"""
		

		if data is not None and len(data)>0:
			self.DATA = data
			self.Basic_Processing_Data()
			print(self)
		else:
			print("There is no events")


	def Data_Adder(self,data):
		
		"""
		data : A numpy array that contains events in unix epoch format to be added to the story object data
		"""
		if data is not None and len(data)>0:
			self.DATA = np.append(self.DATA,data)
			self.Basic_Processing_Data()
			print(self)
		else:
			print("There is no added events")
			print(self)


	def Data_Remove(self):
		"""
		Remove the DATA attribut, i.e. lost all events data
		"""
		del self.DATA
		print(self)


	def Data_To_Timestamps(self):

		"""
		Return DATA attribut as a list of pandas datetime fortmat objects
		"""

		return pd.to_datetime(self.DATA,unit="s")


	def Data_To_Dataframe(self):
		
		"""
		Return DATA attribut as a pandas dataframe object
		"""

		df = pd.Series(self.DATA).to_frame().reset_index().rename(columns = {"index":"level",0:"ts"})
		df.level = 0
		return df

	# SPECIAL METHODS * * * # SPECIAL METHODS * * * # SPECIAL METHODS * * * # SPECIAL METHODS * * * 
	# SPECIAL METHODS * * * # SPECIAL METHODS * * * # SPECIAL METHODS * * * # SPECIAL METHODS * * * 
	# SPECIAL METHODS * * * # SPECIAL METHODS * * * # SPECIAL METHODS * * * # SPECIAL METHODS * * * 
	
	def Basic_Processing_Data(self):

		data = self.DATA
		data = np.unique(data)
		self.DATA = data
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
			to_be_printed = a + " | " + b + " | " + c + " | " +  d
		else:
			to_be_printed = "No loaded events, please use Load_Data() or Generate_Data() methods"

		return to_be_printed