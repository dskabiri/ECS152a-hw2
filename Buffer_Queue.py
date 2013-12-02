import simpy
import random


class Buffer_Queue(object):

	def __init__(self, env, maxSize):
		self.env = env
		self.maxSize = maxSize
		self.cur_size = 0

	def add(self):

		if(self.cur_size == 0):
			self.cur_size += 1
		elif(self.cur_size < self.maxSize):
			self.cur_size += 1
		else:
			print("Buffer Full")

	def remove(self):
		self.cur_size -= 1



def arrival(env, lambd, BQ):

	while True:
		lambd_time = random.expovariate(lambd)
		yield env.timeout(lambd_time)
		BQ.add()


def service(env, Mu, BQ):

	while True:
		if(BQ.cur_size != 0):
			yield env.timeout(Mu)
			BQ.remove()
		else:
			yield env.timeout(1)



MAX_SIZE = 10
LAMBD = .99
MU = 1

print("Begin Simulation")
random.seed(10)
env = simpy.Environment()
BQ = Buffer_Queue(env, MAX_SIZE)

env.process(service(env, MU, BQ))
env.process(arrival(env, LAMBD, BQ))


env.run(until=1000)
