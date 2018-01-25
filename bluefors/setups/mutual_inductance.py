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

#import Nowack_Lab.Instruments.lockin
import Nowack_Lab.Instruments.nidaq
#import Nowack_Lab.Instruments.piezos
#import Nowack_Lab.Instruments.attocube
import Nowack_Lab.Instruments.preamp
import Nowack_Lab.Instruments.squidarray


#from Nowack_Lab.Instruments.lockin          import SR830
from Nowack_Lab.Instruments.nidaq           import NIDAQ
#from Nowack_Lab.Instruments.piezos          import Piezos
#from Nowack_Lab.Instruments.attocube        import Attocube
from Nowack_Lab.Instruments.preamp          import SR5113
from Nowack_Lab.Instruments.squidarray      import SquidArray

#import Nowack_Lab.Procedures.touchdown
#import Nowack_Lab.Procedures.planefit
#import Nowack_Lab.Procedures.scanplane
import Nowack_Lab.Procedures.daqspectrum
import Nowack_Lab.Procedures.mutual_inductance

#from Nowack_Lab.Procedures.touchdown         import Touchdown
#from Nowack_Lab.Procedures.planefit          import Planefit
#from Nowack_Lab.Procedures.scanplane         import Scanplane
from Nowack_Lab.Procedures.mutual_inductance import MutualInductance2
from Nowack_Lab.Procedures.daqspectrum       import SQUIDSpectrum


from Nowack_Lab import set_experiment_data_path
set_experiment_data_path()


# Initialize DAQ and set input/output channels
daq = NIDAQ(dev_name="Dev2")
daq.outputs = {
    'x':0,
    'y':1,
    'z':2,
    'fieldcoil':3
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
pa      = SR5113(port='COM2')
#liC     = SR830(gpib_address=15)
#liS     = SR830(gpib_address=12)
#pz      = Piezos(daq)
#atto    = Attocube()
s       = SquidArray.load(visaResource='COM1')

# Create dictionary of instruments for measurements to use
instruments = {
    'preamp'        : pa,
    'daq'           : daq,
#    'piezos'        : pz,
#    'lockin_cap'    : liC,
#    'lockin_squid'  : liS,
    'squidarray'    : s,
#    'atto'          : atto
}
