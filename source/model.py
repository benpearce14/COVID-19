import numpy as np
import scipy.stats as stats
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
D_I: The 'mean' time for incubation period of the disease,
D_C: The 'mean' time for contagious period of the disease,
D_Ss: The 'mean' time for symptomatic period of the disease for the strong pop,
D_Sw: The 'mean' time for symptomatic period of the disease for the weak pop,

Sig_I: The 'dev' time for incubation period of the disease,
Sig_C: The 'dev' time for contagious period of the disease,
Sig_Ss: The 'dev' time for symptomatic period of the disease for the strong pop,
Sig_Sw: The 'dev' time for symptomatic period of the disease for the weak pop,
'''

D_I = 5.1 #Known
Sig_I= 0.86 #Known
D_C = 1 
Sig_C = 1 
D_Sw = 18.8 #Known
Sig_Sw = 0.45 #Known
D_Ss = 7
Sig_Ss = 1

def CreateDataframes(pop, frac_fat, c_0, days):
	'''Create the required dataframes:
		Ns: The strong population dataframe,
		Nw: The weak population dataframe,
		delta_Ns: The changes in strong population dataframe,
		delta_Nw: The changes in weak population dataframe,
	'''
	days = np.zeros(days)
	ds = {'Healthy': days, 'Incubating': days, 'Contagious': days, 'Symtomatic': days, 'Recovered': days, 'Dead': days }
	dw = {'Healthy': days, 'Incubating': days, 'Contagious': days, 'Symtomatic': days, 'Recovered': days, 'Dead': days }
	Ns = pd.DataFrame(data=ds)
	Nw = pd.DataFrame(data=dw)

	delta_Ns = pd.DataFrame(data=ds)
	delta_Nw = pd.DataFrame(data=dw)

	#Most likely cadidates for infection is the strong population.
	Ns["Healthy"][0] = pop*(1-frac_fat) - c_0
	Ns["Contagious"][0] = c_0

	Nw["Healthy"][0] = pop*frac_fat
	return Ns, Nw, delta_Ns, delta_Nw

def Convolve(delta_N, d, a, scale):
	'''Implement function to smear the time period of individuals in different phases of the disease'''
	tau = 200
	sum=0
	for i in range(tau):
		if d - i >= 0:
			sum += stats.gamma.pdf(i, a=a, scale=scale)*delta_N[d-i]
	return sum


def PredictNextDay(Ns, Nw, delta_Ns, delta_Nw, d, k_s, k_w):
	'''Alters Ns, Nw to model the progession of the disease by one day
		Ns: The strong population dataframe,
		Nw: The weak population dataframe,
		delta_Ns: The changes in strong population dataframe,
		delta_Nw: The changes in weak population dataframe,
		d: The day we have data for,
		k_s: The strong lockdown parameter,
		k_w: The weak lockdown parameter.
	'''
	strong_alive =Ns["Healthy"][d]+Ns["Incubating"][d]+Ns["Contagious"][d]+Ns["Symtomatic"][d]+Ns["Recovered"][d]
	weak_alive =Nw["Healthy"][d]+Nw["Incubating"][d]+Nw["Contagious"][d]+Nw["Symtomatic"][d]+Nw["Recovered"][d]
	pop_alive = strong_alive + weak_alive
	hide_factor = 0.5

	delta_Ns["Incubating"][d] = ( k_s * Ns["Healthy"][d] * ( Ns["Contagious"][d] + Ns["Symtomatic"][d] + hide_factor * (Nw["Contagious"][d] + Nw["Symtomatic"][d])) / pop_alive )
	delta_Nw["Incubating"][d] = ( k_w * Nw["Healthy"][d] * ( Ns["Contagious"][d] + Ns["Symtomatic"][d] + hide_factor * (Nw["Contagious"][d] + Nw["Symtomatic"][d])) / pop_alive )

	delta_Ns["Contagious"][d] = Convolve(delta_Ns["Incubating"], d, a=D_I, scale=Sig_I)
	delta_Nw["Contagious"][d] = Convolve(delta_Nw["Incubating"], d, a=D_I, scale=Sig_I)      

	#Need to think about this transition... 
	delta_Ns["Symtomatic"][d] = Convolve(delta_Ns["Contagious"], d, a=D_C, scale=Sig_C)      
	delta_Nw["Symtomatic"][d] = Convolve(delta_Nw["Contagious"], d, a=D_C, scale=Sig_C)      

	#Need to think about this transition...
	delta_Ns["Recovered"][d] = Convolve(delta_Ns["Symtomatic"], d, a=D_Ss, scale=Sig_Ss)      
	delta_Nw["Dead"][d] = Convolve(delta_Nw["Symtomatic"], d, a=D_Ss, scale=Sig_Sw)      


	#print(delta_Ns_Incubating, delta_Ns_Contagious, delta_Ns_Symtomatic, delta_Ns_Recovered)
	Ns["Healthy"][d+1] = max(Ns["Healthy"][d] - delta_Ns["Incubating"][d],0)
	Ns["Incubating"][d+1] = max(Ns["Incubating"][d] + delta_Ns["Incubating"][d] - delta_Ns["Contagious"][d],0)
	Ns["Contagious"][d+1] = max(Ns["Contagious"][d] + delta_Ns["Contagious"][d] - delta_Ns["Symtomatic"][d],0)


	Nw["Healthy"][d+1] = max(Nw["Healthy"][d] - delta_Nw["Incubating"][d],0)
	Nw["Incubating"][d+1] = max(Nw["Incubating"][d] + delta_Nw["Incubating"][d] - delta_Nw["Contagious"][d],0)
	Nw["Contagious"][d+1] = max(Nw["Contagious"][d] + delta_Nw["Contagious"][d] - delta_Nw["Symtomatic"][d],0)

	Ns["Symtomatic"][d+1] = max(Ns["Symtomatic"][d] + delta_Ns["Symtomatic"][d] - delta_Ns["Recovered"][d],0)
	Ns["Recovered"][d+1] = max(Ns["Recovered"][d] + delta_Ns["Recovered"][d],0)

	Nw["Symtomatic"][d+1] = max(Nw["Symtomatic"][d] + delta_Nw["Symtomatic"][d] - delta_Nw["Dead"][d],0)
	Nw["Dead"][d+1] = max(Nw["Dead"][d] + delta_Nw["Dead"][d],0)
	return Ns, Nw, delta_Ns, delta_Nw

def RunModel(days=200,pop=66.4e6,frac_fat=0.01,c_0=0.402, k_s=2.84, k_w=2.84):
	'''Run the model for the custom parameters provided'''
	Ns, Nw, delta_Ns, delta_Nw = CreateDataframes(pop, frac_fat, c_0, daystot)
	for d in range(0, daystot):
		Ns, Nw, delta_Ns, delta_Nw = PredictNextDay(Ns,Nw, delta_Ns, delta_Nw ,d, k_s, k_w)
	return Ns, Nw


if __name__ == '__main__':
	print("Run as test code")
	import plotting_routines as pr
	
	#Define test variables:
	daystot=200
	Ns, Nw = RunModel(days=daystot)
	pr.plot_strong(daystot, Ns)
	pr.plot_weak(daystot, Nw)
