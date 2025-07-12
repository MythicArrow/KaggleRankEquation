import numpy as np
def formula(teammate,rank,teams,t):
  term1 = 1e+5 / np.sqrt(teammate)
  term2 = rank ** -0.75
  term3 = np.log10(1 + np.log10(teams))
  term4 = np.exp(-t / 500)
  term_list = [term1,term2,term3,term4]
  product = np.prod(term_list)
  return product
