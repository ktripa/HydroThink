import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file_path = 'path_of_your_downloaded_nino3.4_data.txt'


def plot_nino34_data(file_path):
    # Load the data
    data = pd.read_csv(file_path, delim_whitespace=True, header=None)
    data.columns = ['Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Replace -99.99 with NaN
    data.replace(-99.99, np.nan, inplace=True)

    # Melt the dataframe to long format
    data_long = data.melt(id_vars=['Year'], var_name='Month', value_name='Anomaly')
    data_long['Date'] = pd.to_datetime(data_long['Year'].astype(str) + '-' + data_long['Month'])

    # Sorting by Date to ensure the plot is in order
    data_long.sort_values('Date', inplace=True)

    # Plotting
    plt.figure(figsize=(14, 7))
    plt.plot(data_long['Date'], data_long['Anomaly'], label='Niño 3.4 Index', color='blue')
    plt.axhline(0, color='black', linewidth=0.8)  # Add a line at zero anomaly for reference
    plt.title('Monthly Niño 3.4 Index (Sea Surface Temperature Anomaly)')
    plt.xlabel('Year')
    plt.ylabel('Temperature Anomaly (°C)')
    plt.grid(True)
    plt.legend()
    plt.show()


plot_nino34_data(file_path)
