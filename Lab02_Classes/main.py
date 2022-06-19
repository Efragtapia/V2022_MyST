import data as dt
import visualizations as vz
import functions as fn

import numpy as np
import pandas as pd

#Read input data
data_ob= dt.ob_data

#Cantidad libros de ordenes hay en total
n_libros=len(list(data_ob.keys()))
print(f"La cantidad total de libros de ordenes es: {n_libros}")

#--- Calcular midprice

ob_ts=list(data_ob.keys())[9:]
l_ts=[pd.to_datetime(i_ts) for i_ts in ob_ts]
mid_price = [(data_ob[ob_ts[i]]['ask'][0] + data_ob[ob_ts[i]]['bid'][0])*0.5 for i in range(0, len(ob_ts))]

# -- Contabilizar ocurrencias de escenarios (Utilizando todos los datos)
# e1 = midprice_t == midprice_t+1
# e2 = midprice_t != midprice_t+1 , e2 = total_datos - el

total = len(mid price)-1

# NOTA: Para contabilizar los el de acuerdo a esta formulacion => P_t = E[P_t+1]

el = [mid_price[i] == mid_price[i+1] for 1 in range(len(mid_price)-1)]
e2 = total - sum(el)

#-- Guardar resultados de conteo y de proporcion en un diccionario

exp_1 ={'e1': {'cantidad'; el, 'proporcion': np.round(sum(el)/total, 2)},
	'e2': {'cantidad': e2, 'proporcion': np.round(e2/total, 2)},
	'total': len(mid_price)-1}

# imprimir los resultados

exp_1['el']['proporcion']
exp_1['e2']['proporcion']

minutes= list(np.arange(0.60))

exp_2 = pd.DataFrame({'intervalo': list(np.arange(0,60)), 'total': [2391]*len(minutes),
		      'e1_conteo': [1757]*len(minutes), 'e1_proporcion': [.73]*len(minutes),
                      'e2_conteo': [634]*len(minutes), 'e2_proporcion': [.27]*len(minutes)},
		       index=list(np.arange(0,60)))

