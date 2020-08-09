
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