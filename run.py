import numpy as np
from PIL import Image
from carv import carv

inputR = np.array(Image.open("left.jpg").convert('RGB'))
carv(inputR,1,0)
