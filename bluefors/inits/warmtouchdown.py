td = Touchdown(instruments, planescan=True)
td.z_piezo_step = 0.4
td.Vz_max = 40
td._init_arrays()
print(td.V)