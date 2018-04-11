import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib import pyplot as plt
plt.ion()
plt.style.use("notebook")
from Nowack_Lab.Instruments import nidaq, lockin, piezos, preamp, attocube, montana, squidarray
from Nowack_Lab.Procedures import planefit, touchdown

# Initialize DAQ and set input/output channels
daq = nidaq.NIDAQ()
daq.outputs = {
    'x':0,
    'y':1,
    'z':2
}
daq.inputs = {
    'cap':20,
    'theta':21,
    'capx':18,
    'capy':19,
    'acx':0,
    'acy':1,
    'dc':6
}

# Initialize other measurement equipment
#pa = preamp.SR5113(port="COM4")
liC = lockin.SR830(gpib_address=8)
liS = lockin.SR830(gpib_address=9)
pz = piezos.Piezos(daq)
montana = montana.Montana()
#atto = attocube.Attocube(montana)
s = squidarray.SquidArray.load()
# Create dictionary of instruments for measurements to use
instruments = {
    'daq':daq,
    'montana':montana,
    'piezos':pz,
    'lockin_cap':liC,
    #'atto': atto,
    #'preamp': pa,
    'lockin_squid': liS,
    'squidarray':s
    
}
