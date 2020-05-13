import numpy as np
import scipy.constants
import matplotlib.pyplot as plt

plt.style.use('seaborn-pastel')

reselc = scipy.constants.physical_constants["electric constant"]
(Eps, medida, nao) = reselc

V = 10e5
h = range(-5000, 5000)
t = np.arange(0, 0.005, 0.000001)  # Time
hb = 0
Dist = [1000, 7000, 15000]
eTot = []
eF4 = []
eC4 = []
primeiro = []
a = int(input('Qual distância medir ? \n 0 - 1.000 metros \n 1 - 7.000 metros \n 2 - 15.000 metros \n->'))

cont = 0

for i in t:
    hb = h[cont] - V * i

    # print('{:.4f}'.format(hb), end=', ')
    eF1 = -1e-3 / (2 * np.pi * Eps)
    eC1 = (1 / (hb + Dist[a] ** 2) ** (1 / 2)) - ((1 / (h[cont] ** 2 + Dist[a] ** 2)) ** (1 / 2)) - h[cont] * (
            h[cont] - hb) / ((h[cont] ** 2 + Dist[a] ** 2) ** (3 / 2))
    eF4.append(eF1)
    eC4.append(eC1)
    eT = (eF1 * eC1)/1000
    primeiro.append(eT)
    mx = primeiro[0]

    if cont >= 0 and mx > 0:
        eTot.append(eT + mx)
    elif cont >= 0 and mx < 0:
        eTot.append(eT - mx)

    cont += 1

plt.xlabel('Tempo [ms]')
plt.ylabel('Campo Elétrico \n ')
plt.title(f'Campo elétrico do Lider ({Dist[a]} metros)')
linha_Qtotal, = plt.plot(t, eTot, label='Campo Total')
plt.legend(handles=[linha_Qtotal])
plt.show()
