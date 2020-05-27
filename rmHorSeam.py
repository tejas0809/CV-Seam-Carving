'''
  File name: rmHorSeam.py
  Author:
  Date created:
'''

'''
  File clarification:
    Removes horizontal seams. You should identify the pixel from My from which
    you should begin backtracking in order to identify pixels for removal, and
    remove those pixels from the input image.

    - INPUT I: n × m × 3 matrix representing the input image.
    - INPUT My: n × m matrix representing the cumulative minimum energy map along horizontal direction.
    - INPUT Tby: n × m matrix representing the backtrack table along horizontal direction.
    - OUTPUT Iy: (n − 1) × m × 3 matrix representing the image with the row removed.
    - OUTPUT E: the cost of seam removal.
'''
import numpy as np
from rmVerSeam import rmVerSeam
def rmHorSeam(I, My, Tby):
  # Your Code Here
  E=min(My[:,My.shape[1]-1])
  I1=np.transpose(I,(1,0,2))
  My1=np.transpose(My)
  Tby1=np.transpose(Tby)
  Ix1,E1=rmVerSeam(I1,My1,Tby1)
  Iy=np.transpose(Ix1,(1,0,2))
  return Iy, E
