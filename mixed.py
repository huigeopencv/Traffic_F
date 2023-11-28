
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
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
ax.fill(angles,DRL_Altruism,color='lime',alpha=0.25)
ax.plot(angles,DRL_Altruism,color='lime',linewidth=2,linestyle='solid',label='DRL_Altruism')

ax.fill(angles,VSL,color='cyan',alpha=0.25)
ax.plot(angles,VSL,color='cyan',linewidth=2,linestyle='dashed',label='VSL')

ax.fill(angles,DRL_Egoism,color='deeppink',alpha=0.25)
ax.plot(angles,DRL_Egoism,color='deeppink',linewidth=2,linestyle='dotted',label='DRL_Egoism')

ax.plot(angles,Uncontrol,color='gold',linewidth=2,linestyle='dashdot',label='Uncontrol')
ax.fill(angles,Uncontrol,color='gold',alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories,fontsize=28)
ax.tick_params(axis='y',labelsize=28)
# plt.thetagrids(angles*180/np.pi, categories,1.2)
# ax.yaxis.set_major_formatter(plt.FuncFormatter(percentage_label))
# ax.set_rlabel_position(180)
# 3000veh/h的图例位置
ax.legend(loc='center left',bbox_to_anchor=(1,0.5),fontsize=24)
#plt.savefig("./mixed.jpg",dpi=400,bbox_inches='tight')
# 2500veh/h的图例位置
# ax.legend(bbox_to_anchor=(1.2,1.26),fontsize=24)
plt.tight_layout()
plt.show()


