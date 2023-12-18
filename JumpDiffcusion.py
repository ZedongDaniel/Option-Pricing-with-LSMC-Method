# load packages
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def SimStockPrice(s0: float, sigma: float, d: float, alpha: float, T: float, n: float, Nsim: float, lam: float, alphaJ: float, sigmaJ: float , stratified: bool) -> np.ndarray:       
    if stratified:
        unif_samples = np.random.uniform(0,1,(n, Nsim)) # set stratified sampling z
        stratified_samples = (np.arange(1, Nsim + 1) - unif_samples) / Nsim
        z = norm.ppf(stratified_samples,0,1)
        
        for t in np.arange(0, n): # create random order of z-value matrix by row
            np.random.shuffle(z[t,:])  
    else:
        z = np.random.normal(0,1,size = (n, Nsim)) # initize z value
    
    prices = np.zeros((n, Nsim))
    prices[0,:] = s0

    h = T/n # calculate horizontial time
    k = np.exp(alphaJ) -1
    J = np.random.poisson(lam*h ,size = (n, Nsim)) # this section simulate number of jump per period 
    sum_w = np.zeros((n, Nsim))       # and magnitude of each jump

    for i in np.arange(0, Nsim):
        for t in np.arange(0, n):
            w = np.random.normal(0,1,size = J[t,i])
            sum_w[t,i] = np.sum(w)

    for t in np.arange(1,n):  # recursively append price              
        drift = (alpha - lam*k - d - 0.5 * sigma**2) * h
        diffusion = sigma * np.sqrt(h) * z[t,:]
        jump = J[t,:] * (alphaJ - 0.5 * sigmaJ**2) + sigmaJ * sum_w[t,:]

        prices[t, :] = prices[t-1, :] * np.exp(drift + diffusion + jump)
        
    return prices

if __name__ == "__main__":
    s0 = 200
    alpha = 0.05
    d = 0
    sigma = 0.17
    T = 1
    n = 252
    Nsim = 1000
    lam = 2
    alphaJ = 0.1
    sigmaJ = 0.1
    stratified = True
    
    SimPrice = SimStockPrice(s0, sigma, d, alpha , T , n , Nsim , lam , alphaJ , sigmaJ  , stratified)
    
    plt.plot(SimPrice[:,:])
    plt.ylabel("Simulated Stock Price")
    plt.xlabel("time")
    plt.show()
    
    
    