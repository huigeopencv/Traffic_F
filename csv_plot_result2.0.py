# '''
# Author: jt 1723221731@qq.com
# Date: 2023-04-10 15:33:11
# LastEditors: jt 1723221731@qq.com
# LastEditTime: 2023-06-29 16:14:03
# FilePath: /flow_w/csv_plot_result.py
# Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
# '''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='Times New Roman',size=13)
# # # 2500veh/h Lita10%
# # y1=[]
# r1=pd.read_csv("/home/jt/0823/Litaxing_2500/litaxing_2500_speed_emission_1.csv")
# r2=pd.read_csv("/home/jt/0823/Litaxing_2500/litaxing_2500_speed_emission_2.csv")
# r3=pd.read_csv("/home/jt/0823/Litaxing_2500/litaxing_2500_speed_emission_3.csv")
# # r4=pd.read_csv("/home/jt/0823/Litaxing_2500/litaxing_2500_speed_emission_4.csv")
# r5=pd.read_csv("/home/jt/0823/Litaxing_2500/litaxing_2500_speed_emission_5.csv")
# r6=pd.read_csv("/home/jt/0823/Litaxing_2500/litaxing_2500_speed_emission_6.csv")
# r7=pd.read_csv("/home/jt/0823/Litaxing_2500/litaxing_2500_speed_emission_7.csv")
# r8=pd.read_csv("/home/jt/0823/Litaxing_2500/litaxing_2500_speed_emission_8.csv")
# r9=pd.read_csv("/home/jt/0823/Litaxing_2500/litaxing_2500_speed_emission_9.csv")
# r10=pd.read_csv("/home/jt/0823/Litaxing_2500/litaxing_2500_speed_emission_10.csv")
# y1=(r1['m_speed'][0:1501]+r2['m_speed'][0:1501]+r3['m_speed'][0:1501]+r5['m_speed'][0:1501]+r6['m_speed'][0:1501]+r7['m_speed'][0:1501]+r8['m_speed'][0:1501]+r9['m_speed'][0:1501]+r10['m_speed'][0:1501])/(9)
# # y1=np.array(y1)
# # # 3000veh/h Lita10%
# r1=pd.read_csv("/home/jt/0823/Litaxing_3000/litaxing_3000_speed_emission_1.csv")
# r2=pd.read_csv("/home/jt/0823/Litaxing_3000/litaxing_3000_speed_emission_2.csv")
# r3=pd.read_csv("/home/jt/0823/Litaxing_3000/litaxing_3000_speed_emission_3.csv")
# r4=pd.read_csv("/home/jt/0823/Litaxing_3000/litaxing_3000_speed_emission_4.csv")
# r5=pd.read_csv("/home/jt/0823/Litaxing_3000/litaxing_3000_speed_emission_5.csv")
# r6=pd.read_csv("/home/jt/0823/Litaxing_3000/litaxing_3000_speed_emission_6.csv")
# r7=pd.read_csv("/home/jt/0823/Litaxing_3000/litaxing_3000_speed_emission_7.csv")
# r8=pd.read_csv("/home/jt/0823/Litaxing_3000/litaxing_3000_speed_emission_8.csv")
# r9=pd.read_csv("/home/jt/0823/Litaxing_3000/litaxing_3000_speed_emission_9.csv")
# r10=pd.read_csv("/home/jt/0823/Litaxing_3000/litaxing_3000_speed_emission_10.csv")
# y2=(r1['m_speed'][0:1501]+r2['m_speed'][0:1501]+r3['m_speed'][0:1501]+r4['m_speed'][0:1501]+r5['m_speed'][0:1501]+r6['m_speed'][0:1501]+r7['m_speed'][0:1501]+r8['m_speed'][0:1501]+r9['m_speed'][0:1501]+r10['m_speed'][0:1501])/(10)
# # # 2500veh/h Liji10%  y3
# r1=pd.read_csv("/home/jt/0823/Lijixing_2500/lijixing_2500_speed_emission_1.csv")
# r2=pd.read_csv("/home/jt/0823/Lijixing_2500/lijixing_2500_speed_emission_2.csv")
# y3=(r1['m_speed'][0:1501]+r2['m_speed'][0:1501])/(2)
# # # 3000veh/h Liji10%  y4
# r1=pd.read_csv("/home/jt/0823/Lijixing_3000/lijixing_3000_speed_emission_1.csv")
# r2=pd.read_csv("/home/jt/0823/Lijixing_3000/lijixing_3000_speed_emission_2.csv")
# r3=pd.read_csv("/home/jt/0823/Lijixing_3000/lijixing_3000_speed_emission_3.csv")
# r4=pd.read_csv("/home/jt/0823/Lijixing_3000/lijixing_3000_speed_emission_4.csv")
# y4=(r1['m_speed'][0:1501]+r2['m_speed'][0:1501]+r3['m_speed'][0:1501]+r4['m_speed'][0:1501])/(4)
#
# m1=pd.read_csv("/home/jt/0823/Uncontrol_2500_10%_speed_emission.csv")['m_speed'][0:1501]
# m2=pd.read_csv("/home/jt/0823/Uncontrol_3000_10%_speed_emission.csv")['m_speed'][0:1501]
# # # 2500veh/h
# m3=pd.read_csv("/home/jt/0823/VSL2500_speed_emission.csv")['m_speed'][0:1501]
# m4=pd.read_csv("/home/jt/0823/VSL3000_speed_emission.csv")['m_speed'][0:1501]
# # x = [i*0.2 for i in range(1501)]
# # # x1=[i for i in range(1501)]
# # plt.plot(x, m1)
# # plt.plot(x, y1)
# # plt.plot(x, m3)
# # plt.plot(x, y3)
# # plt.xlim([0,300])
# # # ,prop={"family":"Times New Roman","size":12}
# # plt.legend(['Uncontrol','DRL_Altruism','VSL','DRL_Egoism'],prop={"family":"Times New Roman","size":11})#利他性
# # plt.xlabel("Time(s)",fontdict={"family":"Times New Roman","size":14})
# # plt.ylabel("Average_speed(m/s)",fontdict={"family":"Times New Roman","size":14})
# # plt.grid()
# # plt.show()
#
# # 3000veh/h
# x = [i*0.2 for i in range(1501)]
# x1=[i for i in range(1501)]
# plt.plot(x, m2)
# plt.plot(x, y2)
# plt.plot(x, m4)
# plt.plot(x, y4)
# plt.xlim([0,300])
# # ,prop={"family":"Times New Roman","size":12}
# plt.legend(['Uncontrol','DRL_Altruism','VSL','DRL_Egoism'],prop={"family":"Times New Roman","size":11})#利他性
# plt.xlabel("Time(s)",fontdict={"family":"Times New Roman","size":14})
# plt.ylabel("Average_speed(m/s)",fontdict={"family":"Times New Roman","size":14})
# plt.grid()
# plt.show()
#
# # r1=pd.read_csv("/home/jt/0712/Bottleneck_2500_speed_emission.csv")
# #
# # r4=pd.read_csv("/home/jt/0712/Lijixing_2500_first_0713/bottleneck_lijixing_2_speed_emission.csv")
# # x = [i*0.2 for i in range(1501)]
# # x1=[i for i in range(1501)]
# # plt.plot(x, r1['m_speed'][0:1501])
# #
# # plt.plot(x, r4['m_speed'][0:1501])
# # plt.xlim([0,300])
# # # ,prop={"family":"Times New Roman","size":12}
# # plt.legend(['Uncontrol','DRL_Egoism'],prop={"family":"Times New Roman"})#利他性
# # plt.xlabel("Time(s)",fontdict={"family":"Times New Roman","size":14})
# # plt.ylabel("Average_speed(m/s)",fontdict={"family":"Times New Roman","size":14})
# #
# # plt.grid()
# # plt.show()
#
# # 折扣率的奖励图
# r=pd.read_csv("/home/jt/ray_results/bottleneck/PPO_MergePOEnv-v0_0_2023-07-22_12-30-08frhgo53c/progress.csv")
# r1=pd.read_csv("/home/jt/0712/Learning_rate/Lr_1e-3_dr_0999/progress.csv")
# r2=pd.read_csv("/home/jt/0712/Discount_rate/Lr_1e-3_dr_099/progress.csv")
# r3=pd.read_csv("/home/jt/0712/Discount_rate/Lr_1e-3_dr_09/progress.csv")
# # rmean=r["episode_reward_mean"]
# r1mean=r1["episode_reward_mean"]
# r2mean=r2["episode_reward_mean"]
# r3mean=r3["episode_reward_mean"]
# x=[i for i in range(500)]
# x1=[i for i in range(714)]
# # plt.plot(x, rmean[0:500])
# plt.plot(x, r1mean)
# plt.plot(x, r2mean)
# plt.plot(x, r3mean[0:500])
# plt.xlim([0,500])
# plt.legend(['dr=0.999','dr=0.99','dr=0.9'])#利他性
# plt.xlabel("Iterations",fontdict={"family":"Times New Roman","size":14})
# plt.ylabel("Total rewards",fontdict={"family":"Times New Roman","size":14})
# plt.grid()
# plt.show()
#
# # 学习率的奖励图
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
#
# # # 2500veh/h
# r1=pd.read_csv("/home/jt/0823/shentoulv1/60%/3000_60%_UNcontrol_speed_emission.csv")
# r2=pd.read_csv("/home/jt/0823/bottleneck_20230905-1909561693912196.6503994-0_speed_emission.csv")
# # r3=pd.read_csv("/home/jt/0823/Litaxing_2500/litaxing_2500_speed_emission_10.csv")
# # r4=pd.read_csv("/home/jt/0823/shentoulv/50%Uncontrol_2500_speed_emission.csv")
# # r5=pd.read_csv("/home/jt/0823/shentoulv/80%Uncontrol_2500_speed_emission.csv")
# # r6=pd.read_csv("/home/jt/0823/shentoulv/100%Uncontrol_2500_speed_emission.csv")
# x = [i*0.2 for i in range(1501)]
# x1=[i for i in range(1501)]
# plt.plot(x, r1['m_speed'][0:1501])
# plt.plot(x, r2['m_speed'][0:1501])
# # plt.plot(x, r3['m_speed'][0:1501])
# # plt.plot(x, r4['m_speed'][0:1501])
# # plt.plot(x, r5['m_speed'][0:1501])
# # plt.plot(x, r6['m_speed'][0:1501])
# plt.xlim([0,300])
# print(sum(r1['m_speed'][0:1501]),sum(r2['m_speed'][0:1501]),(sum(r2['m_speed'][0:1501])-sum(r1['m_speed'][0:1501]))/sum(r1['m_speed'][0:1501]))
# # ,prop={"family":"Times New Roman","size":12}
# plt.legend(['3000Un10%','3000Liji10%'],prop={"family":"Times New Roman","size":11})#利他性
# plt.xlabel("Time(s)",fontdict={"family":"Times New Roman","size":14})
# plt.ylabel("Average_speed(m/s)",fontdict={"family":"Times New Roman","size":14})
# plt.grid()
# plt.show()
# r=pd.read_csv("/home/jt/ray_results/bottleneck/PPO_MergePOEnv-v0_0_2023-09-03_17-47-07tm0g0xb0/progress.csv")
# # r1=pd.read_csv("/home/jt/0712/Learning_rate/Lr_1e-4_dr_0999/progress.csv")
# # r2=pd.read_csv("/home/jt/0712/Learning_rate/Lr_1e-5_dr_0999/progress.csv")
# rmean=r["episode_reward_mean"]
# # r1mean=r1["episode_reward_mean"]
# # r2mean=r2["episode_reward_mean"]
# x=[i for i in range(640)]
# # x1=[i for i in range(500)]
# plt.plot(x, rmean)
# # plt.plot(x, r1mean)
# # plt.plot(x1, r2mean)
# plt.xlim([0,1000])
# plt.legend(['lr=1e-5'])#利他性
# plt.xlabel("Iterations",fontdict={"family":"Times New Roman","size":14})
# plt.ylabel("Total rewards",fontdict={"family":"Times New Roman","size":14})
# plt.grid()
# plt.show()
#
# r=pd.read_csv("/home/jt/0823/shentoulv/10%Uncontrol_2500_emission.csv")
# data={}
#
# import csv
# # with open("/home/jt/0823/shentoulv/10%Uncontrol_2500_emission.csv", 'rb') as f:
# #     reader = csv.DictReader(f, delimiter=',')
# # print(type(reader))
# # for row in reader:
# #     item=data.get(row['id'],dict())
# #     item[row[]]=int(row[])
# #     data[row['id']]=item
# # for _,row in r.iterrows():
# #     temp_dict1=row.to_dict()
# #     vehid_val=temp_dict1.pop('id')
# #     t_val=temp_dict1.pop('time')
# #     if vehid_val not in data:
# #         data[vehid_val]={}
# #     if t_val not in data[vehid_val]:
# #         data[vehid_val][t_val]={}
# #     for key,value in temp_dict1.items():
# #         if key not in data[vehid_val][t_val]:
# #             data[vehid_val][t_val][key] = value
# # print(data['flow_00.0'][0.8])
# # print(type(data['flow_00.0'][0.8]))
# # print(data['flow_00.0'][0.8].keys())
# # print(data['flow_00.0'][0.8].values())
#
#
#
# # for _,row in r.iterrows():
# #     temp_dict1=row.to_dict()
# #     vehid_val=temp_dict1.pop('distance')
# #     t_val=temp_dict1.pop('id')
# #     if vehid_val not in data:
# #         data[vehid_val]={}
# #     if t_val not in data[vehid_val]:
# #         data[vehid_val][t_val]={}
# #     for key,value in temp_dict1.items():
# #         if key not in data[vehid_val][t_val]:
# #             data[vehid_val][t_val][key] = value
# # sum_dict={}
# # for dis,dis_value in data.items():
# #     bb=0
# #     for veh,vehid_val in dis_value.items():
# #         # if 'speed' in vehid_val:
# #         bb += vehid_val['speed']
# #             # if dis in sum_dict:
# #             #     sum_dict[dis]+=vehid_val['speed']
# #             # else:
# #             #     sum_dict[dis]=vehid_val['speed']
# #     sum_dict[dis]=bb/len(dis_value)
# # print(len(set(sum_dict.keys())),len(sum_dict.keys()),len(sum_dict.values()))
# # print(sum_dict[0.0])
# # sorted_data=dict(sorted(sum_dict.items(),reverse=True))
# # x=list(sorted_data.keys())
# # y=list(sorted_data.values())
# # x1=x[::1000]
# # y1=y[::1000]
# # plt.plot(x1,y1)
# # plt.show()
#
# categories=['0%CAV','10%CAVs','20%CAVs','30%CAVs','40%CAVs','50%CAVs']
categories=['0%CAV','10%CAVs','20%CAVs','30%CAVs','40%CAVs','50%CAVs','60%CAVs']
# # 2500veh/h
# DRL_Altruism=np.array([11.39,14.12,15.75,15.123,16.44,16.43])
# DRL_Egoism=np.array([11.39,10.57,10.786,8.04,12.23,11.36])
# VSL=np.array([12.23,13.32,13.93,13.84,13.9,14.1])
# 3000veh/h
# DRL_Altruism=np.array([10.55,12.46,12.63,13.36,13.82,14.35,15.86])
# DRL_Egoism=np.array([10.55,9.98,9.72,9.59,9.8,10.7,11.66])
# VSL=np.array([11.36,11.6,12.2,12.74,12.81,12.85,12.9])
# angles=np.linspace(0,2*np.pi,len(categories),endpoint=False).tolist()
# angles=np.concatenate((angles,[angles[0]]))
# DRL_Altruism=np.concatenate((DRL_Altruism,[DRL_Altruism[0]]))
# VSL=np.concatenate((VSL,[VSL[0]]))
# DRL_Egoism=np.concatenate((DRL_Egoism,[DRL_Egoism[0]]))
# angles+=angles[:1]
# fig,ax=plt.subplots(figsize=(11,11),subplot_kw=dict(polar=True))
# # ax.fill(angles,DRL_Altruism,color='salmon',alpha=0.25)
# ax.plot(angles,DRL_Altruism,color='crimson',linewidth=2,linestyle='solid',label='DRL_Altruism')
# # ax.fill(angles,VSL,color='g',alpha=0.25)
# ax.plot(angles,VSL,color='g',linewidth=2,linestyle='dashed',label='VSL')
# # ax.fill(angles,DRL_Egoism,color='b',alpha=0.25)
# ax.plot(angles,DRL_Egoism,color='black',linewidth=2,linestyle='dashdot',label='DRL_Egoism')
# ax.set_xticks(angles[:-1])
# ax.set_xticklabels(categories,fontname="Times New Roman",fontsize=28)
# ax.tick_params(axis='y',labelsize=28)
# # plt.thetagrids(angles*180/np.pi, categories,1.2)
# # ax.yaxis.set_major_formatter(plt.FuncFormatter(percentage_label))
# # ax.set_rlabel_position(180)
# ax.legend(loc='upper right',bbox_to_anchor=(1.16,1.14),fontsize=24)
# # ax.legend(bbox_to_anchor=(1.17,1.18),fontsize=24)
# plt.tight_layout()
# plt.show()

