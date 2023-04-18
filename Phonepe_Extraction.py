#!/usr/bin/env python
# coding: utf-8

# In[68]:


import os
from os import walk
import json
from pathlib import Path
import pandas as pd

Data_Aggregated_Transaction_Table = pd.DataFrame({})
Data_Aggregated_Transaction_Summary_Table = pd.DataFrame({})

def Aggregated_Transaction_Table_fun(state,year,quarter,path):
  global Data_Aggregated_Transaction_Table
  global Data_Aggregated_Transaction_Summary_Table
  dft = pd.read_json(path)

  dataFrom = dft['data']['from']
  dataTo = dft['data']['to']
  T_row = {'State' : state, 'Year' : year, 'Quarter' : quarter, 
           'DataFrom' : dataFrom,
           'DataTo' : dataTo}
  Data_Aggregated_Transaction_Summary_Table = Data_Aggregated_Transaction_Summary_Table.append(T_row, ignore_index = True)

  DAT_temp = dft['data']['transactionData']
  if DAT_temp:
    for i in DAT_temp:
      DAT_row = {'Payment Mode' : i['name'],
                 'Total Transaction count' : i['paymentInstruments'][0]['count'],
                 'Total Amount' : i['paymentInstruments'][0]['amount'],
                 'Quarter' : quarter, 'Year' : year, 'State' : state
                }
      Data_Aggregated_Transaction_Table = Data_Aggregated_Transaction_Table.append(DAT_row, ignore_index = True)

#Path for all states in aggregated transactions
t_s = r'C:\Users\Sylvester\Desktop\Phonepe\pulse\data\aggregated\transaction\country\india\state'
t_path = r'C:\Users\Sylvester\Desktop\Phonepe\pulse\data\aggregated\transaction\country\india\state'
t_states = os.listdir(t_path)

for i in t_states:
  #print(i)
  p = t_s+'\\'+i
  states_year = os.listdir(p)
  for j in states_year:
    #print(j)
    pt = p+'\\'+j
    f = []
    for (dirpath, dirnames, filenames) in walk(pt):
      f.extend(filenames)
      break
    for k in f:
      fp = pt+'\\'+k
      fn = Path(fp).stem
      #print(i,j,fn)
      Aggregated_Transaction_Table_fun(i,j,fn,fp)
      #print(fp)


# In[55]:


#Data_Aggregated_Transaction_Table
Data_Aggregated_Transaction_Table.to_csv('Data_Aggregated_Transaction_Table.csv',index = False)
print(len(Data_Aggregated_Transaction_Table))
Data_Aggregated_Transaction_Table.head(5)


# In[69]:


Data_Aggregated_Transaction_Summary_Table.to_csv('Data_Aggregated_Transaction_Summary_Table.csv',index=False)  
print(len(Data_Aggregated_Transaction_Summary_Table))
Data_Aggregated_Transaction_Summary_Table.head(5)


# In[57]:


#Data_Aggregated_User_Table
Data_Aggregated_User_Table = pd.DataFrame({}) 
Data_Aggregated_User_Summary_Table = pd.DataFrame({})


# In[58]:


import os
from os import walk
from pathlib import Path
import pandas as pd

def Aggregated_User_Table_fun(state,year,quarter,path):
    global Data_Aggregated_User_Table
    global Data_Aggregated_User_Summary_Table
    dfu = pd.read_json(path)
    
    registeredUsers=dfu['data']['aggregated']['registeredUsers']
    appOpens=dfu['data']['aggregated']['appOpens']
    U_row={'State':state,'Year': year,'Quarter':quarter,'Registered Users':registeredUsers,'AppOpenings':appOpens}
    Data_Aggregated_User_Summary_Table= Data_Aggregated_User_Summary_Table.append(U_row, ignore_index = True )

    DAU_temp=dfu['data']['usersByDevice']
    if DAU_temp:  
        for i in DAU_temp:
            DAU_row={ 'Brand Name':i['brand'], 'Registered Users Count':i['count'], 'Percentage Share of Brand':i['percentage'],'Quarter':quarter,'Year': year,'State':state}  
            Data_Aggregated_User_Table = Data_Aggregated_User_Table.append(DAU_row, ignore_index = True)

u_s= r'C:\Users\Sylvester\Desktop\Phonepe\pulse\data\aggregated\user\country\india\state'
u_path = r'C:\Users\Sylvester\Desktop\Phonepe\pulse\data\aggregated\user\country\india\state'
u_states = os.listdir(u_path)

