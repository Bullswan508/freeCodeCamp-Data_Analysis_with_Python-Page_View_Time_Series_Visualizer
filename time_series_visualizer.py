import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('./fcc-forum-pageviews.csv', parse_dates=['date']).set_index('date')

df.rename(columns={'value' : 'total_views'}, inplace=True)

# Clean data
df.drop(df[(df['total_views'] > df['total_views'].quantile(0.975)) | (df['total_views'] < df['total_views'].quantile(0.025))].index, inplace=True)


def draw_line_plot():
    # Draw line plot

    fig, ax = plt.subplots()

    fig.set_size_inches(16, 5)

    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    sns.lineplot(data=df, ax=ax, legend=False, palette=['red'])



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['year'] = [d.year for d in df_bar.date]
    df_bar['month'] = [d.month for d in df_bar.date]

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.barplot(x='year', y='total_views', data=df_bar, hue='month', palette='bright', ax=ax, errorbar=None)
    # set legend labels
    labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September','October', 'November', 'December']
    for t, l in zip(ax.legend(loc='upper left', title='Months').texts, labels): t.set_text(l)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_title('Average Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    # plt.show(fig)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig, ax = plt.subplots(1, 2, figsize=(40, 15))

    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    ax[0].set_title('Year-wise Box Plot (Trend)')

    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')

    sns.boxplot(data=df_box, ax=ax[0], x='year', y='total_views', hue='year', legend=False, palette='tab10')

    sns.boxplot(data=df_box, ax=ax[1], x='month', y='total_views', hue='month', legend=False, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

if __name__ == '__main__':
    
    draw_bar_plot()