#
# # # 2500veh/h Lita10%
# # r1=pd.read_csv("/home/jt/0823/Litaxing_2500/litaxing_2500_speed_emission_1.csv")
# # r2=pd.read_csv("/home/jt/0823/Litaxing_2500/litaxing_2500_speed_emission_2.csv")
# # r3=pd.read_csv("/home/jt/0823/Litaxing_2500/litaxing_2500_speed_emission_3.csv")
# # r4=pd.read_csv("/home/jt/0823/Litaxing_2500/litaxing_2500_speed_emission_4.csv")
# # r5=pd.read_csv("/home/jt/0823/Litaxing_2500/litaxing_2500_speed_emission_5.csv")
# # r6=pd.read_csv("/home/jt/0823/Litaxing_2500/litaxing_2500_speed_emission_6.csv")
# # r7=pd.read_csv("/home/jt/0823/Litaxing_2500/litaxing_2500_speed_emission_7.csv")
# # r8=pd.read_csv("/home/jt/0823/Litaxing_2500/litaxing_2500_speed_emission_8.csv")
# # r9=pd.read_csv("/home/jt/0823/Litaxing_2500/litaxing_2500_speed_emission_9.csv")
# # r10=pd.read_csv("/home/jt/0823/Litaxing_2500/litaxing_2500_speed_emission_10.csv")
# # print(sum(r1['m_speed'][0:1501]+r2['m_speed'][0:1501]+r3['m_speed'][0:1501]+r4['m_speed'][0:1501]+r5['m_speed'][0:1501]+r6['m_speed'][0:1501]+r7['m_speed'][0:1501]+r8['m_speed'][0:1501]+r9['m_speed'][0:1501]+r10['m_speed'][0:1501])/(1501*10))
# # # 2500veh/h Lita20%
# # r1=pd.read_csv("/home/jt/0823/shentoulv/20%/2500_20%_speed_emission_1.csv")
# # r2=pd.read_csv("/home/jt/0823/shentoulv/20%/2500_20%_speed_emission_2.csv")
# # r3=pd.read_csv("/home/jt/0823/shentoulv/20%/2500_20%_speed_emission_3.csv")
# # r4=pd.read_csv("/home/jt/0823/shentoulv/20%/2500_20%_speed_emission_4.csv")
# # r5=pd.read_csv("/home/jt/0823/shentoulv/20%/2500_20%_speed_emission_5.csv")
# # r6=pd.read_csv("/home/jt/0823/shentoulv/20%/2500_20%_speed_emission_6.csv")
# # # r7=pd.read_csv("/home/jt/0823/shentoulv/20%/2500_20%_speed_emission_7.csv")
# # # r8=pd.read_csv("/home/jt/0823/shentoulv/20%/2500_20%_speed_emission_8.csv")
# # # r9=pd.read_csv("/home/jt/0823/shentoulv/20%/2500_20%_speed_emission_9.csv")
# # # r10=pd.read_csv("/home/jt/0823/shentoulv/20%/2500_20%_speed_emission_10.csv")
# # print(sum(r1['m_speed'][0:1501]+r2['m_speed'][0:1501]+r3['m_speed'][0:1501]+r4['m_speed'][0:1501]+r5['m_speed'][0:1501]+r6['m_speed'][0:1501])/(1501*6))
# # # 2500veh/h Lita30%
# # r1=pd.read_csv("/home/jt/0823/shentoulv/30%/2500_30%_speed_emission_1.csv")
# # r2=pd.read_csv("/home/jt/0823/shentoulv/30%/2500_30%_speed_emission_2.csv")
# # r3=pd.read_csv("/home/jt/0823/shentoulv/30%/2500_30%_speed_emission_3.csv")
# # r4=pd.read_csv("/home/jt/0823/shentoulv/30%/2500_30%_speed_emission_4.csv")
# # r5=pd.read_csv("/home/jt/0823/shentoulv/30%/2500_30%_speed_emission_5.csv")
# # r6=pd.read_csv("/home/jt/0823/shentoulv/30%/2500_30%_speed_emission_6.csv")
# # r7=pd.read_csv("/home/jt/0823/shentoulv/30%/2500_30%_speed_emission_7.csv")
# # r8=pd.read_csv("/home/jt/0823/shentoulv/30%/2500_30%_speed_emission_8.csv")
# # r9=pd.read_csv("/home/jt/0823/shentoulv/30%/2500_30%_speed_emission_9.csv")
# # r10=pd.read_csv("/home/jt/0823/shentoulv/30%/2500_30%_speed_emission_10.csv")
# # print(sum(r1['m_speed'][0:1501]+r2['m_speed'][0:1501]+r3['m_speed'][0:1501]+r4['m_speed'][0:1501]+r5['m_speed'][0:1501]+r6['m_speed'][0:1501]+r7['m_speed'][0:1501]+r8['m_speed'][0:1501]+r9['m_speed'][0:1501]+r10['m_speed'][0:1501])/(1501*10))
# # # 2500veh/h Lita40%
# # r1=pd.read_csv("/home/jt/0823/shentoulv/40%/2500_40%_speed_emission_1.csv")
# # r2=pd.read_csv("/home/jt/0823/shentoulv/40%/2500_40%_speed_emission_2.csv")
# # r3=pd.read_csv("/home/jt/0823/shentoulv/40%/2500_40%_speed_emission_3.csv")
# # r4=pd.read_csv("/home/jt/0823/shentoulv/40%/2500_40%_speed_emission_4.csv")
# # r5=pd.read_csv("/home/jt/0823/shentoulv/40%/2500_40%_speed_emission_5.csv")
# # r6=pd.read_csv("/home/jt/0823/shentoulv/40%/2500_40%_speed_emission_6.csv")
# # r7=pd.read_csv("/home/jt/0823/shentoulv/40%/2500_40%_speed_emission_7.csv")
# # r8=pd.read_csv("/home/jt/0823/shentoulv/40%/2500_40%_speed_emission_8.csv")
# # r9=pd.read_csv("/home/jt/0823/shentoulv/40%/2500_40%_speed_emission_9.csv")
# # r10=pd.read_csv("/home/jt/0823/shentoulv/40%/2500_40%_speed_emission_10.csv")
# # print(sum(r1['m_speed'][0:1501]+r2['m_speed'][0:1501]+r3['m_speed'][0:1501]+r4['m_speed'][0:1501]+r5['m_speed'][0:1501]+r6['m_speed'][0:1501]+r7['m_speed'][0:1501]+r8['m_speed'][0:1501]+r9['m_speed'][0:1501]+r10['m_speed'][0:1501])/(1501*10))
# # # 2500veh/h Lita50%
# # r1=pd.read_csv("/home/jt/0823/shentoulv/50%/2500_50%_speed_emission_1.csv")
# # r2=pd.read_csv("/home/jt/0823/shentoulv/50%/2500_50%_speed_emission_2.csv")
# # r3=pd.read_csv("/home/jt/0823/shentoulv/50%/2500_50%_speed_emission_3.csv")
# # r4=pd.read_csv("/home/jt/0823/shentoulv/50%/2500_50%_speed_emission_4.csv")
# # r5=pd.read_csv("/home/jt/0823/shentoulv/50%/2500_50%_speed_emission_5.csv")
# # r6=pd.read_csv("/home/jt/0823/shentoulv/50%/2500_50%_speed_emission_6.csv")
# # r7=pd.read_csv("/home/jt/0823/shentoulv/50%/2500_50%_speed_emission_7.csv")
# # r8=pd.read_csv("/home/jt/0823/shentoulv/50%/2500_50%_speed_emission_8.csv")
# # r9=pd.read_csv("/home/jt/0823/shentoulv/50%/2500_50%_speed_emission_9.csv")
# # r10=pd.read_csv("/home/jt/0823/shentoulv/50%/2500_50%_speed_emission_10.csv")
# # print(sum(r1['m_speed'][0:1501]+r2['m_speed'][0:1501]+r3['m_speed'][0:1501]+r4['m_speed'][0:1501]+r5['m_speed'][0:1501]+r6['m_speed'][0:1501]+r7['m_speed'][0:1501]+r8['m_speed'][0:1501]+r9['m_speed'][0:1501]+r10['m_speed'][0:1501])/(1501*10))
# # # 2500veh/h Liji10%
# # r1=pd.read_csv("/home/jt/0823/Lijixing_2500/lijixing_2500_speed_emission_1.csv")
# # r2=pd.read_csv("/home/jt/0823/Lijixing_2500/lijixing_2500_speed_emission_2.csv")
# # print(sum(r1['m_speed'][0:1501]+r2['m_speed'][0:1501])/(1501*2))
# # # 2500veh/h Liji20%
# # r1=pd.read_csv("/home/jt/0823/shentoulv_liji/20%/liji20%_speed_emission_1.csv")
# # r2=pd.read_csv("/home/jt/0823/shentoulv_liji/20%/liji20%_speed_emission_2.csv")
# # r3=pd.read_csv("/home/jt/0823/shentoulv_liji/20%/liji20%_speed_emission_3.csv")
# # r4=pd.read_csv("/home/jt/0823/shentoulv_liji/20%/liji20%_speed_emission_4.csv")
# # # r5=pd.read_csv("/home/jt/0823/shentoulv_liji/20%/2500_30%_speed_emission_5.csv")
# # # r6=pd.read_csv("/home/jt/0823/shentoulv_liji/20%/2500_30%_speed_emission_6.csv")
# # # r7=pd.read_csv("/home/jt/0823/shentoulv_liji/20%/2500_30%_speed_emission_7.csv")
# # # r8=pd.read_csv("/home/jt/0823/shentoulv_liji/20%/2500_30%_speed_emission_8.csv")
# # # r9=pd.read_csv("/home/jt/0823/shentoulv_liji/20%/2500_30%_speed_emission_9.csv")
# # # r10=pd.read_csv("/home/jt/0823/shentoulv_liji/20%/2500_30%_speed_emission_10.csv")
# # print(sum(r1['m_speed'][0:1501]+r2['m_speed'][0:1501]+r3['m_speed'][0:1501]+r4['m_speed'][0:1501])/(1501*4))
# # # 2500veh/h Liji30%
# # r1=pd.read_csv("/home/jt/0823/shentoulv_liji/30%/liji30%_speed_emission_1.csv")
# # r2=pd.read_csv("/home/jt/0823/shentoulv_liji/30%/liji30%_speed_emission_2.csv")
# # r3=pd.read_csv("/home/jt/0823/shentoulv_liji/30%/liji30%_speed_emission_3.csv")
# # # r4=pd.read_csv("/home/jt/0823/shentoulv_liji/20%/liji20%_speed_emission_4.csv")
# # # r5=pd.read_csv("/home/jt/0823/shentoulv_liji/20%/2500_30%_speed_emission_5.csv")
# # # r6=pd.read_csv("/home/jt/0823/shentoulv_liji/20%/2500_30%_speed_emission_6.csv")
# # # r7=pd.read_csv("/home/jt/0823/shentoulv_liji/20%/2500_30%_speed_emission_7.csv")
# # # r8=pd.read_csv("/home/jt/0823/shentoulv_liji/20%/2500_30%_speed_emission_8.csv")
# # # r9=pd.read_csv("/home/jt/0823/shentoulv_liji/20%/2500_30%_speed_emission_9.csv")
# # # r10=pd.read_csv("/home/jt/0823/shentoulv_liji/20%/2500_30%_speed_emission_10.csv")
# # print(sum(r1['m_speed'][0:1501]+r2['m_speed'][0:1501]+r3['m_speed'][0:1501])/(1501*4))
# # # 2500veh/h Liji40%
# # r1=pd.read_csv("/home/jt/0823/shentoulv_liji/40%/liji40%_speed_emission_1.csv")
# # r2=pd.read_csv("/home/jt/0823/shentoulv_liji/40%/liji40%_speed_emission_2.csv")
# # r3=pd.read_csv("/home/jt/0823/shentoulv_liji/40%/liji40%_speed_emission_3.csv")
# # r4=pd.read_csv("/home/jt/0823/shentoulv_liji/40%/liji40%_speed_emission_4.csv")
# # r5=pd.read_csv("/home/jt/0823/shentoulv_liji/40%/liji40%_speed_emission_5.csv")
# # r6=pd.read_csv("/home/jt/0823/shentoulv_liji/40%/liji40%_speed_emission_6.csv")
# # # r7=pd.read_csv("/home/jt/0823/shentoulv_liji/20%/2500_30%_speed_emission_7.csv")
# # # r8=pd.read_csv("/home/jt/0823/shentoulv_liji/20%/2500_30%_speed_emission_8.csv")
# # # r9=pd.read_csv("/home/jt/0823/shentoulv_liji/20%/2500_30%_speed_emission_9.csv")
# # # r10=pd.read_csv("/home/jt/0823/shentoulv_liji/20%/2500_30%_speed_emission_10.csv")
# # print(sum(r1['m_speed'][0:1501]+r2['m_speed'][0:1501]+r3['m_speed'][0:1501]+r4['m_speed'][0:1501]+r5['m_speed'][0:1501]+r6['m_speed'][0:1501])/(1501*6))
# # # 2500veh/h Liji50%
# # r1=pd.read_csv("/home/jt/0823/shentoulv_liji/50%/liji50%_speed_emission_1.csv")
# # r2=pd.read_csv("/home/jt/0823/shentoulv_liji/50%/liji50%_speed_emission_2.csv")
# # r3=pd.read_csv("/home/jt/0823/shentoulv_liji/50%/liji50%_speed_emission_3.csv")
# # r4=pd.read_csv("/home/jt/0823/shentoulv_liji/50%/liji50%_speed_emission_4.csv")
# # r5=pd.read_csv("/home/jt/0823/shentoulv_liji/50%/liji50%_speed_emission_5.csv")
# # print(sum(r1['m_speed'][0:1501]+r2['m_speed'][0:1501]+r3['m_speed'][0:1501]+r4['m_speed'][0:1501]+r5['m_speed'][0:1501])/(1501*5))
#
# # # 2500veh/h Liji&lita0%
# r1=pd.read_csv("/home/jt/0823/shentoulv_liji1/60%/3000_60%_UNcontrol_speed_emission.csv")
# print(sum(r1['m_speed'][0:1501])/(1501))
# # # 2500veh/h VSL0%
# # r1=pd.read_csv("/home/jt/0823/VSL2500_0%_speed_emission.csv")
# # print(sum(r1['m_speed'][0:1501])/(1501))
#
#
# 2500不施加控制
# r1=pd.read_csv("/home/jt/0823/Uncontrol_2500_0%_speed_emission.csv")
# r2=pd.read_csv("/home/jt/0823/shentoulv/10%Uncontrol_2500_speed_emission.csv")
# r3=pd.read_csv("/home/jt/0823/shentoulv/20%Uncontrol_2500_speed_emission.csv")
# r4=pd.read_csv("/home/jt/0823/shentoulv/30%/30%Uncontrol_2500_speed_emission.csv")
# r5=pd.read_csv("/home/jt/0823/shentoulv/40%/40%Uncontrol_2500_speed_emission.csv")
# r6=pd.read_csv("/home/jt/0823/shentoulv/50%/50%Uncontrol_2500_speed_emission.csv")
# r7=pd.read_csv("/home/jt/flow_w_vsl/data/2500_60%_UNcontrol_speed_emission.csv")
# r8=pd.read_csv("/home/jt/0823/shentoulv/80%Uncontrol_2500_speed_emission.csv")
# r9=pd.read_csv("/home/jt/0823/shentoulv/100%Uncontrol_2500_speed_emission.csv")
# x = [i*0.2 for i in range(1501)]
# x1=[i for i in range(1501)]
# plt.plot(x, r1['m_speed'][0:1501])
# plt.plot(x, r2['m_speed'][0:1501])
# plt.plot(x, r3['m_speed'][0:1501])
# plt.plot(x, r4['m_speed'][0:1501])
# plt.plot(x, r5['m_speed'][0:1501])
# plt.plot(x, r6['m_speed'][0:1501])
# plt.plot(x, r7['m_speed'][0:1501])
# plt.plot(x, r8['m_speed'][0:1501])
# plt.plot(x, r9['m_speed'][0:1501])
# plt.xlim([0,300])
# # print(sum(r1['m_speed'][0:1501]),sum(r7['m_speed'][0:1501]),(sum(r6['m_speed'][0:1501])-sum(r1['m_speed'][0:1501]))/sum(r1['m_speed'][0:1501]))
# plt.legend(['0%','10%CAVs','20%CAVs','30%CAVs','40%CAVs','50%CAVs','60%CAVs','80%CAVs','100%CAVs'],prop={"family":"Times New Roman","size":11})#利他性
# plt.xlabel("Time(s)",fontdict={"family":"Times New Roman","size":14})
# plt.ylabel("Average_speed(m/s)",fontdict={"family":"Times New Roman","size":14})
# plt.grid()
# plt.show()

