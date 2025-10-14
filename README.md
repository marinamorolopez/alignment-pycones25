# alignment-pycones25
This repository includes the slides of the public presentation 'Diagnóstico prenatal de enfermedades genéticas usando Python' of PyConES 2025 and both the code and files used for the practical case.

## Installation
You simply have to download the .py and fasta files (or get your own fasta files from a database as [NCBI](https://www.ncbi.nlm.nih.gov/)).

## Usage
First you'll have to select the file of the original gene of interest. Then you'll have to select the file of the patient gene data. When finished running, the script will give you the positions of the mutations in the patient data compared to the original gene, and both the original DNA bases and the mutated ones in these positions.
If you want to recreate the example of the slides use the provided fasta file COL7A1 as the original gene and patient_sequence as the patient gene.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
