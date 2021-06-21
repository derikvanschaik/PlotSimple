import PySimpleGUI as sg

class PlotGraph(sg.Graph):

	# Params: y_values, x_values = list of ints. point_color = string representing color. 
	def __init__(self, key, x_vals, y_vals, size = (400, 400)):
		self.size = size 
		self.key = key
		self.border_offset = 10
		self.points = list(map(lambda x, y: (x, y), x_vals, y_vals)) # list of the points to later plot
		self.point_count = 0 #we have plotted one set of points so far
		self.point_colors_default = ['RoyalBlue', 'red', 'orange', 'purple', 'green', 'yellow', 'peach', 'turquoise'] # index into this list based on point count -- wll need a lot more colors 

		if len(y_vals) != len(x_vals):
			raise ValueError("ERROR: Y values must contain the same number of elements as your x values.")

		max_y = max(y_vals)
		min_y = min(y_vals) if min(y_vals) < 0 else 0 
		max_x = max(x_vals)
		min_x = min(x_vals)

		self.canvas_bott_left = (min_x - self.border_offset, min_y - self.border_offset) 
		self.canvas_top_right = (max_x + self.border_offset, max_y + self.border_offset)
		# instantiate the sg.Graph object 
		super().__init__(self.size, self.canvas_bott_left, self.canvas_top_right, enable_events = True)

	def draw_plot_rect(self):
		rect_bott_left = tuple(map(lambda corner: corner + self.border_offset, self.canvas_bott_left))
		rect_top_right = tuple(map(lambda corner: corner - self.border_offset, self.canvas_top_right))
		super().draw_rectangle(rect_bott_left, rect_top_right, line_color = "black")

	def plot_points(self):

		color = self.point_colors_default[self.point_count] #default color
		self.point_count += 1
		for point in self.points:
			super().draw_point(point, size= 1, color=color)

	def get_point_str(self):
		return f"points: {self.points}"

	def plot_more_points(self, x_vals, y_vals):

		color = self.point_colors_default[self.point_count] #default color
		self.points = [self.points] #converts self.points to a list of list of points to accomodate more points 
		self.points.append(list(map(lambda x, y: (x, y), x_vals, y_vals))) #append the new points at the end of list 
		for point in self.points[self.point_count]:
			super().draw_point(point, size= 1, color=color)
		self.point_count += 1 

	def draw_legend(self, names):
		legend_loc = self.canvas_bott_left[0]+2, self.canvas_top_right[1] - 2 # top left corner shifted down a bit
		horiz_shift = 0
		vert_shift = 0
		for i, name in enumerate(names):
			super().draw_point(legend_loc, size = 1, color = self.point_colors_default[i])
			super().draw_text( name, (legend_loc[0]+ 5, legend_loc[1]) )
			legend_loc = (legend_loc[0] + 10, legend_loc[1]) 

	# will increase the rectangle by this delta -- WILL NOT SCALE THE UNITS OR POINTS ETC
	def increase_plot_size(self, delta):
		super().erase() # we want to clear the canvas to redraw the rect and points with new rect
		self.border_offset -= delta 
		self.draw_plot_rect()

		for i in range(self.point_count):
			for point in self.points[i]:
				super().draw_point(point, size = 1, color = self.point_colors_default[i])

	










