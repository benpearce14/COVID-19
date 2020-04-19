import numpy as np
import pandas as pd

import extract_data as ed
import model as md
import plotting_routines as pr


country_list = ['United Kingdom']
countries_info = ed.extract_countries(country_list)
    
pop = countries_info[0][1]
frac_fat = 0.01
c_0 = 1
k_s = 2.84
k_w = k_s # For now

D_I = 5
D_C = 3
D_S = 7

daystot = 200
Ns, Nw, delta_Ns, delta_Nw = CreateDataframes(pop, frac_fat, c_0, daystot)
for d in range(0, daystot):
Ns, Nw, delta_Ns, delta_Nw = PredictNextDay(Ns,Nw, delta_Ns, delta_Nw ,d, k_s, k_w)

pr.plot_strong(daystot, Ns)
pr.plot_weak(daystot, Nw)
