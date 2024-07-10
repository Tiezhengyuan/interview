
import numpy as np
from scipy import stats

def task(df1):
  print(df1.shape)
  day1 = df1.loc[df1.day==1, 'analyte_value']
  mean_day1 = np.mean(day1)
  day8 = df1.loc[df1.day==8, 'analyte_value']
  mean_day8 = np.mean(day8)
  
  t_res = stats.ttest_ind(day1, day8)
  ci= t_res.confidence_interval(0.05)
  res = {
    # 'marker': marker,
    'CI': f"{ci.low:4f}-{ci.high:4f}",
    'pvalue': t_res.pvalue
  }
  return res
