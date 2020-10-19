import numpy as np

def  MVT(t):
	return (ValueAtTime(0, 0.5, t) * ValueAtTime(0.2, 2, t) * ValueAtTime(0.2, 2, t) * ValueAtTime(2, 0.3, t)) 

def ValueAtTime(a,b,t):
	return np.sin((t+a)*b)