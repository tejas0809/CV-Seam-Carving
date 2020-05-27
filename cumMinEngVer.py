'''
  File name: cumMinEngVer.py
  Author:
  Date created:
'''
'''
  File clarification:
    Computes the cumulative minimum energy over the vertical seam directions.

    - INPUT e: n × m matrix representing the energy map.
    - OUTPUT Mx: n × m matrix representing the cumulative minimum energy map along vertical direction.
    - OUTPUT Tbx: n × m matrix representing the backtrack table along vertical direction.
'''
import numpy as np

def cumMinEngVer(e):
  Mx = np.zeros(e.shape)
  Tbx = np.zeros(e.shape)
  Mx[0,:]=e[0,:]
  Tbx[0,:]=0
  # print(e.shape[0])
  for i in range(1,e.shape[0]):
    xx=Mx[i-1,:]
    # print("xx",xx)
    xx_left=Mx[i-1,:]
    xx_left=np.delete(xx_left,0)
    xx_left=np.append(xx_left,np.inf)
    # print("xx_l",xx_left)
    xx_right=Mx[i-1,:]
    xx_right=np.append(xx_right,np.inf)
    xx_right=np.delete(xx_right,xx_right.shape[0]-1)
    xx_right=np.delete(xx_right,xx_right.shape[0]-1)
    xx_right=np.insert(xx_right,0,np.inf)
    # print("xx_r",xx_right)
    xx_comp=np.vstack((xx_right,xx,xx_left))
    # print(xx_comp)
    xx_min=np.min(xx_comp,axis=0)
    xx_ind=np.argmin(xx_comp,axis=0)
    xx_ind=xx_ind-1
    # print("xxmin",xx_min)
    # print("xxind",xx_ind)
    Mx[i,:]=e[i,:]+xx_min
    # print("Mxupdated",Mx[i,:])
    Tbx[i,:]=xx_ind
  return Mx, Tbx
