import sys; sys.path.append('..')
import time
import numpy
import estimate

# config
min_iters_pow = 1
max_iters_pow = 5
precision = 50
nb_tries = 10

print('nb_iters,time,estimation')
for nb_iters in numpy.logspace(min_iters_pow, max_iters_pow, precision):
    nb_iters = int(nb_iters)
    for _ in range(nb_tries):
        init_time = time.time()
        estimated_pi = estimate.pi(nb_iters, 'pure_python')
        dt = time.time() - init_time
        print('%s,%s,%s' % (nb_iters, dt, estimated_pi))
        sys.stdout.flush()
