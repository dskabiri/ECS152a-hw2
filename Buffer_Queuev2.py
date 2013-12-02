import simpy
import random

MAX_SIZE = 10
LAMBD = .2
MU = 1






env = simpy.Environment()
bufferQ = simpy.Resource(env, capacity = MAX_SIZE)