from modeller import *
e = environ()

target='pdb_70'

a = alignment(e, file='%s.fasta'%target, alignment_format='FASTA')
a.write(file='%s.ali'%target, alignment_format='PIR')

