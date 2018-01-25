import random

def wait_until_t(targetT, lakeshore, spread=.001, numsamples=20,
                 maxwaitbtwpts = 2):
    starttime = time.time()
    print("Waiting until T={0}".format(targetT))
    while (starttime + 1200 > time.time()):
        ts = []
        for i in range(numsamples):
            ts.append(lakeshore.T[6])
            time.sleep(maxwaitbtwpts*random.random())
        ts = np.array(ts)
        print('[Tmean, Tstd, Tmin, Tmax] = ' +
              '[{0:3.5f},{3:5.3f},{1:3.5f},{2:3.5f}]'.format(
            np.mean(ts), ts.min(), ts.max(), np.std(ts)))

        # If (target is within min/max and min/max close together) or
        #    (target is close to the mean value)
        if ( (targetT > ts.min() and targetT < ts.max()
                and abs(ts.min() - ts.max()) < 2*spread ) or
             (abs(targetT  - np.mean(ts)) < spread)        ):
            print("T={0:3.3f}, time_elapsed={1:3.3f}".format(
                lakeshore.T[6],
                time.time() - starttime
                ))
            break
        time.sleep(10)

class ntransport(Measurement):
    def __init__(self):
        super().__init__(instruments = {})
    def setup_plots(self):
        pass
    def plot(self):
        self.fig, self.ax = plt.subplots()
        self.ax.plot(self.ts, self.Rs)
        self.ax.set_ylabel('R (ohms)')
        self.ax.set_xlabel('Temperature (k)')
    def do(self):
        pass
    def run(self):
        self.plot()
        self.save()

iouts = np.linspace(-10e-6,10e-6,21)
ts = np.linspace(1.05,1.4,21)

Rs = []
name = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S_dctransport') 
try:
    for t in ts:
        l.pid_setpoint = t
        wait_until_t(t, l)
        v = VvsIdc(daqchannel=daq.ai6, instruments=instruments, iouts=iouts,
               dwelltime = .1)
        v.T = t
        v.run(save_appendedpath=name)
        Rs.append(v.R)
except:
    pass
n = ntransport()
n.ts = ts
n.Rs = Rs
n.run()
