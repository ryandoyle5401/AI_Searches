# Maze Solver

# Project Description
At a high level, this project simulates a 2-dimensional maze and utilizes foundational artifical intelligence search algorithms to traverse the maze. To analyze how the different search algorithms perform, some performance measures such as the time taken to complete the maze, the number of nodes expanded, and the location of which nodes are expanded will also be displayed.  

Mazes are represented as both a 2D array, where 0's represent an open path and 1's represent walls, and as an adjacency list. The 2D array maze is used to give the user a visual understanding of what the maze looks like, and the adjacency list is used to perform graph-search algorithms over the maze.  

All mazes have the same starting and ending point. The starting point will always be the top-left corner of the maze, and the exit will always be the bottom-right corner of the maze. However, there will be different configurations of open paths and walls between different mazes. This to make the project more versatile and to analyze the performance of search algorithms over different maze configurations.  

# Code Structure
The overall structure of the project is simple: a 2-dimensional maze is created and represented as an array and as an adjacency list. The array is used for visualization of the maze, and the adjacency list is used for running search algorithms over the maze. A GUI interface allows the user to get a visualization of the maze, and allows the user to select which search algorithms to use.
