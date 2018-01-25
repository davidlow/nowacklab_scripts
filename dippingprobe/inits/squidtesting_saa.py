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

from Nowack_Lab.Procedures.mutual_inductance    import MutualInductance2
from Nowack_Lab.Procedures.mutual_inductance    import MutualInductance_sweep

from Nowack_Lab import set_experiment_data_path
set_experiment_data_path()

daq = NIDAQ(dev_name='Dev1')

daq.outputs = {
        'fieldcoil':3,
}
daq.inputs = {
        'dc':6
}

s = SquidArray()
preamp = SR5113(port='COM2')

instruments = {
        'daq':daq,
        'squidarray':s,
        'preamp':preamp
}
