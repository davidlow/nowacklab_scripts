# nowacklab_scripts

Scripts used to setup measurements and initialize certain measurements.

Requires NowackLab code base.

# Organization:

Top level directory has folders defining which instrument you are on.  Second level directories are `inits` and `setups`.  `setups` 
imports all necessary packages, defines inputs and outputs of daq, defines instruments, etc.  `inits` are run to define a measurement
after a file in `setups` is run.

In `ipython`, the command I use to excecute either of these is `%run -i filename.py` or `%load filename.py` if you wish to edit it.
