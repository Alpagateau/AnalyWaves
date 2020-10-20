import numpy as np
import wave
import struct
import matplotlib.pyplot as plt
import soundfile as sf

class Analyser:

	def __init__(self):
		self.data = []
		self.samplerate = 0
		self.path = ''

		self.w1 = [0,0]

	def Load(self, path):
		self.path = path
		self.data, self.samplerate = sf.read(path)

	def GetWaves(self):
		MAX = np.amax(self.data)
		freq = []
		for i in range(len(self.data)):
			if self.data[i] == MAX:
				freq += [i]
		dist = 0
		for i in range(len(freq)-1):
			if freq[i+1]-freq[i] == dist:
				continue
			else:
				dist = freq[i+1]-freq[i]
		self.w1 = [0, np.pi/(dist/self.samplerate)*2]
		return [freq,(dist/self.samplerate)]
