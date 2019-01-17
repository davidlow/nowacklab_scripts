from matplotlib import pyplot as plt
plt.ion()
import numpy as np
from importlib import reload

import Nowack_Lab.Instruments.nidaq
import Nowack_Lab.Instruments.squidarray
import Nowack_Lab.Instruments.preamp

from Nowack_Lab.Instruments.nidaq       import NIDAQ
from Nowack_Lab.Instruments.squidarray  import SquidArray
from Nowack_Lab.Instruments.preamp      import SR5113

import Nowack_Lab.Procedures.alexsave_arraytune
import Nowack_Lab.Procedures.alexsave_spectrum

from Nowack_Lab.Procedures.alexsave_arraytune import SQUID_Noise_Open_Loop
from Nowack_Lab.Procedures.alexsave_arraytune import SQUID_Noise_Closed_Loop
from Nowack_Lab.Procedures.alexsave_spectrum import DaqSpectrum

from Nowack_Lab import set_experiment_data_path
set_experiment_data_path()

daq = NIDAQ(dev_name='Dev1')

daq.outputs = {
        'fieldcoil':3,
        'test':1
}
daq.inputs = {
        'saa':5,
        'dc':6,
        'test':4
}

s = SquidArray.load()
preamp = SR5113(port='COM2')

instruments = {
        'daq':daq,
        'squidarray':s,
        'preamp':preamp
}

s.S_flux_lim=500
