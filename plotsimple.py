import PySimpleGUI as sg 
import simpleplot as sp
import random 

def main():
	sg.theme('Material2')
	x, y = range(40), range(40)
	# init PlotGraph object with the initial set of points and key 
	plot = sp.PlotGraph('graph',x, y )
	# put object into layout and finalize window 
	layout = [[plot]]
	window = sg.Window('', layout).finalize()
	# begin plotting 
	#-----------------

	# draw the plot rect 
	# Method: draw_plot_rect
	plot.draw_plot_rect()

	# plot the set of initial points 
	# Method: plot_points
	plot.plot_points()

	# plot as many additional points as you'd like 
	# Method: plot_more_points
	# x2, y2 = range(-40, 40), [-i**2 +1500 for i in range(-40, 40)]
	x2, y2 = range(40), [random.randint(0,40) for i in range(40)]
	plot.plot_more_points(x2, y2)

	# draw a legend 
	# Method: draw_legend
	plot.draw_legend(['y = x', 'random'])



	while True:
		event, values = window.read()
		if event in (None, sg.WIN_CLOSED):
			break

		
	window.close()

if __name__ == '__main__':
	main()