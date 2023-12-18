import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from RealTimeData import stock_inputs, jump_inputs, option_info
from LSMC import OptionValue
import os

ticker = 'aapl'
start_date = '2018-12-16'
end_date = '2023-12-16'

spot, vol = stock_inputs(ticker, start_date, end_date)
numJ, alphaJ, volJ = jump_inputs(ticker, start_date, end_date)

print(f'underlying splot price: {spot:.2f}; historical volatility: {(vol * 100):.2f}%')
print(f'number of jumps per year: {numJ:.2f}; jump magnitude: {(alphaJ * 100):.2f} %; jump volatility: {(volJ * 100):.2f} %')

TTM = '2024-03-15'
strike_array, mkt_call, iv_array = option_info(ticker, TTM, call = True)

Rf = alpha = 0.0523 # three month treasury bill rate
T = 3/12
d = 0
strike = 200
n = 100
Nsim = 1000

mc_call = np.zeros((len(strike_array)))
for i in np.arange(len(strike_array)):
    mc_call[i] = OptionValue(spot, iv_array[i], d, alpha, T, n, Nsim, numJ, alphaJ, volJ, Rf, strike_array[i], Call = True, stratified=True)


if not os.path.exists('Figures'):
    os.makedirs('Figures')
     
plt.plot(strike_array, mc_call, label = "MC call price")
plt.plot(strike_array, mkt_call, label = "Acutal call Price")
plt.legend()
plt.ylabel("call Price")
plt.xlabel("strike price")
plt.title("Monte Carlo Price vs Actual Price")
plt.savefig("Figures/AAPL Call_2024_03_15.jpg")
plt.show()

strike_array, mkt_put, iv_array = option_info(ticker, TTM, call = False)
mc_put = np.zeros((len(strike_array)))
for i in np.arange(len(strike_array)):
    mc_put[i] = OptionValue(spot, iv_array[i], d, alpha, T, n, Nsim, numJ, alphaJ, volJ, Rf, strike_array[i], Call = False, stratified=True)

plt.plot(strike_array, mc_put, label = "MC put price")
plt.plot(strike_array, mkt_put, label = "Acutal put Price")
plt.legend()
plt.ylabel("put Price")
plt.xlabel("strike price")
plt.title("Monte Carlo Price vs Actual Price")
plt.savefig("Figures/AAPL Put_2024_03_15.jpg")
plt.show()

if not os.path.exists('Data Folder'):
    os.makedirs('Data Folder')
    
pd.DataFrame(mc_put).to_csv('Data Folder/MC put_2024_03_15.csv')
pd.DataFrame(mkt_put).to_csv('Data Folder/MKT put_2024_03_15.csv')


