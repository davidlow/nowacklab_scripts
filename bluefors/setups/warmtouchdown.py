### Setup script, modified from gmf57.  
###
###  +-----------------+
###  |  DO NOT MODIFY  |
###  +-----------------+
###
### Make a copy and rename with today's date
###
### Author: david low (dhl88)

from matplotlib import pyplot as plt
plt.ion()
#plt.style.use("notebook")

import Nowack_Lab.Instruments.lockin
import Nowack_Lab.Instruments.nidaq
import Nowack_Lab.Instruments.piezos


from Nowack_Lab.Instruments.lockin          import SR830
from Nowack_Lab.Instruments.nidaq           import NIDAQ
from Nowack_Lab.Instruments.piezos          import Piezos

import Nowack_Lab.Procedures.touchdown

from Nowack_Lab.Procedures.touchdown         import Touchdown


from Nowack_Lab import set_experiment_data_path
set_experiment_data_path()


# Initialize DAQ and set input/output channels
daq = NIDAQ(dev_name="Dev2")
daq.outputs = {
    'x':0,
    'y':1,
    'z':2
}
daq.inputs = {
    'cap':0,
    'theta':1, 
    'capx':2, # disconnected
    'capy':3, # disconnected
    'acx' :4,
    'acy' :5,
    'dc'  :6
}

# Initialize other measurement equipment
liC     = SR830(gpib_address=15)
pz      = Piezos(daq)

# Create dictionary of instruments for measurements to use
instruments = {
    'daq'           : daq,
    'piezos'        : pz,
    'lockin_cap'    : liC,
}
