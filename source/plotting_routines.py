#import matplotlib
#matplotlib.use('agg')

import matplotlib.pyplot as plt
import seaborn as sns


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
		plt.legend(loc=2, fontsize=8)
		plt.semilogy()
		plt.savefig('../data_plots/%s.pdf' % countries_info[i][0])
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
	plt.legend(loc=2)
	plt.savefig("../model_plots/strong_test.pdf")
	plt.close()


def plot_weak(daystot, Ns):
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
	plt.legend(loc=2)
	plt.savefig("../model_plots/weak_test.pdf")
	plt.close()
	print('Test run completed')
