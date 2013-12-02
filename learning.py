import simpy
from random import expovariate




# The buffer class inherits from object base class
class Buffer_Queue(object):

	# constructor
	def __init__(self, env, lambd, maxBuffer):
		self.env = env
		self.cur_Buffer = 0
		self.max = maxBuffer
		self.proc = env.process(self.run(lambd))

	# basic run method
	def run(self, lambd):
		while True:
			print('Time is %d' % env.now)

			if(self.cur_Buffer < self.max):
				lambd_time = expovariate(lambd)
				yield env.timeout(lambd_time)
				self.cur_Buffer = self.cur_Buffer + 1
			else:
				print('Buffer full with %d packets' % self.cur_Buffer)
				yield env.timeout(0)
				self.cur_Buffer = self.cur_Buffer - 1


class Arrival(Process):

	def __init__(self, env, maxBuffer):
		self.env = env
		self.max = maxBuffer





# for testing purposes
env = simpy.Environment()
theBuffer = Buffer_Queue(env, .2, 3)
env.run(until=30)

