import simpy
import random

class G:
	DroppedPkts = 0
	TotalPkts = 0


class Buffer_Queue(object):

	def __init__(self, env, maxSize, G):
		self.env = env
		self.maxSize = maxSize
		self.cur_size = 0
		self.G = G

	def add(self):

		if(self.cur_size < self.maxSize):
			self.cur_size += 1
			self.G.TotalPkts += 1
		else:
			self.G.DroppedPkts += 1

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
# random.seed(10)
env = simpy.Environment()
G = G()
BQ = Buffer_Queue(env, MAX_SIZE, G)

env.process(service(env, MU, BQ))
env.process(arrival(env, LAMBD, BQ))


env.run(until=1000000)
print("Total Packets: {} Dropped Packets: {} Pd = {}".format(G.TotalPkts, G.DroppedPkts, G.DroppedPkts/float(G.TotalPkts)))
