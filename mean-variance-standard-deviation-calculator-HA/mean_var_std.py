import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  
  a = np.array(list).reshape(3,3)
  calculations = {
    "mean": [np.mean(a, axis=0).tolist(),np.mean(a, axis=1).tolist(),a.mean().tolist()],
    "variance": [np.var(a, axis=0).tolist(),np.var(a, axis=1).tolist(),a.var().tolist()],
    "standard deviation": [np.std(a, axis=0).tolist(),np.std(a, axis=1).tolist(),a.std().tolist()],
    "max": [np.max(a, axis=0).tolist(),np.max(a, axis=1).tolist(),a.max().tolist()],
    "min": [np.min(a, axis=0).tolist(),np.min(a, axis=1).tolist(),a.min().tolist()],
    "sum": [np.sum(a, axis=0).tolist(),np.sum(a, axis=1).tolist(),a.sum().tolist()]}
  return calculations