mi = MutualInductance2(instruments = instruments,
                       Is         = np.linspace(-1e-3,1e-3,100),
                       Rbias      = 3165,
                       rate       = 100,
                       numsteps   = 1000,
                       conversion = 1/14.4)
