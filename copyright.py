
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