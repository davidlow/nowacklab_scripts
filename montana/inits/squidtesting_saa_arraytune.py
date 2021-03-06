from matplotlib import pyplot as plt
plt.ion()
import numpy as np

import Nowack_Lab.Instruments.nidaq
import Nowack_Lab.Instruments.squidarray
import Nowack_Lab.Instruments.preamp

from Nowack_Lab.Instruments.nidaq       import NIDAQ
from Nowack_Lab.Instruments.squidarray  import SquidArray
from Nowack_Lab.Instruments.preamp      import SR5113

import Nowack_Lab.Procedures.mutual_inductance
import Nowack_Lab.Procedures.array_tune

from Nowack_Lab.Procedures.mutual_inductance    import MutualInductance2
from Nowack_Lab.Procedures.array_tune           import ArrayTune
from Nowack_Lab.Procedures.array_tune           import ArrayTuneBatch

from Nowack_Lab import set_experiment_data_path
set_experiment_data_path()

daq = NIDAQ()

daq.outputs = {
        'fieldcoil':3,
	'test':0
}
daq.inputs = {
        'saa':4,
        'dc':6,
        'test':3
}

s = SquidArray()
preamp = SR5113(port='COM4')

instruments = {
        'daq':daq,
        'squidarray':s,
        'preamp':preamp
}
