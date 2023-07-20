# Option-Pricing-with-LSMC-Method

This jupyter notebook is for the capstone project in FINA 4529 (Derivatives II) at Carlson School of Management, University of Minnesota.  

The program simulates stock price based on the jump-diffusion model and pricing the American option using the Longstaff and Schwartz (2001) method, also called the least square monte carlo method. It also embedded the stratified sampling feature, one of the variance reduction techniques, into the simulating function to improve pricing efficiency. That is said, it simulates uniform random variables $u_{i}$ first and then simulates standard normal random variable $Z_{i}$ using $u_{i}$. In this way, it can improve sampling accuracy by reducing sampling error.   

Take Apple's share as an example. When working on this project, the spot price for AAPL is around $165 (the price has skyrocketed to $190.) I estimated historical volatility, the number of jumps, and other inputs; the program simulated 1000 stock paths using both the standard jump method and the stratified sampling method.  
![ ](https://github.com/ZedongDaniel/Option-Pricing-with-LSMC-Method/blob/a6cbc36be2f5129ba287b8e379d65530f52be950/images/simulated%20stock%20path.jpg)

Then, I compared two simulation methods and analyzed the stratified sampling method's convergence advantage. By looking directly at the figure, the stratified sampling method converges to the "true" place faster than the simple method， resulting in a smaller variance in the whole process.  
![ ](https://github.com/ZedongDaniel/Option-Pricing-with-LSMC-Method/blob/0970b50f076825071ec3df0905cad4e4ddaf067e/images/comvergence%20comparison.jpg)

At the end of the project, I used the pricing function to price five actual options traded on the market and compared simulated prices with real traded prices. For demonstration, I attached a figure showing the simulation's performance on LuLu's put option. The simulation went well; the simulated prices matched the actual traded price. The anomaly happened when the strike price was around 450. It is because I used the ask price to represent the "actual price" when the strike price was about 450, Yahoo Finance did not provide the ask price. One improvement could be using mid-price to represent the actual trade price.  
![ ](https://github.com/ZedongDaniel/Option-Pricing-with-LSMC-Method/blob/08d4243616266fcb76671cf32838120cf9cb2864/images/Lulu's%20Put.jpg)





