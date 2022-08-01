# PhotoLab.py: Image Processing Engine in Python/Piped to MATLAB

# Libraries
import os
import cv2


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
	pass

def sharpenPy(path):
	pass

def laplacianPy(path):
	pass
