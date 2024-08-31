import pandas as pd
import numpy as np
Temperature={
    'To':43,
    'Tp':1,
    'Tf':-24.5,
    'Te':48
    }

convection_coff={
    'Ho':3,
    'Hp':5,
    'Hf':5,
    'He':5
}

coductive_coff={
    'steel':58.1395348837209,
    'cyclopentane':0.021,
    'VIP':0.0025,
    'ABS':0.232558139534884,
    'Gasket':0.062,
    'anti_sweat_condenser':0.965,
    'correction':1
}

df=pd.read_csv('Ref_dimension.csv')
L=df[['Size']]
X1=L.Size[0]-L.Size[7]
X2=L.Size[2]-(L.Size[3]+L.Size[4])/2-(L.Size[5]+L.Size[6])
X3=L.Size[4]/2+L.Size[5]+L.Size[6]/2
X4=L.Size[0]-L.Size[8]
X5=L.Size[1]-L.Size[9]/2
X6=(X3+L.Size[6]/2)-(L.Size[15]+L.Size[11]/2)
i=(L.Size[11]+L.Size[15])-L.Size[6]
tanA=L.Size[15]/(L.Size[13]-L.Size[14])
sinA=L.Size[15]/(L.Size[15]**2+(L.Size[13]-L.Size[14])**2)**0.5
cosA=(L.Size[13]-L.Size[14])/(L.Size[15]**2+(L.Size[13]-L.Size[14])**2)**0.5
j=i*(L.Size[13]-L.Size[14])/L.Size[15]
m=L.Size[1]-L.Size[9]
n=L.Size[12]/sinA
o=L.Size[6]/tanA
k=L.Size[1]-L.Size[13]+o-n
p=L.Size[6]/(2*tanA)
X9=k+n/2-p
X8=(L.Size[11]+L.Size[15]-(L.Size[11]+L.Size[6])/2)/sinA
X7=L.Size[1]-X9-X8*cosA-L.Size[10]/2
Wd1=L.Size[0]-L.Size[7]*2
Wd2=L.Size[0]-L.Size[8]*2
Ht=X2-(L.Size[3]+L.Size[4])/2
Vol_1=Wd1*Ht*(L.Size[1]-L.Size[9])
Vol_2=Wd2*(L.Size[5]-i)*m+Wd2*(k+j+k)*i/2

# Uppar Door Gasket
X10=L.Size[18]-L.Size[21]
X11=L.Size[19]-L.Size[20]

# Lower Door Gasket
X12=L.Size[23]-L.Size[26]
X13=L.Size[24]-L.Size[25]


'''Area'''
Area={
    'upper_room_door_dimension':X10*X11/1e6,
    'upper_room_top_dimension':X1*X5/1e6,
    'upper_room_side_L':X2*X5/1e6,
    'upper_room_side_R':X2*X5/1e6,
    'upper_room_rear':X1*X2/1e6,
    'FC_FF_Partation':((L.Size[1]-L.Size[10]/2)/1000*X4)/1e3,
    #Lower
    'lower_room_door_dimension':X12*X13/1e6,
    'lower_room_side_r':((m+L.Size[10]/2)*X3-(X7*2+X8*cosA)*X8*sinA)/1e6,
    'lower_room_side_l':((m+L.Size[10]/2)*X3-(X7*2+X8*cosA)*X8*sinA)/1e6,
    'lower_room_rear':X6*X4/1e6,
    'lower_engine_vertical':X8*X4/1e6,
    'lower_engine_top':X7*X4/1e6,
    'lower_room_bottom':X9*X4/1e6,
    
}

'''Thickness'''
upper_room_door={
    'External_cover':0.001,
    'Insulation':0.053,
    'Inner_Liner':0.001}

upper_room_top={
    'External_cover':0.001,
    'Insulation':0.068,
    'Inner_Liner':0.001}
