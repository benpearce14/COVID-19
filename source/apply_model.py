import numpy as np
import pandas as pd

import extract_data as ed
import model as md
import plotting_routines as pr


country_list = ['United Kingdom']
countries_info = ed.extract_countries(country_list)

pop = countries_info[0][1]

frac_fat = 0.01
c_0 = 0.402
#c_0 = 153.639
k_s = 2.84
#k_s = 2.0376
k_w = k_s # For now

daystot = 200
Ns, Nw, delta_Ns, delta_Nw = md.CreateDataframes(pop, frac_fat, c_0, daystot)
for d in range(0, daystot):
    Ns, Nw, delta_Ns, delta_Nw = md.PredictNextDay(Ns,Nw, delta_Ns, delta_Nw ,d, k_s, k_w)

pr.plot_country_evolution(daystot, countries_info[0], Nw)
