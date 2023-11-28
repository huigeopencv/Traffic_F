import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='Times New Roman',size=13)
# 2500veh/h
# categories=['0%CAV','10%CAVs','20%CAVs','30%CAVs','40%CAVs','50%CAVs']
# DRL_Altruism=np.array([11.39,14.12,15.75,15.123,16.44,16.43])
# DRL_Egoism=np.array([11.39,10.57,10.786,8.04,12.23,11.36])
# VSL=np.array([12.23,13.32,13.93,13.84,15.2,15.6])
# Uncontrol=np.array([11.39,11.74,12.02,12.00,14.14,14.32])
# 3000veh/h
categories=['0%CAV','10%CAVs','20%CAVs','30%CAVs','40%CAVs','50%CAVs','60%CAVs']
DRL_Altruism=np.array([10.55,12.46,12.63,13.36,13.82,14.35,15.86])
DRL_Egoism=np.array([10.55,9.98,9.72,9.59,9.8,10.7,11.66])
VSL=np.array([11.36,11.6,12.2,12.74,12.81,13.4,14.9])
Uncontrol=np.array([10.55,10.61,10.9,10.9,11.4,11.82,13.3])
angles=np.linspace(0,2*np.pi,len(categories),endpoint=False).tolist()
angles=np.concatenate((angles,[angles[0]]))
DRL_Altruism=np.concatenate((DRL_Altruism,[DRL_Altruism[0]]))
VSL=np.concatenate((VSL,[VSL[0]]))
DRL_Egoism=np.concatenate((DRL_Egoism,[DRL_Egoism[0]]))
Uncontrol=np.concatenate((Uncontrol,[Uncontrol[0]]))
angles+=angles[:1]
fig,ax=plt.subplots(figsize=(11,11),subplot_kw=dict(polar=True))
# 颜色填充
# ax.fill(angles,DRL_Altruism,color='salmon',alpha=0.25)
ax.plot(angles,DRL_Altruism,color='crimson',linewidth=2,linestyle='solid',label='DRL_Altruism')
# ax.fill(angles,VSL,color='g',alpha=0.25)
ax.plot(angles,VSL,color='g',linewidth=2,linestyle='dashed',label='VSL')
# ax.fill(angles,DRL_Egoism,color='b',alpha=0.25)
ax.plot(angles,DRL_Egoism,color='black',linewidth=2,linestyle='dashdot',label='DRL_Egoism')
ax.plot(angles,Uncontrol,color='pink',linewidth=2,linestyle='dashdot',label='Uncontrol')
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories,fontname="Times New Roman",fontsize=28)
ax.tick_params(axis='y',labelsize=28)
# plt.thetagrids(angles*180/np.pi, categories,1.2)
# ax.yaxis.set_major_formatter(plt.FuncFormatter(percentage_label))
# ax.set_rlabel_position(180)
# 3000veh/h的图例位置
ax.legend(loc='upper right',bbox_to_anchor=(1.2,1.22),fontsize=24)
# 2500veh/h的图例位置
# ax.legend(bbox_to_anchor=(1.2,1.26),fontsize=24)
plt.tight_layout()
plt.show()