upper_room_sides={
    'External_cover':0.001,
    'Insulation':0.072,
    'Inner_Liner':0.001}
upper_room_rear={
    'External_cover':0.001,
    'Insulation':0.069,
    'Inner_Liner':0.001}
fc_ff_partition={
    'Inner_Liner':0.001,
    'Insulation':0.058,
    'Inner_Liner':0.001}
lower_room_door={
    'External_cover':0.001,
    'Insulation':0.045,
    'Inner_Liner':0.001}
lower_room_bottom={
    'External_cover':0.001,
    'Insulation':0.063,
    'Inner_Liner':0.001}
lower_room_sides={
    'External_cover':0.001,
    'Insulation':0.051,
    'Inner_Liner':0.001}
lower_room_rear={
    'External_cover':0.001,
    'Insulation':0.052,
    'Inner_Liner':0.001}
engine_vertical={
    'External_cover':0.001,
    'Insulation':0.052,
    'Inner_Liner':0.001}
engine_top={
    'External_cover':0.001,
    'Insulation':0.056,
    'Inner_Liner':0.001}


'''Resistance'''
Resistance={
    'upper_room_door':(1/convection_coff['Ho'])+(1/convection_coff['Hp'])+(upper_room_door['External_cover']/coductive_coff['steel'])+(upper_room_door['Insulation']/coductive_coff['cyclopentane'])+(upper_room_door['Inner_Liner']/coductive_coff['ABS']),
    'upper_room_top':(1/convection_coff['Ho'])+(1/convection_coff['Hp'])+(upper_room_top['External_cover']/coductive_coff['steel'])+(upper_room_top['Insulation']/coductive_coff['cyclopentane'])+(upper_room_top['Inner_Liner']/coductive_coff['ABS']),
    'upper_room_sides':(1/convection_coff['Ho'])+(1/convection_coff['Hp'])+(upper_room_sides['External_cover']/coductive_coff['steel'])+(upper_room_sides['Insulation']/coductive_coff['cyclopentane'])+(upper_room_sides['Inner_Liner']/coductive_coff['ABS']),
    'upper_room_rear':(1/convection_coff['Ho'])+(1/convection_coff['Hp'])+(upper_room_rear['External_cover']/coductive_coff['steel'])+(upper_room_rear['Insulation']/coductive_coff['cyclopentane'])+(upper_room_rear['Inner_Liner']/coductive_coff['ABS']),
    'FC_FF_partition':(1/convection_coff['Hp'])+(1/convection_coff['Hf'])+(fc_ff_partition['Inner_Liner']/coductive_coff['ABS'])+(fc_ff_partition['Insulation']/coductive_coff['cyclopentane'])+(fc_ff_partition['Inner_Liner']/coductive_coff['ABS']),
    'lower_room_door':(1/convection_coff['Ho'])+(1/convection_coff['Hf'])+(lower_room_door['External_cover']/coductive_coff['steel'])+(lower_room_door['Insulation']/coductive_coff['cyclopentane'])+(lower_room_door['Inner_Liner']/coductive_coff['ABS']),
    'lower_room_bottom':(1/convection_coff['Ho'])+(1/convection_coff['Hf'])+(lower_room_bottom['External_cover']/coductive_coff['steel'])+(lower_room_bottom['Insulation']/coductive_coff['cyclopentane'])+(lower_room_bottom['Inner_Liner']/coductive_coff['ABS']),
    'lower_room_sides':(1/convection_coff['Ho'])+(1/convection_coff['Hf'])+(lower_room_sides['External_cover']/coductive_coff['steel'])+(lower_room_sides['Insulation']/coductive_coff['cyclopentane'])+(lower_room_sides['Inner_Liner']/coductive_coff['ABS']),
    'lower_room_rear':(1/convection_coff['Ho'])+(1/convection_coff['Hf'])+(lower_room_rear['External_cover']/coductive_coff['steel'])+(lower_room_rear['Insulation']/coductive_coff['cyclopentane'])+(lower_room_rear['Inner_Liner']/coductive_coff['ABS']),
    'engine_vertical':(1/convection_coff['Hf'])+(1/convection_coff['He'])+(engine_vertical['External_cover']/coductive_coff['steel'])+(engine_vertical['Insulation']/coductive_coff['cyclopentane'])+(engine_vertical['Inner_Liner']/coductive_coff['ABS']),
    'engine_top':(1/convection_coff['Hf'])+(1/convection_coff['He'])+(engine_top['External_cover']/coductive_coff['steel'])+(engine_top['Insulation']/coductive_coff['cyclopentane'])+(engine_top['Inner_Liner']/coductive_coff['ABS']),
}

