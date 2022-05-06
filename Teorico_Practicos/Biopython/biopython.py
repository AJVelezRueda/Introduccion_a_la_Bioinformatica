from Bio import Align

aligner = Align.PairwiseAligner()
aligner.mode = 'local'
alignments = aligner.align("TACCG", "ACGG")
for alignment in sorted(alignments):
    print("Score = %.1f:" % alignment.score)
    print(alignment)

###Adding a mismatch score
aligner.mismatch_score = -10
alignments = aligner.align("AAACAAA", "AAAGAAA")
print(len(alignments))
print(alignments[1])

aligner.mismatch_score = -1
alignments = aligner.align("AAACAAA", "AAAGAAA")
print(len(alignments))
print(alignments[1])

