import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib


DF = pd.read_csv('temp_work_net_bigdata.csv', encoding= 'utf-8')
# 모집 직종의 요소 개수를 구하여 그래프로 표현
print(DF['모집직종'].value_counts())
print(DF['모집직종'].value_counts())
# csv로 저장
DF['모집직종'].value_counts().to_csv('temp_work_net_bigdata_counts.csv', encoding='utf-8', index=True)

# plt.plot(DF['모집직종'], DF['모집직종'].value_counts())
# plt.show()