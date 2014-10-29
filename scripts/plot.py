import sys
import csv
import math
from statistics import mean as avg
from collections import OrderedDict
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print('Bench file required')
    sys.exit(1)

# read data
benchs = OrderedDict()
with open(sys.argv[1], 'r') as fp: # read input file
    reader = csv.reader(fp)
    next(reader) # ignore header
    for line in reader:
        try:
            nb_iters, time, estimation = line
            nb_iters, time, estimation = int(nb_iters), float(time), float(estimation)
            bench = benchs.setdefault(nb_iters, {
                'estimations': [],
                'times': []
                })
            bench['estimations'].append(estimation)
            bench['times'].append(time)
        except ValueError:
            print('ignored line %s, bad format' % line)

# plot data
m, n = 1, 1
xs = list(benchs.keys())
plt.xlabel('Number of iterations')

# all estimations
sp1 = plt.subplot(m, n, 1)
sp1.set_xscale('log')
for x, b in benchs.items():
    sp1.scatter([x] * len(b['estimations']), b['estimations'], c='r')
sp1.set_ylabel('All estimations', color='r')

# math.pi horizontal line
sp1.axhline(y=math.pi, c='y')

# average time
sp2 = sp1.twinx()
sp2.plot(xs, [avg(b['times']) for b in benchs.values()], c='b')
sp2.set_ylabel('Average runtime (s)', color='b')

plt.show()
