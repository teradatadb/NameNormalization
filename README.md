# NameNormalization
Natural Language Processing tool for standardizing company names to a standard form.

# Introduction
This project aims to standardize a list of similar company names (for example: JPMC, JPMorgan, J.P.Morgan Chase) to their standard form (e.g., JPMorgan Chase & Co.). Traditional string matching approaches like Levenshtein Distance may be slow, hence NLP is utilized for efficiency.

# Installation
1. Clone or download this repository.
2. Run pip install -r requirements.txt inside this repository. Consider this inside a Python virtual environment.
3. The 'data.xlsx' file, included in this repository, contains a list of standard company names for matching.
4. Use `streamlit run app.py` to start the application.

As it operates, the tool maps individual or multiple company names to the corresponding standard name. If a company name is not included in the list, it can be manually added to achieve continuous optimization.

# References
Links to related resources and references are provided:
1. [Super Fast String Matching](https://bergvca.github.io/2017/10/14/super-fast-string-matching.html)
2. [sparse_dot_topn](https://github.com/ing-bank/sparse_dot_topn)
3. [Boosting the selection of the most similar entities in large scale datasets](https://medium.com/wbaa/https-medium-com-ingwbaa-boosting-selection-of-the-most-similar-