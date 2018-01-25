from matplotlib import pyplot as plt
plt.ion()
import numpy as np

import Nowack_Lab.Instruments.nidaq
import Nowack_Lab.Instruments.preamp

from Nowack_Lab.Instruments.nidaq       import NIDAQ
from Nowack_Lab.Instruments.preamp      import SR5113
from Nowack_Lab.Instruments.preamp      import FakeSR5113

import Nowack_Lab.Procedures.squidIV2

from Nowack_Lab.Procedures.squidIV2     import SQUID_IV
from Nowack_Lab.Procedures.squidIV2     import SQUID_Mod
from Nowack_Lab.Procedures.squidIV2     import SQUID_FCIV
from Nowack_Lab.Procedures.squidIV2     import SQUID_FC

from Nowack_Lab import set_experiment_data_path
set_experiment_data_path()

daq = NIDAQ(dev_name='Dev1')

daq.outputs = {
        'iv':0,
        'mod':1,
        'fc':3
}
daq.inputs = {
        'iv':6
}

instruments = {
        'daq':daq,
}
