from matplotlib import pyplot as plt
plt.ion()
import numpy as np

import Nowack_Lab.Instruments.nidaq

from Nowack_Lab.Instruments.nidaq       import NIDAQ

import Nowack_Lab.Procedures.geophones

from Nowack_Lab.Procedures.geophones            import Geophone_calibrate
from Nowack_Lab.Procedures.geophones            import Geophone_sr5113
from Nowack_Lab.Procedures.geophones            import GeophoneAccelerometer
from Nowack_Lab.Procedures.geophones            import Geophone

from Nowack_Lab import set_experiment_data_path
set_experiment_data_path()

daq = NIDAQ(dev_name='Dev1')

daq.outputs = {
        'out':2,
}
daq.inputs = {
        'inA':20,
        'inB':21,
}

#preamp = SR5113(port='COM2')

instruments = {
        'daq':daq,
}
