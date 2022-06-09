# NameNormalization
Natural Language Processing tool for standardizing company names to a standard form.

# Introduction
This project aims to standardize a list of similar company names (for example: JPMC, JPMorgan, J.P.Morgan Chase) to their standard form (e.g., JPMorgan Chase & Co.). Traditional string matching approaches like Levenshtein Distance may be slow, hence NLP is utilized for efficiency.

# Installation
1. Clone or download this repository.
2. Run pip install -r requirements.txt inside this repository. Consider this inside a Python virtual environment.
3. The 'data.xlsx' file, included in this repository, contains a list of standard company names for matching.
4. Use `strea