# 3000不施加控制
# r1=pd.read_csv("/home/jt/0823/Uncontrol_3000_0%_speed_emission.csv")
# r2=pd.read_csv("/home/jt/0823/Uncontrol_3000_10%_speed_emission.csv")
# r3=pd.read_csv("/home/jt/0823/shentoulv_liji1/20%/Uncontrol_3000_20%_speed_emission.csv")
# r4=pd.read_csv("/home/jt/0823/shentoulv_liji1/30%/Uncontrol_3000_30%_speed_emission.csv")
# r5=pd.read_csv("/home/jt/0823/shentoulv_liji1/40%/Uncontrol_3000_40%_speed_emission.csv")
# r6=pd.read_csv("/home/jt/0823/shentoulv_liji1/50%/Uncontrol_3000_50%_speed_emission.csv")
# r7=pd.read_csv("/home/jt/0823/3000_60%_UNcontrol_speed_emission.csv")
# r8=pd.read_csv("/home/jt/0823/3000_80%_UNcontrol_speed_emission.csv")
# r9=pd.read_csv("/home/jt/0823/3000_100%_UNcontrol_speed_emission.csv")
# x = [i*0.2 for i in range(1501)]
# x1=[i for i in range(1501)]
# plt.plot(x, r1['m_speed'][0:1501])
# plt.plot(x, r2['m_speed'][0:1501])
# plt.plot(x, r3['m_speed'][0:1501])
# plt.plot(x, r4['m_speed'][0:1501])
# plt.plot(x, r5['m_speed'][0:1501])
# plt.plot(x, r6['m_speed'][0:1501])
# plt.plot(x, r7['m_speed'][0:1501])
# plt.plot(x, r8['m_speed'][0:1501])
# plt.plot(x, r9['m_speed'][0:1501])
# plt.xlim([0,300])
# # print(sum(r1['m_speed'][0:1501]),sum(r7['m_speed'][0:1501]),(sum(r6['m_speed'][0:1501])-sum(r1['m_speed'][0:1501]))/sum(r1['m_speed'][0:1501]))
# plt.legend(['0%','10%CAVs','20%CAVs','30%CAVs','40%CAVs','50%CAVs','60%CAVs','80%CAVs','100%CAVs'],prop={"family":"Times New Roman","size":11})#利他性
# plt.xlabel("Time(s)",fontdict={"family":"Times New Roman","size":14})
# plt.ylabel("Average_speed(m/s)",fontdict={"family":"Times New Roman","size":14})
# plt.grid()
# plt.show()