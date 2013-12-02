import simpy
from random import expovariate

def car(env):

	while True:
		print('Start parking at %d' % env.now)
		parking_duration = 5
		yield env.timeout(parking_duration)
		
		print('Start driving at %d' % env.now)
		trip_duration = 2
		yield env.timeout(trip_duration)




# The buffer class inherits from object base class
class Buffer_Queue(object):

	def __init__(self, env, lambd, bufferSize):
		self.env = env
		self.bufferSize = bufferSize
		self.proc = env.process(self.run(lambd))

	def run(self, lambd):
		while True:
			print('Time is %d' % env.now)

			if(self.bufferSize < 3):
				lambd_time = expovariate(lambd)
				yield env.timeout(lambd_time)
				self.bufferSize = self.bufferSize + 1
			else:
				print('Buffer full with %d packets' % self.bufferSize)
				yield env.timeout(1)






env = simpy.Environment()
theBuffer = Buffer_Queue(env, .2, 0)
env.run(until=30)

