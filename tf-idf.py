import numpy as np
def tfidf(mat, rownames=None):
    """TF-IDF 
    
    Parameters
    ----------
    mat : 2d np.array
       The matrix to operate on.
       
    rownames : list of str or None
        Not used; it's an argument only for consistency with other methods 
        defined here.
        
    Returns
    -------
    (np.array, list of str)    
       The first member is the TF-IDF-transformed version of `mat`, and 
       the second member is `rownames` (unchanged).
    
    """
    colsums = np.sum(mat, axis=0)
    doccount = mat.shape[1]
    w = np.array([_tfidf_row_func(row, colsums, doccount) for row in mat])
    return (w, rownames)

def _tfidf_row_func(row, colsums, doccount):
    df = float(len([x for x in row if x > 0]))
    idf = 0.0
    # This ensures a defined IDF value >= 0.0:
    if df > 0.0 and df != doccount:
        idf = np.log(doccount / df)
    tfs = row/colsums
    return tfs * idf
