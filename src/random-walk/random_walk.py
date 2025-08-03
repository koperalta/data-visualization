from random import choice

# A random walk is a path that's determined by a series of simple decisions, each of which is left
# entirely to chance.

class RandomWalk:
    """ A class to generate random walks. """
    
    def __init__(self, num_points=5_000):
        """ Initialize the random walk with a specified number of steps. """
        self.num_points = num_points
        
        # All walks start at (0, 0). Together, these lists will hold all the points in the walk.
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        """ Calculate all the points in the walk. """
        # Keep taking steps until the walk reaches the desired number of points.
        while len(self.x_values) < self.num_points:
            # Decide which direction to go, and how far to go.
            x_step = self._get_xstep() # Get the x step
            y_step = self._get_ystep() # Get the y step
            
            # Calculate the new position
            x = self.x_values[-1] + x_step # Last x value + step
            y = self.y_values[-1] + y_step # Last y value + step
            
            # Append the new position to the lists.
            self.x_values.append(x)
            self.y_values.append(y)
    
    def _get_xstep(self) :
        # choice(1, -1) returns either 1 or -1
        x_direction = choice([1, -1]) # 1 for right, -1 for left
        
        # choice([0, 1, 2, 3, 4, 5, 6, 7, 8]) returns either 0, 1, 2, 3, or 4 which
        # represents the distance to move in the x direction.
        x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        
        # Calculate the x step based on the direction and distance.
        x_step = x_direction * x_distance
        
        return x_step

    def _get_ystep(self) :
        # choice(1, -1) returns either 1 or -1
        y_direction = choice([1, -1])
        
        # choice([0, 1, 2, 3, 4, 5, 6, 7, 8]) returns either 0, 1, 2, 3, or 4 which
        # represents the distance to move in the y direction.
        y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        
        # Calculate the y step based on the direction and distance.
        y_step = y_direction * y_distance
        
        return y_step