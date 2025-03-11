import numpy as np

def cosine_similarity(arr1,arr2):
  dotProduct=np.dot(arr1,arr2)
  nomr1=np.linalg.norm(arr1)
  nomr2=np.linalg.norm(arr2)
  if norm1==0 or norm2==0:
    raise ValueError('Not correct input')
  return dotProduct/(norm1*norm2)
