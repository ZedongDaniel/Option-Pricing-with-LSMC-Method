import numpy as np
from scipy.stats import norm

from JumpDiffcusion import SimStockPrice

def OptionValue(s0, sigma, d, alpha, T, n, Nsim, lam, alphaJ, sigmaJ, r,k, Call = False, stratified = False):
    price_paths = SimStockPrice(s0, sigma, d, alpha, T, n, Nsim, lam, alphaJ, sigmaJ,stratified)
    
    h = T/n 
    df = np.exp(-r*h)
    
    if Call:
        EV = np.maximum(price_paths[1:,:] - k,0)
    else:
        EV = np.maximum(k - price_paths[1:,:],0)
        
    price_paths = price_paths[1:,:]
    Time, Paths = EV.shape

    V = np.zeros((Time, Paths))

    V[-1,:] = EV[-1,:]

    for t in np.arange(Time-2, -1, -1):

        ITM = EV[t, :] > 0

        X = np.vstack((np.ones(len(price_paths[t, ITM])), price_paths[t, ITM], price_paths[t, ITM]**2)).T
        y = V[t+1, ITM] * df
        bhat = np.linalg.lstsq(X, y,rcond=0)[0]
        CV = bhat[0] + bhat[1]*price_paths[t, ITM] + bhat[2]*price_paths[t, ITM]**2  

        exercise = EV[t, ITM] > CV 

        index_exercise = np.zeros(Paths)
        index_exercise[ITM] = 1
        index_exercise = index_exercise.astype('bool')
        index_exercise[ITM] = exercise

        V[t, index_exercise] = EV[t, index_exercise]
        V[t+1:, index_exercise] = 0
        
        V[t, np.logical_not(index_exercise)] = V[t+1, np.logical_not(index_exercise)] * df

    option_value = np.mean(V[0,:]) *df
    
    return option_value

if __name__ == "__main__":
    # test_value = OptionValue(40, 0.2,0, 0.06, 1, 1000, 10000, 0, 0, 0, 0.06, 40, Call = False, stratified=False)
    # print(f'the put option value is: {test_value:.5f}')
    
    v= OptionValue(50, 0.4, 0, 0.1, 5/12, 200, 10000, 0, 0, 0, 0.1, 60, False, False)
    print(v)