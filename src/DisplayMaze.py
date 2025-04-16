import matplotlib.pyplot as plt
import random

def display_maze(maze):
    color = select_display_color()
    plt.imshow(maze, cmap=color)
    plt.axis('off')  # Turn off the axis
    plt.show()

def select_display_color():
    color_maps = [
        "spring", "cividis", "plasma", "RdGy",
        "Wistia", "brg", "bwr", "flag", "gnuplot",
        "nipy_spectral", "tab20b", "RdGy_r", "cool_r"
    ]
    choice = random.randrange(0,13)  # Select a random value from 0 to 12
    return color_maps[choice]  # Returns a randomly selected color map for the display
