'''
  File name: rmVerSeam.py
  Author:
  Date created:
'''

'''
  File clarification:
    Removes vertical seams. You should identify the pixel from My from which
    you should begin backtracking in order to identify pixels for removal, and
    remove those pixels from the input image.

    - INPUT I: n × m × 3 matrix representing the input image.
    - INPUT Mx: n × m matrix representing the cumulative minimum energy map along vertical direction.
    - INPUT Tbx: n × m matrix representing the backtrack table along vertical direction.
    - OUTPUT Ix: n × (m - 1) × 3 matrix representing the image with the row removed.
    - OUTPUT E: the cost of seam removal.
'''
import numpy as np
def rmVerSeam(I, Mx, Tbx):
  # Your Code Here
  E=min(Mx[Mx.shape[0]-1])
  Ix=np.copy(I)
  # print(Ix.shape)
  # print(E)
  path_ind=np.argmin(Mx[Mx.shape[0]-1])
  # print(start_ind)
  array=np.zeros(Mx.shape[0],2)
  #array[Mx.shape[0],0]
  mask=np.ones(Mx.shape,dtype=bool)
  for i in range(Mx.shape[0]-1,0,-1):
  	print(i)
    mask[i,path_ind]=False
    # print(Ix.shape)
    # Ix=np.delete(Ix[i,:,:],path_ind)
    # Ix=np.delete(Ix[i,:,1],path_ind)
    # Ix=np.delete(Ix[i,:,2],path_ind)
    # print(i)

    if(Tbx[i,path_ind]==1):
      path_ind=path_ind+1
    elif Tbx[i,path_ind]==-1:
      path_ind=path_ind-1
    elif Tbx[i,path_ind]==0:
      path_ind=path_ind
    else:
      print('value in Tbx not in [-1,1]')
  mask[0,path_ind]=False

  # print(np.count_nonzero(mask))
  # print(Ix.shape[0]*Ix.shape[1]-Ix.shape[0])
  # print(Ix.shape)
  Ix=Ix[mask]
  # print(Ix.shape)
  Ix=Ix.reshape(I.shape[0],I.shape[1]-1,3)
  # print(Ix.shape)
  return  Ix,E
