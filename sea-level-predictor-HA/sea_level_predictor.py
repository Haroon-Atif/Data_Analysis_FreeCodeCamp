import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np 

def draw_plot():
  
    # Read data from file
  df = pd.read_csv("epa-sea-level.csv")
  x = df['Year']
  y = df['CSIRO Adjusted Sea Level']
    # Create scatter plot
  fig = plt.figure(figsize=(12,6))
  plt.scatter(x,y)

    # Create first line of best fit
  line1 = linregress(x, y)
  x1 = np.arange(x.min(),2051)
  y1 = line1.slope*x1 + line1.intercept 
  plt.plot(x1, y1, 'r')
  
    # Create second line of best fit
  df_2000 = df[df['Year'] >= 2000]

  z = df_2000['Year']
  w = df_2000['CSIRO Adjusted Sea Level']
  line2 = linregress(z,w)
  z1 = np.arange(2000,2051)
  w1 = line2.slope*z1 + line2.intercept
  plt.plot(z1, w1, 'r')
  
    # Add labels and title
  plt.title('Rise in Sea Level')
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()

