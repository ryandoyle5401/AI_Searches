import matplotlib.pyplot as plt
from matplotlib import colormaps

def display_maze(maze, color):
    plt.imshow(maze, cmap=color)
    #plt.matshow(maze, cmap='viridis')
    plt.axis('off')  # Turn off the axis
    plt.show()

# Example maze
maze = [
    [0, 0, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0]
]

display_maze(maze, 'cool_r')
