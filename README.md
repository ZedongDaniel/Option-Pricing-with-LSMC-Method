# Option-Pricing-with-LSMC-Method

This jupyter notebook is for the capstone project in FINA 4529 (Derivatives II) at Carlson School of Management, University of Minnesota.  

The program simulates stock price based on the jump-diffusion model and pricing the American option using the Longstaff and Schwartz (2001) method, which is also called the least square monte carlo method. It also embedded the stratified sampling feature, one of the variance reduction techniques, into the simulating function to improve pricing efficiency. That is said, it simulates uniform random variables first and then simulates standard normal random variable $Z_{i}$ using $u_{i}$ so that it can improve sampling accuracy by reducing sampling error.


Take Apple's share as an example. At the time of working on this project, the spot price for Aapl is around $165 (the price has skyrocketed to $190 now.) I estimated historical volatility, the number of jumps, and other inputs; the program simulate 1000 stock paths using both the normal jump method and the stratified sampling method.  
![ ](https://github.com/ZedongDaniel/Option-Pricing-with-LSMC-Method/blob/a6cbc36be2f5129ba287b8e379d65530f52be950/images/simulated%20stock%20path.jpg)

Then, I compared two simulation methods and analyzed the stratified sampling method's convergence advantage.  
At the end of the notebook, I used the pricing function to price five actual options traded on the market and compared simulated prices with real traded prices.  




