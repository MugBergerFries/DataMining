import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Plot size to 14" x 7"
matplotlib.rc('figure', figsize=(14, 7))
# Font size to 14
matplotlib.rc('font', size=14)
# Do not display top and right frame lines
matplotlib.rc('axes.spines', top=False, right=False)
# Remove grid lines
matplotlib.rc('axes', grid=False)
# Set backgound color to white
matplotlib.rc('axes', facecolor='white')


def temporal_graph(x_data, y_data, xlabel, ylabel, title):
	'''Input : x_data and y_data are the lists containing the data points for x and y axis
	xlabel and ylabel are the labels that should be given to the corresponding axes
	title contains the title of the graph

	Output : A temporal graph displayed'''
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title)
	y_data = np.array(y_data)
	plt.plot(x_data, y_data[:, 0], c='blue')
	plt.plot(x_data, y_data[:, 1], c='green')
	plt.show()


def boxplot(x_data, y_data, base_color, median_color, x_label, y_label, title):
	'''Input : x_data and y_data are the lists containing the data points for x and y axis
	base_color and median_color can be used to set colors in the graph.
	xlabel and ylabel are the labels that should be given to the corresponding axes
	title contains the title of the graph.

	Output : A boxplot displayed'''
	data = [x_data, y_data]
	fig1, ax1 = plt.subplots()
	ax1.set_title(title)
	bp = ax1.boxplot(data, patch_artist=True)
	for box in bp['boxes']:
		box.set(color=median_color)
		box.set_facecolor(base_color)
	plt.show()


def histogram(data, x_label, y_label, title):
	'''Input : data is the list containing the data points for histogram buckets
	xlabel and ylabel are the labels that should be given to the corresponding axes
	title contains the title of the graph

	Output : A histogram displayed'''
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.title(title)
	n, bins, patches = plt.hist(data, 10)
	plt.show()


def amzn_new_plot(open, close, title):
	'''Define this function as you would seem fit to display the plot that interests you using
	the same dataset. Define your function parameters and display the resulting plots'''
	data = np.subtract(close, open)
	fig1, ax1 = plt.subplots()
	ax1.set_title(title)
	bp = ax1.boxplot(data, patch_artist=True)
	ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
	for box in bp['boxes']:
		box.set(color='magenta')
		box.set_facecolor('blue')
	plt.show()


pdin = pd.read_csv('data/AMZN-5Y-HistoricalQuotes.csv')
date = pdin.loc[:, 'date']
close = pdin.loc[:, 'close']
volume = pdin.loc[:, 'volume']
opencol = pdin.loc[:, 'open']
high = pdin.loc[:, 'high']
low = pdin.loc[:, 'low']
tempdata = [list(i) for i in zip(opencol, close)]
# temporal_graph(date, tempdata, "date", "open/close value", "open/close vs date")
# boxplot(high, low, "aqua", "blue", "high", "low", "high and low box plot")
# histogram(volume, "volume", "count", "count per volume histogram")
amzn_new_plot(opencol, close, "Change in stock value from open to close")
