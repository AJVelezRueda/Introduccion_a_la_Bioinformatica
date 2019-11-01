# Homology modeling with multiple templates
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the automodel class
 
log.verbose()    # request verbose output
env = environ()  # create a new MODELLER environment to build this model in
 
# directories for input atom files
env.io.atom_files_directory = './:../atom_files'
env.io.hetatm = True
 
 
a = automodel(env,
             alnfile  = 'aln_rat_3v03.pir', # alignment filename
             knowns   = ('3V03'),     # codes of the templates
             sequence = 'NM_134326')               # code of the target
a.starting_model= 1                 # index of the first model
a.ending_model  = 100                 # index of the last model
                                   # (determines how many models to calculate)
a.make()                            # do the actual homology modeling

