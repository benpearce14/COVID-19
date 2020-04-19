import numpy as np
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

D_I = 5
D_C = 0
D_S = 5



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

	if d - D_I >= 0:
		delta_Ns["Contagious"][d] = ( delta_Ns["Incubating"][d - D_I] )
		delta_Nw["Contagious"][d] = ( delta_Nw["Incubating"][d - D_I] )

	if d - D_C >= 0:
		delta_Ns["Symtomatic"][d] = ( delta_Ns["Contagious"][d -D_C] )
		delta_Nw["Symtomatic"][d] = ( delta_Nw["Contagious"][d -D_C] )

	if d - D_S >= 0:
		delta_Ns["Recovered"][d] = ( delta_Ns["Symtomatic"][d -D_S] )
		delta_Nw["Dead"][d] = ( delta_Nw["Symtomatic"][d -D_S] )


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
	print(Ns)

	pr.plot_strong(daystot, Ns)
	pr.plot_weak(daystot, Nw)
