import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = df["weight"]/((df["height"]/100)**2)



# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df['overweight'] <= 25, ['overweight']] = 0
df.loc[df['overweight'] > 25, ['overweight']] = 1

df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1


# Draw Categorical Plot
def draw_cat_plot():
  
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    df_cat = df_cat.sort_values(by='variable')
    df_cat['value'] = df_cat['value'].astype(int)


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.

    df_cat = df_cat.groupby(['cardio', 'value', 'variable']).size().reset_index() 
    df_cat = df_cat.rename(columns={'cardio': 'cardio', 'value': 'value','variable': 'variable', 0: 'total'})
    
    

   #Draw the catplot with 'sns.catplot()'
    # Get the figure for the output
    graph = sns.catplot(y="total", x='variable', hue="value", kind="bar", col='cardio',data=df_cat)
    fig = graph.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]
    

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 6))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0, square=True, linewidths=.5)
    


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
