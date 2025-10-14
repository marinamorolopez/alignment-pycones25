# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 09:20:24 2024

@author: Marina Moro López
"""
    
from tkinter.filedialog import askopenfile

def read_sequence_from_file(prompt):
    print(prompt)
    file = askopenfile(mode='r')
    sequence = file.readlines()[1:]
    sequence = ''.join(sequence).replace('\n', '')
    return sequence

def align_sequences(gene_seq, patient_seq):
    alignment = [gene_seq[position] == patient_seq[position] for position in range(len(gene_seq))]
    return alignment

def get_mutation_positions(alignment):
    mutation_positions = [position for position, match in enumerate(alignment) if not match]
    return mutation_positions

def report_mutations(mutation_positions, gene_seq, patient_seq):
    for mutation in mutation_positions:
        print(f"Mutation position: {mutation + 1}")
        print(f"Original base: {gene_seq[mutation]}")
        print(f"Mutated base: {patient_seq[mutation]}")

def main():
    gene_seq = read_sequence_from_file('Please select the file with the gene of reference')
    patient_seq = read_sequence_from_file('Please select the file with the patient sequence')
    alignment = align_sequences(gene_seq, patient_seq)
    mutation_positions = get_mutation_positions(alignment)
    report_mutations(mutation_positions, gene_seq, patient_seq)

if __name__ == "__main__":
    main()


