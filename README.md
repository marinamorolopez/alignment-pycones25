# Prenatal genetic diagnosis with Python
Python application developed for the PyConES 2025 talk "Prenatal diagnosis of genetic diseases using Python".
This project demonstrates how Python can be used to compare DNA sequences and identify genetic variants associated with inherited diseases.

## Features
- Load reference and patient DNA sequences from FASTA files
- Compare DNA sequences base by base
- Detect genetic variants between reference and patient sequences
- Report mutation positions and nucleotide changes
- Generate a simple mutation report for downstream analysis

## Installation
You simply have to download the .py and fasta files (or get your own fasta files from a database as [NCBI](https://www.ncbi.nlm.nih.gov/)).

## Usage
Run the script and select:
1. The reference gene sequence.
2. The patient's DNA sequence.
The program compares both sequences and reports:
- Positions of detected variants
- Reference nucleotide
- Patient nucleotide

## Example
```
Reference sequence: COL7A1.fasta
Patient sequence: patient_sequence.fasta
```
Output
```
Position: 253
Reference: G
Patient: A
Position: 418
Reference: C
Patient: T
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
