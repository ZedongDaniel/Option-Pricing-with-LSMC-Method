import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def stock_inputs(Ticker, start_date, end_date):
    stock_df = yf.download(Ticker, start = start_date, end= end_date, progress= False)
    
    T = ((np.datetime64(end_date) - np.datetime64(start_date))) /np.timedelta64(1,'D') / 365
    n = stock_df.shape[0]
    h = T/n
    
    log_return = (stock_df["Close"] / stock_df["Close"].shift(1)).apply(np.log).dropna().to_numpy()
    
    var = np.var(log_return)
    var_annul = var / h
    sigma = np.sqrt(var_annul)
    
    s0 = stock_df["Close"].iloc[-1]
    
    return s0, sigma

def drawer(Ticker, start_date, end_date):
    stock_df = yf.download(Ticker, start = start_date, end= end_date, progress= False)
    close_series = stock_df['Close']
    
    return_series = (stock_df["Close"] / stock_df["Close"].shift(1)).apply(np.log).dropna()
    
    plt.subplot(1,2,1)
    plt.plot(close_series.index, close_series)
    
    plt.subplot(1,2,2)
    plt.plot(return_series.index, return_series)    
    plt.show()

def jump_inputs(Ticker, start_date, end_date):
    stock_df = yf.download(Ticker, start = start_date, end= end_date, progress= False)
    
    T = ((np.datetime64(end_date) - np.datetime64(start_date))) /np.timedelta64(1,'D') / 365  
    n = stock_df.shape[0]
    h = T/n

    log_return = (stock_df["Close"] / stock_df["Close"].shift(1)).apply(np.log).dropna().to_numpy()
    
    upper = np.mean(log_return) + 3 * np.std(log_return)
    low = np.mean(log_return) - 3 * np.std(log_return)
    
    jump = log_return[np.logical_or(log_return < low, log_return > upper)]
    
    jump_count = len(jump) / T
    jump_alpha = np.mean(jump)
    jump_sigma = np.std(jump)
    
    return jump_count, jump_alpha, jump_sigma

def option_info(Ticker, ttm, call = False):
    option_name = yf.Ticker(Ticker)
    opt = option_name.option_chain(ttm)
    
    if call:
        df = opt.calls
    else:
        df = opt.puts
        
    strike = df["strike"].to_numpy()
    
    mid_price = (df["ask"] + df['bid'])/2
    mkt_price = mid_price.to_numpy()
    
    iv = df['impliedVolatility'].to_numpy()
    
    
    return strike, mkt_price, iv

if __name__ == "__main__":
    aapl = yf.Ticker('aapl')
    opt = aapl.option_chain('2024-03-15').calls
    print(opt.columns)
    
    