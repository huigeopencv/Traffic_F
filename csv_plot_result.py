'''
Author: jt 1723221731@qq.com
Date: 2023-04-10 15:33:11
LastEditors: jt 1723221731@qq.com
LastEditTime: 2023-06-29 16:14:03
FilePath: /flow_w/csv_plot_result.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='Times New Roman',size=13)
# # 2500veh/h
# r1=pd.read_csv("/home/jt/0712/Bottleneck_2500_speed_emission.csv")
# r2=pd.read_csv("/home/jt/0712/Litaxing_2500_first_0712/bottleneck_litaxin_1_speed_emission.csv")
# r5=pd.read_csv("/home/jt/0712/Litaxing_2500_first_0712/bottleneck_litaxin_2_speed_emission.csv")
# r6=pd.read_csv("/home/jt/0712/Litaxing_2500_first_0712/bottleneck_litaxin_3_speed_emission.csv")
# r7=pd.read_csv("/home/jt/0712/Litaxing_2500_first_0712/bottleneck_litaxin_4_speed_emission.csv")
#
# r3=pd.read_csv("/home/jt/0712/VSL_2500/Bottleneck_vsl_20230719-1347401689745660.8671057-0_speed_emission.csv")
# r4=pd.read_csv("/home/jt/0712/Lijixing_2500_first_0713/bottleneck_lijixing_2_speed_emission.csv")
# x = [i*0.2 for i in range(1501)]
# x1=[i for i in range(1501)]
# plt.plot(x, r1['m_speed'][0:1501])
# plt.plot(x, (r2['m_speed'][0:1501]+r5['m_speed'][0:1501]+r6['m_speed'][0:1501]+r7['m_speed'][0:1501])/4)
# plt.plot(x, r3['m_speed'][0:1501])
# plt.plot(x, r4['m_speed'][0:1501])
# plt.xlim([0,300])
# # ,prop={"family":"Times New Roman","size":12}
# plt.legend(['Uncontrol','DRL_Altruism','VSL','DRL_Egoism'],prop={"family":"Times New Roman","size":11})#利他性
# plt.xlabel("Time(s)",fontdict={"family":"Times New Roman","size":14})
# plt.ylabel("Average_speed(m/s)",fontdict={"family":"Times New Roman","size":14})
# print((sum((r2['m_speed'][0:1501]+r5['m_speed'][0:1501]+r6['m_speed'][0:1501]+r7['m_speed'][0:1501])/4)-sum(r1['m_speed'][0:1501]))/sum(r1['m_speed'][0:1501]))
# print((sum(r3['m_speed'][0:1501])-sum( r1['m_speed'][0:1501]))/sum( r1['m_speed'][0:1501]))
# # print((sum(r2['m_speed'][0:1501])-sum( r1['m_speed'][0:1501]))/sum( r2['m_speed'][0:1501]))
# plt.grid()
# plt.show()

# 3000veh/h
# r1=pd.read_csv("/home/jt/0712/Bottleneck_3000_speed_emission.csv")
# r2=pd.read_csv("/home/jt/0712/Litaxing_3000_first_0714/bottleneck_litaxing_5_speed_emission.csv")
# r3=pd.read_csv("/home/jt/0712/VSL_3000/Bottleneck_vsl_20230719-1453511689749631.0292222-0_speed_emission.csv")
# r4=pd.read_csv("/home/jt/0712/Lijixing_3000_first_0718/bottleneck_lijixing_1_speed_emission.csv")
# x = [i*0.2 for i in range(1501)]
# x1=[i for i in range(1501)]
# plt.plot(x, r1['m_speed'][0:1501])
# plt.plot(x, r2['m_speed'][0:1501])
# plt.plot(x, r3['m_speed'][0:1501])
# plt.plot(x, r4['m_speed'][0:1501])
# plt.xlim([0,300])
# # ,prop={"family":"Times New Roman","size":12}
# plt.legend(['Uncontrol','DRL_Altruism','VSL','DRL_Egoism'])#利他性
# plt.xlabel("Time(s)",fontdict={"family":"Times New Roman","size":14})
# plt.ylabel("Average_speed(m/s)",fontdict={"family":"Times New Roman","size":14})
# plt.grid()
# plt.show()

# r1=pd.read_csv("/home/jt/0712/Bottleneck_2500_speed_emission.csv")
#
# r4=pd.read_csv("/home/jt/0712/Lijixing_2500_first_0713/bottleneck_lijixing_2_speed_emission.csv")
# x = [i*0.2 for i in range(1501)]
# x1=[i for i in range(1501)]
# plt.plot(x, r1['m_speed'][0:1501])
#
# plt.plot(x, r4['m_speed'][0:1501])
# plt.xlim([0,300])
# # ,prop={"family":"Times New Roman","size":12}
# plt.legend(['Uncontrol','DRL_Egoism'],prop={"family":"Times New Roman"})#利他性
# plt.xlabel("Time(s)",fontdict={"family":"Times New Roman","size":14})
# plt.ylabel("Average_speed(m/s)",fontdict={"family":"Times New Roman","size":14})
#
# plt.grid()
# plt.show()

# 折扣率的奖励图
# r=pd.read_csv("/home/jt/ray_results/bottleneck/PPO_MergePOEnv-v0_0_2023-07-22_12-30-08frhgo53c/progress.csv")
# r1=pd.read_csv("/home/jt/0712/Discount_rate/PPO_MergePOEnv-v0_0_2023-07-24_09-43-31h0h66prb/progress.csv")
# r2=pd.read_csv("/home/jt/0712/Discount_rate/PPO_MergePOEnv-v0_0_2023-07-25_09-57-26xumd4v_0/progress.csv")
# r3=pd.read_csv("/home/jt/ray_results/bottleneck/PPO_MergePOEnv-v0_0_2023-08-19_11-08-055ku9o3go/progress.csv")
#
# rmean=r["episode_reward_mean"]
# r1mean=r1["episode_reward_mean"]
# r2mean=r2["episode_reward_mean"]
# r3mean=r3["episode_reward_mean"]
#
# x=[i for i in range(500)]
# x1=[i for i in range(714)]
# plt.plot(x, rmean[0:500])
# plt.plot(x, r1mean)
# plt.plot(x, r2mean)
# plt.plot(x1, r3mean)
#
# plt.xlim([0,500])
# plt.legend(['dr=0.999','dr=0.99','dr=0.9','20%'])#利他性
# plt.xlabel("Iterations",fontdict={"family":"Times New Roman","size":14})
# plt.ylabel("Total rewards",fontdict={"family":"Times New Roman","size":14})
# plt.grid()
# plt.show()

# 学习率的奖励图
# r=pd.read_csv("/home/jt/0712/Learning_rate/Lr_1e-3_dr_0999/progress.csv")
# r1=pd.read_csv("/home/jt/0712/Learning_rate/Lr_1e-4_dr_0999/progress.csv")
# r2=pd.read_csv("/home/jt/0712/Learning_rate/Lr_1e-5_dr_0999/progress.csv")
# rmean=r["episode_reward_mean"]
# r1mean=r1["episode_reward_mean"]
# r2mean=r2["episode_reward_mean"]
# x=[i for i in range(500)]
# x1=[i for i in range(500)]
# plt.plot(x, rmean[0:500])
# plt.plot(x, r1mean)
# plt.plot(x1, r2mean)
# plt.xlim([0,500])
# plt.legend(['lr=1e-5','lr=1e-4','lr=1e-3'])#利他性
# plt.xlabel("Iterations",fontdict={"family":"Times New Roman","size":14})
# plt.ylabel("Total rewards",fontdict={"family":"Times New Roman","size":14})
# plt.grid()
# plt.show()

# 2500veh/h 渗透率
r1=pd.read_csv("/home/jt/0712/Bottleneck_2500_speed_emission.csv")
r2=pd.read_csv("/home/jt/0712/bottleneck_20230822-1718481692695928.162701-0_speed_emission.csv")
# r3=pd.read_csv("/home/jt/0712/VSL_2500/Bottleneck_vsl_20230719-1347401689745660.8671057-0_speed_emission.csv")
# r4=pd.read_csv("/home/jt/0712/Lijixing_2500_first_0713/bottleneck_lijixing_2_speed_emission.csv")
x = [i*0.2 for i in range(1501)]
x1=[i for i in range(1501)]
plt.plot(x, r1['m_speed'][0:1501])
plt.plot(x, r2['m_speed'][0:1501])
# plt.plot(x, r3['m_speed'][0:1501])
# plt.plot(x, r4['m_speed'][0:1501])
plt.xlim([0,300])
print(sum(r1['m_speed'][0:1501]),sum(r2['m_speed'][0:1501]),(sum(r2['m_speed'][0:1501])-sum(r1['m_speed'][0:1501]))/sum(r1['m_speed'][0:1501]))
# ,prop={"family":"Times New Roman","size":12}
plt.legend(['10%','20%'],prop={"family":"Times New Roman","size":11})#利他性
plt.xlabel("Time(s)",fontdict={"family":"Times New Roman","size":14})
plt.ylabel("Average_speed(m/s)",fontdict={"family":"Times New Roman","size":14})

plt.grid()
plt.show()

