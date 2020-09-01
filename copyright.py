
import re
import pandas as pd
from ftfy import fix_text
import numpy as np
from scipy.sparse import csr_matrix
import sparse_dot_topn.sparse_dot_topn as ct

def CopyRight(data):

    def ngrams(string, n=3):
        string = fix_text(string)  # fix text encoding issues
        # remove non ascii chars
        string = string.encode("ascii", errors="ignore").decode()
        string = string.lower()  # make lower case
        chars_to_remove = [")", "(", ".", "|", "[", "]", "{", "}", "'"]
        rx = '[' + re.escape(''.join(chars_to_remove)) + ']'
        string = re.sub(rx, '', string)  # remove the list of chars defined above
        string = string.replace('&', 'and')
        string = string.replace(',', ' ')
        string = string.replace('-', ' ')
        string = string.replace('ToucheTohmatsu', ' ')
        string = string.title()  # normalise case - capital at start of each word
        # get rid of multiple spaces and replace with a single space
        string = re.sub(' +', ' ', string).strip()
        string = ' ' + string + ' '  # pad names for ngrams...
        string = re.sub(r'[,-./]|\sBD', r'', string)
        string = string.replace('Corp', ' ')
        string = string.replace('Corporation', ' ')
        string = string.replace('Holding', ' ')
        string = string.replace('Holdings', ' ')
        string = string.replace('Ltd', ' ')
        string = string.replace('LTD', ' ')
        string = string.replace('LLC', ' ')
        string = string.replace('LLP', ' ')
        string = string.replace('Co', ' ')
        string = string.replace('Company', ' ')
        string = string.replace('US', ' ')
        string = string.replace('United States', ' ')
        string = string.replace('International', ' ')
        string = string.replace('Inc', ' ')
        string = string.replace('AB', ' ')
        string = string.replace('SAB', ' ')
        string = string.replace('PJSC', ' ')
        string = string.replace('AG', ' ')
        string = string.replace('AG & Co', ' ')
        string = string.replace('Oyj', ' ')
        string = string.replace('A/S', ' ')
        string = string.replace('Public Co', ' ')
        string = string.replace('Incorporated', ' ')
        string = string.replace('Plc', ' ')
        string = string.replace('S.A.', ' ')
        string = string.replace('SA', ' ')
        string = string.replace('AG', ' ')
        string = string.replace('NV', ' ')
        string = string.replace('ToucheTohmatsu', ' ')
        string = string.replace('Companies', ' ')
        ngrams = zip(*[string[i:] for i in range(n)])
        return [''.join(ngram) for ngram in ngrams]

    from sklearn.feature_extraction.text import TfidfVectorizer
    clean_org_names = pd.read_excel(