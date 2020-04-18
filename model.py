import numpy
import matplotlib.pyplot as pyplot
import pandas as pd

'''Define dataframe N such that there exists;
"Healthy" - Those that are suseptable and previously unaffected,
"Incubating" - Those that are infected but uncontagious,
"Contagious" - Those that are Contagious,
"Symptomatic"- Those that are Contagious and Sympotmatic,
"Recovered" - Those that are immune,
"Dead"- Those that have died.

The Healthy class is divided into a weak and a strong class. 
	Those in the weak class will progress through the stages but will end dead.
	Those in the strong class will progress through the stages but will end Recovered.

Population parameters:
pop: The population size 
frac_fat: The proportion of the heathy population that will end up dead. Something only god knows. eg ~1 - 3% 
c_0: The initial count of contagious people,
k_s: Some arbitary lockdown parameter for the strong population
k_w: Some arbitary lockdown parameter for the weak population

Disease parameters: (Global)
D_I: The mean time for incubation period of the disease,
D_C: The mean time for contagious period of the disease,
D_S: The mean time for symptomatic period of the disease,
''' 

def CreateDataframes():
	d = {'': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)

def PredictNextDay(Ns, Nw, d, k_s, k_w):
	'''Alters Ns, Nw to model the progession of the disease by one day
		Ns: The strong population dataframe,
		Nw: The weak population dataframe,
		d: The day we have data for,
		k_s: The strong lockdown parameter,
		k_w: The weak lockdown parameter.
	'''
	return 0



if __name__ == '__main__':
	print("Run as test code")
	#Define test variables:
	pop = 1e7
	frac_fat = 0.01
	c_0 = 1
	k_s = 0.1
	k_w = k_s # For now

	d_I = 5
	d_C = 2
	d_S = 7

	
	
