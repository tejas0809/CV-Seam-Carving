'''
  File name: cumMinEngHor.py
  Author:
  Date created:
'''

'''
  File clarification:
    Computes the cumulative minimum energy over the horizontal seam directions.

    - INPUT e: n × m matrix representing the energy map.
    - OUTPUT My: n × m matrix representing the cumulative minimum energy map along horizontal direction.
    - OUTPUT Tby: n × m matrix representing the backtrack table along horizontal direction.
'''
import numpy as np


def cumMinEngHor(e):
  My = np.zeros(e.shape)
  Tby = np.zeros(e.shape)
  My[:,0]=e[:,0]
  Tby[:,0]=0
  # print(e.shape[0])
  for i in range(1,e.shape[1]):
    yy=My[:,i-1]
    # print("xx",xx)
    yy_up=My[:,i-1]
    yy_up=np.delete(yy_up,0)
    yy_up=np.append(yy_up,np.inf)
    # print("xx_l",xx_left)
    yy_down=My[:,i-1]
    yy_down=np.append(yy_down,np.inf)
    yy_down=np.delete(yy_down,yy_down.shape[0]-1)
    yy_down=np.delete(yy_down,yy_down.shape[0]-1)
    yy_down=np.insert(yy_down,0,np.inf)
    # print("xx_r",xx_right)
    yy_comp=np.vstack((yy_down,yy,yy_up))
    # print(xx_comp)
    yy_min=np.min(yy_comp,axis=0)
    yy_ind=np.argmin(yy_comp,axis=0)
    yy_ind=yy_ind-1
    # print("xxmin",xx_min)
    # print("xxind",xx_ind)
    My[:,i]=e[:,i]+yy_min
    # print("Mxupdated",Mx[i,:])
    Tby[:,i]=yy_ind
  return My, Tby
