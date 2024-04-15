def make_data(student_id):
  from random import seed
  from random import random
  import numpy as np
  seed(student_id)

  num = random()

  import pandas as pd

  df = pd.read_csv('https://raw.githubusercontent.com/flowonthegoliv/ENVS231_2022/main/data.csv')
  datetime = np.array(pd.to_datetime(df.tmp2))
  tmp = list(str(num))
  tmp = list(dict.fromkeys(tmp[2::]))

  dat1 = np.array(df.iloc[:,int(tmp[0])+1])
  dat2 = np.array(df.iloc[:,int(tmp[1])+1])
  dat3 = np.array(df.iloc[:,int(tmp[2])+1])

  return datetime, dat1, dat2, dat3