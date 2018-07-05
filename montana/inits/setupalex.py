import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib import pyplot as plt
plt.ion()
#plt.style.use("notebook")
from importlib import reload
import numpy as np

import Nowack_Lab.Instruments.nidaq
import Nowack_Lab.Instruments.squidarray
import Nowack_Lab.Instruments.preamp
import Nowack_Lab.Instruments.lockin
import Nowack_Lab.Instruments.piezos
import Nowack_Lab.Instruments.attocube
import Nowack_Lab.Instruments.montana
import Nowack_Lab.Instruments.squidarray

from Nowack_Lab.Instruments.nidaq       import NIDAQ
from Nowack_Lab.Instruments.squidarray  import SquidArray
from Nowack_Lab.Instruments.preamp      import SR5113
from Nowack_Lab.Instruments.lockin	import SR830
from Nowack_Lab.Instruments.piezos	import Piezos
from Nowack_Lab.Instruments.attocube	import Attocube
from Nowack_Lab.Instruments.montana	import Montana

import Nowack_Lab.Procedures.touchdown
import Nowack_Lab.Procedures.planefit
import Nowack_Lab.Procedures.daqspectrum
import Nowack_Lab.Procedures.mutual_inductance
import Nowack_Lab.Procedures.array_tune

from Nowack_Lab.Procedures.touchdown		import Touchdown
from Nowack_Lab.Procedures.planefit		import Planefit
from Nowack_Lab.Procedures.scanplane		import Scanplane
from Nowack_Lab.Procedures.daqspectrum		import DaqSpectrum
from Nowack_Lab.Procedures.daqspectrum		import SQUIDSpectrum
from Nowack_Lab.Procedures.mutual_inductance    import MutualInductance2
from Nowack_Lab.Procedures.array_tune           import ArrayTune
from Nowack_Lab.Procedures.array_tune           import BestLockPoint
from Nowack_Lab.Procedures.array_tune           import ArrayTuneBatch

from Nowack_Lab import set_experiment_data_path
set_experiment_data_path()

# Initialize DAQ and set input/output channels
daq = NIDAQ()
daq.outputs = {
    'x':0,
    'y':1,
    'z':2,
    'fieldcoil':3
}
daq.inputs = {
    'cap':20,
    'theta':21,
    'capx':18,
    'capy':19,
    'acx':0,
    'acy':1,
    'saa':5,
    'test':3,
    'dc':6
}

# Initialize other measurement equipment
pa = SR5113(port="COM4")
liC = SR830(gpib_address=8)
liS = SR830(gpib_address=9)
pz = Piezos(daq)
#montana = Montana()
atto = Attocube()
s = SquidArray.load()
#s = SquidArray()
# Create dictionary of instruments for measurements to use
instruments = {
    'daq':daq,
    'piezos':pz,
    'lockin_cap':liC,
    'atto': atto,
    'preamp': pa,
    'lockin_squid': liS,
    'squidarray':s
    
}
