import sys
import csv
import statistics
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print('Bench file required')
    sys.exit(1)

# read data
benchs = {}
print('reading data')
with open(sys.argv[1], 'r') as fp: # read input file
    reader = csv.reader(fp)
    next(reader) # ignore header
    for line in reader:
        try:
            nb_iters, time, error = line
            nb_iters, time, error = int(nb_iters), float(time), float(error)
            benchs.setdefault(nb_iters, [[], []])
            benchs[nb_iters][0].append(time)
            benchs[nb_iters][1].append(error)
        except ValueError:
            print('ignored line %s, bad format' % line)

# plot data
print('plotting data')
xs, time_ys, error_ys = [], [], []
for nb_iters in benchs:
    xs.append(nb_iters)
    times, errors = benchs[nb_iters]
    time_ys.append(statistics.mean(times))
    error_ys.append(statistics.mean(errors))
plt.plot(xs, time_ys); plt.show()
plt.plot(xs, error_ys); plt.show()
