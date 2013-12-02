import simpy
import random

# global class to total packets
class G:
	def __init__(self):
		self.DroppedPkts = 0
		self.TotalPkts = 0

# this class maintains
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
			self.G.TotalPkts += 1

	def remove(self):
		self.cur_size -= 1



def arrival(env, lambd, BQ):

	while True:
		lambd_time = random.expovariate(lambd)
		yield env.timeout(lambd_time)
		BQ.add()

def service(env, Mu, BQ):

	while True:
		# print("Doing something with packet number: {} at time: {}".format(BQ.cur_size, env.now))
		if(BQ.cur_size == 0):
			yield env.timeout(1)
		elif(BQ.cur_size > 0):
			BQ.remove()
			yield env.timeout(Mu)
		else:
			print("Error")


MU = 1
MAX_SIZE_DICT = [10, 50]
LAMBDA_DICT = [0.2, 0.4, 0.6, 0.8, 0.9, 0.99]
time = 0
interval = 100000


for max_size in MAX_SIZE_DICT:

	for lambd in LAMBDA_DICT:

		print("Begin Simulation")
		env = simpy.Environment()
		glob = G()
		BQ = Buffer_Queue(env, max_size, glob)

		env.process(service(env, MU, BQ))
		env.process(arrival(env, lambd, BQ))

		time += interval
		env.run(until=time)
		print("Lambda: {}  Buffer Size: {}".format(lambd, max_size))
		print("Total Packets: {} Dropped Packets: {} Pd = {}".format(glob.TotalPkts, glob.DroppedPkts, glob.DroppedPkts/float(glob.TotalPkts)))

# Sample Output

# Begin Simulation
# Lambda: 0.2  Buffer Size: 10
# Total Packets: 19916 Dropped Packets: 0 Pd = 0.0
# Begin Simulation
# Lambda: 0.4  Buffer Size: 10
# Total Packets: 79783 Dropped Packets: 0 Pd = 0.0
# Begin Simulation
# Lambda: 0.6  Buffer Size: 10
# Total Packets: 180167 Dropped Packets: 9 Pd = 4.99536541098e-05
# Begin Simulation
# Lambda: 0.8  Buffer Size: 10
# Total Packets: 319606 Dropped Packets: 877 Pd = 0.00274400355438
# Begin Simulation
# Lambda: 0.9  Buffer Size: 10
# Total Packets: 450717 Dropped Packets: 6973 Pd = 0.0154709052465
# Begin Simulation
# Lambda: 0.99  Buffer Size: 10
# Total Packets: 593424 Dropped Packets: 25683 Pd = 0.0432793415838
# Begin Simulation
# Lambda: 0.2  Buffer Size: 50
# Total Packets: 139997 Dropped Packets: 0 Pd = 0.0
# Begin Simulation
# Lambda: 0.4  Buffer Size: 50
# Total Packets: 321028 Dropped Packets: 0 Pd = 0.0
# Begin Simulation
# Lambda: 0.6  Buffer Size: 50
# Total Packets: 540587 Dropped Packets: 0 Pd = 0.0
# Begin Simulation
# Lambda: 0.8  Buffer Size: 50
# Total Packets: 799858 Dropped Packets: 0 Pd = 0.0
# Begin Simulation
# Lambda: 0.9  Buffer Size: 50
# Total Packets: 989538 Dropped Packets: 0 Pd = 0.0
# Begin Simulation
# Lambda: 0.99  Buffer Size: 50
# Total Packets: 1187216 Dropped Packets: 6547 Pd = 0.00551458201372
# [Finished in 56.2s]