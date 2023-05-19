# PhotoLab.py: Image Processing Engine in Python/Piped to MATLAB
# Author: Timothy Do

# Libraries
import os
import cv2
import numpy as np
from matplotlib.pylab import cm


# Matlab Engine Functions 

def fftMat(path):
	os.chdir('./matlab')
	os.system('matlab -nodesktop -nosplash -batch "fftFile \'' + path + '\'"')
	os.chdir('..')

def sharpenMat(path):
	os.chdir('./matlab')
	os.system('matlab -nodesktop -nosplash -batch "sharpenFile \'' + path + '\'"')
	os.chdir('..')

def laplacianMat(path):
	os.chdir('./matlab')
	os.system('matlab -nodesktop -nosplash -batch "laplacianFile \'' + path + '\'"')
	os.chdir('..')

# Python Engine Functions

def fftPy(path): 
	image = cv2.imread(path)
	fft = np.fft.fft2(image)
	fftShift = np.fft.fftshift(fft)
	mag = 20*np.log(np.abs(fftShift))
	mag = np.uint8(mag/(mag.max()/255.0))
	mag = cv2.cvtColor(mag,cv2.COLOR_RGB2GRAY)
	mag = mag/(mag.max()/255.0)
	cv2.imwrite(path,mag)

def sharpenPy(path):
	image = cv2.imread(path)
	kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
	cv2.imwrite(path,cv2.filter2D(image,-1,kernel))

def laplacianPy(path):
	image = cv2.imread(path)
	kernel = np.array([[1,1,1], [1,-8,1], [1,1,1]])
	cv2.imwrite(path,cv2.filter2D(image,-1,kernel))

#Upscayl Functions
def upscayl(path):
	original = os.getcwd()
	os.chdir("C:\\Program Files\\Upscayl\\resources\\bin")
	os.system(f"upscayl-realesrgan.exe -i \"{path}\" -o \"{path}\" -s 4 -m ..\\models -n realesrgan-x4plus-anime")
	os.chdir(original)
	
if __name__ == '__main__':
	print('PhotoLab Can\'t be Run Individually 😂')