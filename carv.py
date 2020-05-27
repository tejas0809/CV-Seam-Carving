'''
  File name: carv.py
  Author:
  Date created:
'''

'''
  File clarification:
    Aimed to handle finding seams of minimum energy, and seam removal, the algorithm
    shall tackle resizing images when it may be required to remove more than one seam,
    sequentially and potentially along different directions.

    - INPUT I: n × m × 3 matrix representing the input image.
    - INPUT nr: the numbers of rows to be removed from the image.
    - INPUT nc: the numbers of columns to be removed from the image.
    - OUTPUT Ic: (n − nr) × (m − nc) × 3 matrix representing the carved image.
    - OUTPUT T: (nr + 1) × (nc + 1) matrix representing the transport map.
'''
import numpy as np
from genEngMap import genEngMap
from cumMinEngVer import cumMinEngVer
from cumMinEngHor import cumMinEngHor
from rmVerSeam import rmVerSeam
from rmHorSeam import rmHorSeam
import imageio

def carv(I, nr, nc):
  # Your Code Here
  T=np.zeros((nr+1,nc+1))
  P=np.zeros((nr+1,nc+1))
  Imgcopy=np.copy(I)
  ImageArray=np.zeros((nc+1),dtype=object)
  T[0,0]=0
  P[0,0]=0
  ImageArray[0]=Imgcopy

  for j in range(1,nc+1):
    P[0,j]=0
    e=genEngMap(Imgcopy)
    Mx,Tbx=cumMinEngVer(e)
    Imgcopy,E=rmVerSeam(Imgcopy,Mx,Tbx)
    T[0,j]=T[0,j-1]+E
    ImageArray[j]=Imgcopy

  # print(ImageArray.shape)

  for i in range(1,nr+1):
    #print(i)
    ImgCopy=np.copy(ImageArray[0])
    e=genEngMap(ImgCopy)
    My,Tby=cumMinEngHor(e)
    ImgCopy,E=rmHorSeam(ImgCopy,My,Tby)
    ImageArray[0]=ImgCopy
    T[i,0]=T[i-1,0]+E
    P[i,0]=1
    for j in range(1,nc+1):
      # upar se
      ImgCopy1=np.copy(ImageArray[j])
      e1=genEngMap(ImgCopy1)
      My,Tby=cumMinEngHor(e1)
      ImgCopy1,E1=rmHorSeam(ImgCopy1,My,Tby)
      # left se
      ImgCopy2=np.copy(ImageArray[j-1])

      e2=genEngMap(ImgCopy2)
      Mx,Tbx=cumMinEngVer(e2)
      ImgCopy2,E2=rmVerSeam(ImgCopy2,Mx,Tbx)

      if((T[i,j-1]+E2)<(T[i-1,j]+E1)):
        T[i,j]=T[i,j-1]+E2
        P[i,j]=0
        ImageArray[j]=ImgCopy2
      else:
        T[i,j]=T[i-1,j]+E1
        P[i,j]=1
        ImageArray[j]=ImgCopy1
  # print(T)
  # print(P)

  np.pad(T,((1,0),(1,0)),'constant',constant_values=float('inf'))
  #------------------------------------------------------------------------------------
  # P=np.zeros((nr+1,nc+1))
  # ind_i=nr
  # ind_j=nc
  # # P[ind_i,ind_j]=1
  # while(True):
  #     # print("test")
  #     P[ind_i,ind_j]=1
  #     if(T[ind_i-1,ind_j]<T[ind_i,ind_j-1]):
  #         ind_i=ind_i-1
  #     else:
  #         ind_j=ind_j-1
  #     if(ind_i==0 and ind_j==0):
  #         break
  # # while(ind_i>0 and ind_j>0):
#--------------------------------------------------------------------------------------

  # for k in reversed(range(nr+nc-1)):
    # print(ind_i,ind_j)
    # print(ind_i-1,ind_j)
    # print(ind_j)

    # if(T[ind_i,ind_j-1])<=(T[ind_i-1,ind_j]):
    #   P[ind_i,ind_j-1]=1
    #   ind_j=ind_j-1
    # else:
    #   P[ind_i-1,ind_j]=1
    #   ind_i=ind_i-1


  # print(P)

  # indices=np.argwhere(P==1)
  # print(indices.shape)
  ImageList=[]
  ImageList.append(I)
  ImgCopy3=np.copy(I)

  indi=nr
  indj=nc
  # points=np.empty((0,2))
  points=np.empty((0,2))
  # print("ponits",points.shape)
  while (True):
      if(P[indi,indj]==1):
          indi=indi-1
          temp=np.array([indi,indj])
          temp=np.reshape(temp,(1,2))
          points=np.vstack((points,temp))
          # points=np.append(points,np.array([indi,indj]),1)
          # print(temp.shape)
          # points.append(np.array([indi,indj]))
      elif (P[indi,indj]==0):
          indj=indj-1
          temp=np.array([indi,indj])
          temp=np.reshape(temp,(1,2))
          points=np.vstack((points,temp))
          # points=np.append(points,np.array([indi,indj]),1)
          # points=np.vstack(np.array([indi,indj]))
          # print(np.array([indi,indj]))
      if indi==0 and indj==0:
          break


  # print("points shape",points.shape)
  # print("points",points)

  points=np.flip(points,axis=0)
  for i in range(points.shape[0]-1):
    # print("bye")
    if(points[i+1][0]>points[i][0]):
      e=genEngMap(ImgCopy3)
      My,Tby=cumMinEngHor(e)
      ImgCopy3,E=rmHorSeam(ImgCopy3,My,Tby)
      ImageList.append(ImgCopy3)
      # print("hi")
    elif (points[i+1][1]>points[i][1]):
      e=genEngMap(ImgCopy3)
      Mx,Tbx=cumMinEngVer(e)
      ImgCopy3,E=rmVerSeam(ImgCopy3,Mx,Tbx)
      ImageList.append(ImgCopy3)
      # print("hihi")

  #print(len(ImageList))
  print(len(ImageList))
  imageio.mimsave('carved_output.gif',ImageList,duration=0.05)
  Ic=ImgCopy3

  return  Ic,T
