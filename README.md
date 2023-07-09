# Option-Pricing-with-LSMC-Method

This jupyter notebook is for the capstone project in FINA 4529 (Derivatives II) at Carlson School of Management, University of Minnesota.  

The program simulate stock price based on jump-diffusion model, and pricing American option using the method of Longstaff and
Schwartz (2001), which is also called least square monte carlo method.  

It also embeded stratified sampling feature, one of variance reduction techniques,  into the simulating function to improve the pricing efficiency.  

In the notebook and the project report, I compared two simulation method and analyze the convergence advantage of stratified sampling method.

In the end of the notebook, I used the pricing function to price five actual option traded on the market, and compared simulated price with real traded prices.  
