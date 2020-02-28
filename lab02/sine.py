"""
This module implements local search on a simple sine function variant. \

edited by Hamin Hong

"""
import math
import time
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange


class Sine(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions)
    """

    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        return math.fabs(x * math.sin(x))


if __name__ == '__main__':

    maximum = 30
    restartCount = 100
    maxValue = 0.0
    totalValAn = 0.0
    anMaxVal = 0.0
    MaxValHill = 0.0
    maxVal = 0.0
    initialVal = 0.0
    hillT = 0.0
    annealT = 0.0
    timeInit = 0.0

    for i in range(restartCount):

        initial = randrange(0, maximum)
        time1 = time.time()
        p = Sine(initial, maximum, delta=1)
        time2 = time.time()
        initialVal += p.value(initial)
        timeInit += (time2 - time1)
        if maxVal < p.value(initial):
            maxVal = p.value(initial)

        time1 = time.time()
        hill_solution = hill_climbing(p)
        time2 = time.time()
        MaxValHill += p.value(hill_solution)
        hillT += (time2 - time1)
        if maxValue < p.value(hill_solution):
            maxValue = p.value(hill_solution)

        time1 = time.time()
        ASolution = simulated_annealing(p, exp_schedule(k=20, lam=0.005, limit=1000))
        time2 = time.time()
        totalValAn += p.value(ASolution)
        annealT += (time2 - time1)
        if anMaxVal < p.value(ASolution):
            anMaxVal = p.value(ASolution)

    print('Initial:  max : %0.3f' % p.initial + '\t average : %0.3f' % (initialVal / restartCount)
          + "\t\ttime: %0.3f seconds" % timeInit )

    print('Hill-climbing solution: \t max : %0.3f' % maxValue
          + '\taverage : %0.3f' % (MaxValHill / restartCount) + "\t\ttime: %0.3f seconds" % hillT)

    print('Simulated annealing solution max : %0.3f' % anMaxVal
          + '\taverage : %0.3f' % (totalValAn / restartCount) + "\t\ttime: %0.3f seconds" % annealT)
