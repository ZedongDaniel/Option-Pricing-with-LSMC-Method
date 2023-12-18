import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from RealTimeData import stock_inputs, jump_inputs
from LSMC import OptionValue
import os

ticker = 'aapl'
start_date = '2018-12-16'
end_date = '2023-12-16'

spot, vol = stock_inputs(ticker, start_date, end_date)
numJ, alphaJ, volJ = jump_inputs(ticker, start_date, end_date)

print(f'underlying splot price: {spot:.2f}; historical volatility: {(vol * 100):.2f}%')
print(f'number of jumps per year: {numJ:.2f}; jump magnitude: {(alphaJ * 100):.2f} %; jump volatility: {(volJ * 100):.2f} %')

Rf = alpha = 0.0523 # three month treasury bill rate
T = 3/12
d = 0
strike = 200
n = 200
Nsim = 10000

put_200 = OptionValue(spot, 0.1950, d, alpha, T, n, Nsim, numJ, alphaJ, volJ, Rf, strike, False, True)
print(f'call option value is {put_200}')

NumSim_array = np.arange(1, 1001)
price_array1 = np.zeros(1000)
price_array2 = np.zeros(1000)

for i in range(0, 1000):
    price_array1[i] = OptionValue(spot, 0.1950, d, alpha, T, n, NumSim_array[i], numJ, alphaJ, volJ, Rf, strike, False, False)
    
for i in range(0, 1000):
    price_array2[i] = OptionValue(spot, 0.1950, d, alpha, T, n, NumSim_array[i], numJ, alphaJ, volJ, Rf, strike, False, True)  


if not os.path.exists('Figures'):
    os.makedirs('Figures')

plt.plot(np.arange(0, 1000), price_array1, price_array2)
plt.title("convergence")
plt.legend(["standard method", "stratified sampling"])
plt.ylabel("option value")
plt.xlabel("number of simuation")
plt.savefig('Figures/convergence_comparison.jpg')
plt.show()











