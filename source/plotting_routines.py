import matplotlib
matplotlib.use('agg')

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plot_countries(countries_info):
	'''Plot raw data for given list of countries'''
	for i in range(len(countries_info)):
		dates = countries_info[i][2]
		x_vals = np.arange(0,len(dates))
		plt.figure()
		plt.plot(x_vals, countries_info[i][3], label='Confirmed')
		plt.plot(x_vals, countries_info[i][4], label='Recovered')
		plt.plot(x_vals, countries_info[i][5], label='Deaths')
		plt.title('%s' % countries_info[i][0])
		plt.xlim(0,max(x_vals))
		plt.xlabel('Days')
		plt.ylabel('N')
		plt.legend(loc='best', fontsize=8)
		plt.semilogy()
		plt.savefig('../data_plots/%s.pdf' % countries_info[i][0])
		plt.close()

		
def plot_countries_confirmed_million(countries_info):
	'''Plot raw data of confirmed cases per million of population for a list of countries'''
	try:
		dates = countries_info[0][2]
		x_vals = np.arange(0,len(dates))
		plt.figure()
	except:
		print('No countries in list specified or error in list.')
		return
	for i in range(len(countries_info)):
		plt.plot(x_vals, countries_info[i][3]*1.0e6/countries_info[i][1], label=countries_info[i][0])
	plt.title('Confirmed Cases (per million)')
	plt.xlim(0,max(x_vals))
	plt.xlabel('Days')
	plt.ylabel('N')
	plt.legend(loc='best', fontsize=8)
	plt.semilogy()
	plt.savefig('../data_plots/confirmed_per_million.pdf')
	plt.close()
	
	
def plot_countries_recovered_million(countries_info):
	'''Plot raw data of recoveries per million of population for a list of countries'''
	try:
		dates = countries_info[0][2]
		x_vals = np.arange(0,len(dates))
		plt.figure()
	except:
		print('No countries in list specified or error in list.')
		return
	for i in range(len(countries_info)):
		plt.plot(x_vals, countries_info[i][4]*1.0e6/countries_info[i][1], label=countries_info[i][0])
	plt.title('Recoveries (per million)')
	plt.xlim(0,max(x_vals))
	plt.xlabel('Days')
	plt.ylabel('N')
	plt.legend(loc='best', fontsize=8)
	plt.semilogy()
	plt.savefig('../data_plots/recovered_per_million.pdf')
	plt.close()
	

def plot_countries_deaths_million(countries_info):
	'''Plot raw data of deaths per million of population for a list of countries'''
	try:
		dates = countries_info[0][2]
		x_vals = np.arange(0,len(dates))
		plt.figure()
	except:
		print('No countries in list specified or error in list.')
		return
	for i in range(len(countries_info)):
		plt.plot(x_vals, countries_info[i][5]*1.0e6/countries_info[i][1], label=countries_info[i][0])
	plt.title('Deaths (per million)')
	plt.xlim(0,max(x_vals))
	plt.xlabel('Days')
	plt.ylabel('N')
	plt.legend(loc='best', fontsize=8)
	plt.semilogy()
	plt.savefig('../data_plots/deaths_per_million.pdf')
	plt.close()
	
	
def plot_strong(daystot, Ns):
	plt.figure()
	plt.plot(np.arange(0,daystot+1), Ns["Healthy"], label='Healthy', color='green')
	plt.plot(np.arange(0,daystot+1), Ns["Incubating"], label='Incubating', color='orange')
	plt.plot(np.arange(0,daystot+1), Ns["Contagious"], label='Contagious', color='pink')
	plt.plot(np.arange(0,daystot+1), Ns["Symtomatic"], label='Symtomatic', color='red')
	plt.plot(np.arange(0,daystot+1), Ns["Recovered"], label='Recovered', color='grey')
	plt.semilogy()
	plt.xlabel('Days')
	plt.ylabel('N')
	plt.xlim(0, daystot)
	plt.ylim(1)
	plt.title('Strong Population')
	plt.legend(loc='best', fontsize=8)
	plt.savefig("../model_plots/strong_test.pdf")
	plt.close()


def plot_weak(daystot, Nw):
	plt.figure()
	plt.plot(np.arange(0,daystot+1), Nw["Healthy"], label='Healthy', color='green')
	plt.plot(np.arange(0,daystot+1), Nw["Incubating"], label='Incubating', color='orange')
	plt.plot(np.arange(0,daystot+1), Nw["Contagious"], label='Contagious', color='pink')
	plt.plot(np.arange(0,daystot+1), Nw["Symtomatic"], label='Symtomatic', color='red')
	plt.plot(np.arange(0,daystot+1), Nw["Dead"], label='Dead', color='grey')
	plt.semilogy()
	plt.xlabel('Days')
	plt.ylabel('N')
	plt.xlim(0, daystot)
	plt.ylim(1)
	plt.title('Weak Population')
	plt.legend(loc='best', fontsize=8)
	plt.savefig("../model_plots/weak_test.pdf")
	plt.close()
	print('Test run completed')
	
	
def plot_country_evolution(daystot, first_death_day, countries_info, Nw):
	x_vals = np.arange(0,daystot+1)+first_death_day
	dates = np.arange(0,len(countries_info[2]))
	plt.figure()
	plt.plot(dates, countries_info[3], label='Confirmed Cases')
	plt.plot(dates, countries_info[5], label='Confirmed Deaths')
	plt.plot(x_vals, Nw["Dead"], label='Modelled Deaths')
	plt.title('%s' % countries_info[0])
	plt.ylim(1, 1e8)
	plt.xlim(0, 120)
	plt.xlabel('Days')
	plt.ylabel('N')
	plt.legend(loc=2, fontsize=8)
	plt.semilogy()
	plt.savefig('../model_plots/%s.pdf' % countries_info[0])
	plt.close()
