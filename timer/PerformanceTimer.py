import time


class PerformanceTimer:
    timers = {}

    def __init__(self, name: str = "", iterations: int = 5):
        self.running = False
        self.start = None
        self.name = name
        self.elapsed = 0.0
        self.measurements = []
        self.iterations = iterations

        PerformanceTimer.timers[self.name] = self

    def measure_function(self, func, *kwargs):
        for i in range(self.iterations):
            self.start_timer()
            func(*kwargs)
            self.stop_timer()
            self.measurements.append(self.elapsed)
            self.reset()

    def start_timer(self):
        if self.running is False:
            self.start = time.perf_counter()
            self.running = True
        else:
            raise Exception('Timer already started.')

    def stop_timer(self):
        if self.running is True:
            self.elapsed = time.perf_counter() - self.start
            self.running = False
        else:
            raise Exception('Timer is not running.')

    def reset(self):
        self.start = None
        self.elapsed = 0.0
        self.running = False

    def average_time(self):
        return sum(self.measurements) / len(self.measurements)

    def print(self):
        print(('Timer: ' + self.name).center(50, '-'))
        print('Running: ' + str(self.running))

        if self.measurements:
            print('Measured Times: ' + str(self.measurements))
            print('Average: ' + str(self.average_time()))
        else:
            print('Elapsed Time: ' + str(self.elapsed))

        print('\n')
