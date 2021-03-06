import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def graph_price_seniment(sentiment, price):
    """
    This method graphs the sentiment as a bar graph over the price which is a line graph
    :param sentiment: the sentiment dateTime series containing sentiment scores at a given time
    :param price: the price dateTime series which has the value for each hour
    """

    sentiment = pd.Series(sentiment['Sentiment'], index=sentiment.index)
    price = pd.Series(price['Price'], index=price.index)

    # reverse the price data so that it is in ascending order like the sentiment data
    price = price.iloc[::-1]

    # find the minimum start time between the sentiment and the price data
    startTime = max(sentiment.index[0], price.index[0])

    # keep only rows that have the share the same date times
    price = price[startTime:sentiment.index[-1]]
    sentiment = sentiment[startTime:]

    # Plot graph with 2 y axes
    fig, ax1 = plt.subplots()

    # Plot price as line
    ax1.plot(price.index, price, 'r-')
    # Set the x-axis label
    ax1.set_xlabel('Time')

    # Set the y-axis label
    ax1.set_ylabel('Price')

    # Set up ax2 to be the second y axis with x shared
    ax2 = ax1.twinx()
    # Add bar plot for the sentiment
    ax2.bar(sentiment.index, sentiment, width=0.04, alpha=.5)
    ax2.set_ylim(sentiment.min() * 1.1, sentiment.max() * 1.1)

    plt.show()