for i in u_states:
    #print(i)
    p=s+'\\'+i
    states_year=os.listdir(p)
    for j in states_year:
        #print(j)
        pt=p+'\\'+j
        f=[]
        for (dirpath, dirnames, filenames) in walk(pt):
            f.extend(filenames)
            break
        for k in f:
            fp=pt+'\\'+k            
            fn=Path(fp).stem
            #print(i,j,fn)
            Aggregated_User_Table_fun(i,j,fn,fp)


# In[59]:


#Data_Aggregated_User_Table
Data_Aggregated_User_Table.to_csv('Data_Aggregated_User_Table.csv',index=False) 
print(len(Data_Aggregated_User_Table))
Data_Aggregated_User_Table.head(5)


# In[60]:


#Data_Aggregated_User_Summary_Table
Data_Aggregated_User_Summary_Table.to_csv('Data_Aggregated_User_Summary_Table.csv',index=False) 
print(len(Data_Aggregated_User_Summary_Table))
Data_Aggregated_User_Summary_Table.head(5)


# In[61]:


#Data_Map_Transaction_Table
Data_Map_Transaction_Table = pd.DataFrame({})


# In[ ]:





# In[62]:


import os
from os import walk
import json
from pathlib import Path
import pandas as pd


def Data_Map_Transaction_Table_Fun(state,year,quarter,path):
  global Data_Map_Transaction_Table
  dfmt = pd.read_json(path)

  DMT_temp = dfmt['data']['hoverDataList']
  if DMT_temp:
    for i in DMT_temp:
      DMT_row = {'Place Name' : i['name'], 
                 'Total Transaction count' : i['metric'][0]['count'],
                 'Total Amount' : i['metric'][0]['amount'], 
                 'Quarter' : quarter, 'Year' : year, 'State' : state
                }
      Data_Map_Transaction_Table = Data_Map_Transaction_Table.append(DMT_row, ignore_index = True)

#Path for all states in aggregated transactions
t_s = r'C:\Users\Sylvester\Desktop\Phonepe\pulse\data\map\transaction\hover\country\india\state'
t_path = r'C:\Users\Sylvester\Desktop\Phonepe\pulse\data\map\transaction\hover\country\india\state'
t_states = os.listdir(t_path)

for i in t_states:
  #print(i)
  p = t_s+'\\'+i
  states_year = os.listdir(p)
  for j in states_year:
    #print(j)
    pt = p+'\\'+j
    f = []
    for (dirpath, dirnames, filenames) in walk(pt):
      f.extend(filenames)
      break
    for k in f:
      fp = pt+'\\'+k
      fn = Path(fp).stem
      #print(i,j,fn)
      Data_Map_Transaction_Table_Fun(i,j,fn,fp)
      #print(fp)


# In[63]:


Data_Map_Transaction_Table.to_csv('Data_Map_Transaction_Table.csv', index = False)
print(len(Data_Map_Transaction_Table))
Data_Map_Transaction_Table.head(5)


# In[64]:


#Data_Map_User_Table
Data_Map_User_Table = pd.DataFrame({})


# In[65]:


def Data_Map_User_Table_Fun(state,year,quarter,path):
  global Data_Map_User_Table
  dfmu = pd.read_json(path)

  DMU_temp = dfmu['data']['hoverData']
  if DMU_temp:
    for i in DMU_temp:
      DMU_row = {'Place Name' : i,
                 'Registered Users Count' : DMU_temp[i]['registeredUsers'],
                 'App Openings' : DMU_temp[i]['appOpens'],
                 'Quarter' : quarter, 'Year' : year, 'State' : state
                }
      Data_Map_User_Table = Data_Map_User_Table.append(DMU_row, ignore_index = True)

#Path for all states in aggregated transactions
t_s = r'C:\Users\Sylvester\Desktop\Phonepe\pulse\data\map\user\hover\country\india\state'
t_path = r'C:\Users\Sylvester\Desktop\Phonepe\pulse\data\map\user\hover\country\india\state'
t_states = os.listdir(t_path)

for i in t_states:
  #print(i)
  p = t_s+'\\'+i
  states_year = os.listdir(p)
  for j in states_year:
    #print(j)
    pt = p+'\\'+j
    f = []
    for (dirpath, dirnames, filenames) in walk(pt):
      f.extend(filenames)
      break
    for k in f:
      fp = pt+'\\'+k
      fn = Path(fp).stem
      #print(i,j,fn)
      Data_Map_User_Table_Fun(i,j,fn,fp)
      #print(fp)


# In[66]:


#Data_Map_User_Table
Data_Map_User_Table.to_csv('Data_Map_User_Table.csv',index=False) 
print(len(Data_Map_User_Table))
Data_Map_User_Table.head(8)


# In[ ]:




