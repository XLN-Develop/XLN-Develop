
from pathlib import Path
import random
import sys
import xlnseq_fasta

#----------------------------------------------------------------------
# FUNCTIONS
#----------------------------------------------------------------------

def create_60bp_sequence() -> str:
    '''Creates a random DNA sequence of 60bp, and return it as a fasta structure'''

    header:             str         = '> Sequence of '
    nucleotides_type:   list[str]   = ["A","T","C","G"]
    seq_60bp:           str         = ''

    for _ in range (60):
        nucleotide: str = random.choice(nucleotides_type)
        seq_60bp        = seq_60bp + nucleotide
    
    seq_60bp_fa:    str = xlnseq_fasta.create_dna_rna_fasta_string(header, seq_60bp)

    assert (seq_60bp_fa != '') 

    return seq_60bp_fa

#----------------------------------------------------------------------

def create_120bp_sequence() -> str:
    '''Creates a random DNA sequence of 120bp, and return it as a fasta structure'''

    header: str = '> Sequence of '

    first_seq_fa:   str = create_60bp_sequence()
    second_seq_fa:  str = create_60bp_sequence()

    first_seq:      str = xlnseq_fasta.extract_only_sequence_from_fasta(first_seq_fa)
    second_seq:     str = xlnseq_fasta.extract_only_sequence_from_fasta(second_seq_fa)

    seq_120bp:      str = f'{first_seq}{second_seq}'
    seq_120bp_fa:   str = xlnseq_fasta.create_dna_rna_fasta_string(header, seq_120bp)

    return seq_120bp_fa

#----------------------------------------------------------------------

def create_180bp_sequence() -> str:
    '''Creates a random DNA sequence of 180bp, and return it as a fasta structure'''

    header:     str = '> Sequence of '
    seq_180bp:  str = f''

    for _ in range(3):
        random_seq_fa:      str = create_60bp_sequence()
        random_seq_string:  str = xlnseq_fasta.extract_only_sequence_from_fasta(random_seq_fa)
        seq_180bp               = seq_180bp + random_seq_string
    
    seq_180bp_fa: str = xlnseq_fasta.create_dna_rna_fasta_string(header, seq_180bp)

    return seq_180bp_fa

#----------------------------------------------------------------------

def create_600bp_sequence() -> str:
    '''Creates a random DNA sequence of 600bp, and return it as a fasta structure'''

    header:     str = '> Sequence of '
    seq_600bp:  str = f''

    for _ in range(10):
        random_seq_fa:      str = create_60bp_sequence()
        random_seq_string:  str = xlnseq_fasta.extract_only_sequence_from_fasta(random_seq_fa)
        seq_600bp               = seq_600bp + random_seq_string
    
    seq_600bp_fa: str = xlnseq_fasta.create_dna_rna_fasta_string(header, seq_600bp)
    return seq_600bp_fa

#----------------------------------------------------------------------

def create_6000bp_sequence() -> str:
    '''Creates a random DNA sequence of 6000bp, and return it as a fasta structure'''

    header:      str = '> Sequence of '
    seq_6000bp:  str = f''

    for _ in range(100):
        random_seq_fa:      str = create_60bp_sequence()
        random_seq_string:  str = xlnseq_fasta.extract_only_sequence_from_fasta(random_seq_fa)
        seq_6000bp              = seq_6000bp + random_seq_string

    seq_6000bp_fa: str = xlnseq_fasta.create_dna_rna_fasta_string(header, seq_6000bp)
    
    return seq_6000bp_fa

#----------------------------------------------------------------------

def user_seq(number_of_lines: int) -> str:
    '''Creates a random DNA sequence of specified (from user) lines of 
    60bp each, and return it as a fasta structure'''

    header:             str = '> Sequence of '
    user_seq_string:    str = f''

    for _ in range(number_of_lines):
        random_seq_fa:      str = create_60bp_sequence()
        random_seq_string:  str = xlnseq_fasta.extract_only_sequence_from_fasta(random_seq_fa)
        user_seq_string         = user_seq_string + random_seq_string
    
    user_seq_fa:        str = xlnseq_fasta.create_dna_rna_fasta_string(header, user_seq_string)

    return user_seq_fa
    
#----------------------------------------------------------------------
# MAIN
#----------------------------------------------------------------------

# FOR EASY DEBUGGING:
#if __name__ == "__main__":

    # Create random sequences of different size:
    #sequence_60bp:          str         = create_60bp_sequence()
    #sequence_120bp:         str         = create_120bp_sequence()
    #sequence_180bp:         str         = create_180bp_sequence()
    #sequence_600bp:         str         = create_600bp_sequence()
    #sequence_6000bp:        str         = create_6000bp_sequence()

    # For debug the user_seq() function
    # Create random sequence depending of the parameter (number of lines
    # of 60bp) is passed trought the command-line:
    #args:                   list[str]   = sys.argv              # For command-line
    #args:                   list[str]   = [sys.argv[0], "4"]   # For easy-testing
    #amount_lines_of_60bp:   int         = int(args[1])
    #user_sequence:          str         = users_seq(amount_lines_of_60bp)

    # For easy debbuging:
    #print (sequence_60bp)
    #print (sequence_120bp)   
    #print (sequence_180bp)
    #print (sequence_600bp)
    #print (sequence_6000bp)
    #print(user_sequence)

