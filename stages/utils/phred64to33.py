#!/usr/bin/env python

#base quality conversion Phred64 to Phred33 scale
#used as: samtools view -Sh old.bam | SVE/stages/utils/phred64to33.py | samtools view -Sb - > ./phred33.bam
import sys

for line in sys.stdin:
    if line.startswith('@'): #header
        print line,
    else:                    #alignments
        raw  = line.split('\t')
        base_qual = ''.join([chr(ord(i)-31) for i in raw[10]])
        if len(raw)>10:
            print '\t'.join(raw[:10]+[base_qual]+raw[11:]),
        else:
            print '\t'.join(raw[:10]+[base_qual]),
            
