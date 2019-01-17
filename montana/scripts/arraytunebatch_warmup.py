sbias = np.linspace(40,1000,61)
aflux = np.linspace(-.6,.6,11)
atb = ArrayTuneBatch(instruments=instruments, sbias=sbias, 
			aflux=aflux, sbias_ex=100, 
			save_appendedpath='2018-04-06_2340', 
			conversion=.6718)

try: 
	atb.run()
except:
	pass
s.zero()
daq.zero()
montana.warmup()