'''Temperature'''
T_amb=Temperature['To']
T_upper=Temperature['Tp']
T_lower=Temperature['Tf']
T_engine=Temperature['Te']

'''Heat Absorption'''
upper_room_door=(T_amb-T_upper)*Area['upper_room_door_dimension']/Resistance['upper_room_door']
upper_room_top=(T_amb-T_upper)*Area['upper_room_top_dimension']/Resistance['upper_room_top']
upper_room_side_L=(T_amb-T_upper)*Area['upper_room_side_L']/Resistance['upper_room_sides']
upper_room_side_R=(T_amb-T_upper)*Area['upper_room_side_R']/Resistance['upper_room_sides']
upper_room_side_rear=(T_amb-T_upper)*Area['upper_room_rear']/Resistance['upper_room_rear']
FC_FF_partition=(T_lower-T_upper)*Area['FC_FF_Partation']/Resistance['FC_FF_partition']
lower_room_door=(T_amb-T_lower)*Area['lower_room_door_dimension']/Resistance['lower_room_door']
lower_room_side_L=(T_amb-T_lower)*Area['lower_room_side_l']/Resistance['lower_room_sides']
lower_room_side_R=(T_amb-T_lower)*Area['lower_room_side_r']/Resistance['lower_room_sides']
lower_room_rear=(T_amb-T_lower)*Area['lower_room_rear']/Resistance['lower_room_rear']
engine_vertical=(T_engine-T_lower)*Area['lower_engine_vertical']/Resistance['engine_vertical']
engine_top=(T_engine-T_lower)*Area['lower_engine_top']/Resistance['engine_top']
lower_room_bottom=(T_amb-T_lower)*Area['lower_room_bottom']/Resistance['lower_room_bottom']
#Total Cabinet 
upper_room_heat_absorption=upper_room_door+upper_room_top+upper_room_side_L+upper_room_side_R+upper_room_side_rear+FC_FF_partition
lower_room_heat_absorption=lower_room_door+lower_room_side_L+lower_room_side_R+lower_room_rear+engine_vertical+engine_top+lower_room_bottom-FC_FF_partition
# Gaskert
upper_room_gasket=(T_amb-T_upper)*coductive_coff['Gasket']*((2*(X10+X11))/1e3)
lower_room_gasket=(T_amb-T_lower)*coductive_coff['Gasket']*((2*(X12+X13))/1e3)
#Condenser
anti_swweat=coductive_coff['anti_sweat_condenser']*2*((X1+X2+X3+X4)/1e3)
sides_back=coductive_coff['anti_sweat_condenser']*2*((X1+X2+X3)/1e3)+coductive_coff['anti_sweat_condenser']*2*((X5+X2+X3)/1e3)
condenser_heat_absorption=anti_swweat+sides_back

#Total
Heat_absorption=upper_room_heat_absorption+lower_room_heat_absorption+upper_room_gasket+lower_room_gasket+anti_swweat
print('Total Heat Absorption: %0.3f'%Heat_absorption)
print('Upper Room Heat Absorption: %0.3f'%upper_room_heat_absorption)
print('Lower Room Heat Absorption: %0.3f'%lower_room_heat_absorption)