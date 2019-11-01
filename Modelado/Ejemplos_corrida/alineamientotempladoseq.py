###########
# Align2D #
###########
from modeller import *

target='aln_pig_3v03'
template='3V03_A'

env = environ()
aln = alignment(env)
mdl = model(env, file="%s.pdb" % template, model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes=template, atom_files="%s.pdb" % template)
aln.append(file='%s.ali'%target, align_codes=target)
aln.align2d()
aln.write(file='%s-%s.ali' % (target,template), alignment_format='PIR')
aln.write(file='%s-%s.pap' % (target,template), alignment_format='PAP', alignment_features ="INDICES HELIX BETA")

