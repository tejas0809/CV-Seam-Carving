###CIS581: Computer Vision and Computational Photography\\
###Project 2, Part B: Seam Carving\\
##Name: Tejas Srivastava tjss@seas.upenn.edu  14547354\\

The objective of the project was to implement image resizing based on minimum cost seam carving .\\

##File structure
- cumMinEngHor.py: computes the cumulative minimum energy over the horizontal direction (uses genEngMap).
- cumMinEngVer.py: computes the cumulative minimum energy over the vertical direction (uses genEngMap).
- rmHorSeam.py: removes the horizontal seam with the minimum energy.
- rmVerSeam.py: removes the vertical seam with the minimum energy.
- genEngMap.py: used to create the energy map for a given image.(Already given)
- carv.py: resizing the image by removing the specified number of seams along the rows and columns using dynamic programming. (uses cumMinEngHor, cumMinEngVer, rmHorSeam, rmVerSeam).	Also, generated the gif of the images of different sizes( as the transition occurs from one size to another)
- run.py: used to take image as input, the number of rows and columns to be removed and call the carv.py on it, to perform the operation.
	
	
##Running the code
- Simply use 'python3 run.py' for running the code.
- Please make sure the required dependencies are installed.
- To change the input image, change the name of the image in line 5 of run.py
- Number of seams to be removed along the row and columns can also be changed in line 5 of run.py
- The name of the output gif can be changed in line 123 of carv.py 

