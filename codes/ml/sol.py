import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Dropout, BatchNormalization
from sklearn.utils import shuffle
from PIL import ImageFont

import warnings
warnings.filterwarnings('ignore')

import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import tensorflow as tf

files = ['ttbar','wmp','wpwm','zwpm','n2n2']

cs_lo_k = {
            'ttbar':988.57,
            'wmp'  :1.95*1e5,
            'wpwm' :124.31,
            'zwpm' :51.82,
            'n2n2' :1
          }

br_ratio = {
            'ttbar':0.67*(1-0.67)*2,
            'wmp'  :(1-0.67),
            'wpwm' :(1-0.67)*0.67*2,
            'zwpm' :0.7*(1-0.67),
            'n2n2' :1
          }

cs_nmg = {
         'ttbar':393.30,
         'wmp'  :7.865*1e4,
         'wpwm' :74.96,
         'zwpm' :14.28,
         'n2n2' :1
         }

cs_mg = {'ttbar':5.883,
          'wmp':111.5,
          'wpwm':0.944,
          'zwpm':0.2381,
          'n2n2':3.99*1e-4
        }

cs_pb = []
for f in files:
    cs_pb.append((cs_lo_k[f]*br_ratio[f]*cs_mg[f])/cs_nmg[f])

cs = [i*1e3 for i in cs_pb]
#k_f = [1.954,1.356,1.92,2.09,1.0]

cs_corr = {files[i] : cs[i] for i in range(len(files))}

no_of_files = {'ttbar':0,
          'wmp':0,
          'wpwm':0,
          'zwpm':0,
          'n2n2':0
        }

df = []
for f in range(len(files)):
    con_df = []
    
    for i in range(1,53):
        try:
            con_df.append(pd.read_csv('~/neutrino/datasets/csvdata/' + files[f] + str(i) + '.csv'))
            no_of_files[files[f]] += 1
        except:
            pass
            #print("Not Here : ",files[f],i)
    
    df.append(pd.concat(con_df,ignore_index=True))
    df[-1]['type'] = f
    
    if files[f] == "n2n2":
        df[-1]['tag'] = 1
    else:
        df[-1]['tag'] = 0

tot_num = 0
for i in no_of_files.keys():
    tot_num += no_of_files[i]*1e5
    #print("For the process ",i," the number of events : ",no_of_files[i]*1e5)
#print('Number of Datapoints Considered : ',tot_num)

dtset = pd.concat(df,ignore_index=True)
dtset = shuffle(dtset)
dtset['met'] = np.fabs(dtset['met'])

## Analysis Level Cuts
dtset = dtset[dtset['ptl'] >= 120.0][dtset['ptj'] >= 120.0][dtset['etaj'] <= 2.0][dtset['etaj'] >= -2.0]

train_len = int(0.8*len(dtset))
x_train = dtset.T[:-2].T[:train_len]
y_train = dtset['tag'][:train_len]

x_test = dtset.T[:-2].T[train_len:]
y_test = dtset['tag'][train_len:]

print('Shapes : ',x_train.shape,y_train.shape,x_test.shape,y_test.shape)

model = Sequential()
input_shape = x_train.shape

from keras.layers.normalization.batch_normalization import BatchNormalization
model.add(Dense(10,activation = 'relu',input_dim = input_shape[1]))
model.add(BatchNormalization())
model.add(Dense(25,activation = 'relu',input_dim = 10))
model.add(BatchNormalization())
model.add(Dense(40,activation = 'relu',input_dim = 25))
model.add(BatchNormalization())
model.add(Dense(20,activation = 'relu',input_dim = 40))
model.add(BatchNormalization())
model.add(Dense(12,activation = 'relu',input_dim = 20))
model.add(BatchNormalization())
model.add(Dense(8,activation = 'relu',input_dim = 12))
model.add(BatchNormalization())
model.add(Dense(1,activation = 'sigmoid',input_dim = 8))

model.compile(optimizer='adam', loss='binary_crossentropy',metrics=['accuracy'])

model.fit(x_train,y_train,epochs=150,batch_size=512,validation_split=0.2,class_weight={0:.993,1:0.007})

tot_pred = model.predict(dtset.T[:-2].T)

pred_set = dtset.copy()
pred_set['pred'] = tot_pred

cor_pred = len(pred_set[train_len:][pred_set['pred'] >= 0.5][pred_set['tag'] == 1]) + len(pred_set[train_len:][pred_set['pred'] < 0.5][pred_set['tag'] == 0])
print('The accuracy of the test set is : ',cor_pred/(len(pred_set[train_len:])))

print('Correctly identified signal (True Positive)     : ',len(pred_set[pred_set['pred'] >= 0.5][pred_set['tag'] == 1]))
print('Falsely identified signal (Flase Positive)      : ',len(pred_set[pred_set['pred'] >= 0.5][pred_set['tag'] == 0]))
print('Correctly identified background (True Negative) : ',len(pred_set[pred_set['pred'] < 0.5][pred_set['tag'] == 0]))
print('Falsely identified background (False Negative)  : ',len(pred_set[pred_set['pred'] < 0.5][pred_set['tag'] == 1]))

print('The amount of signal left is     :', len(pred_set[pred_set['pred'] >= 0.5][pred_set['tag'] == 1])/len(df[-1]))
print('The amount of background left is :', len(pred_set[pred_set['pred'] >= 0.5][pred_set['tag'] == 0])/np.sum([len(i) for i in df[:-1]]))

print('Thus, the rate of correct signal prediction is : ',len(pred_set[pred_set['pred'] >= 0.5][dtset['tag'] == 1])/(len(pred_set[pred_set['pred'] >= 0.5])))

L = 3000
ns = cs_corr['n2n2']*(len(pred_set[pred_set['pred'] >= 0.7][pred_set['tag'] == 1])/(no_of_files['n2n2']*1e5))*L
print('n2n2',cs_corr['n2n2'],(len(pred_set[pred_set['pred'] >= 0.7][pred_set['tag'] == 1])))
nb = 0

for i in range(len(files)-1):
    nb += cs_corr[files[i]]*(len(pred_set[pred_set['pred'] >= 0.7][pred_set['tag'] == 0][pred_set['type'] == i])/((no_of_files[files[i]]*1e5)))*L
    print(files[i],len(pred_set[pred_set['pred'] >= 0.7][pred_set['tag'] == 0][pred_set['type'] == i]),cs_corr[files[i]])

print('The number of signal is :', ns)
print('The number of background is :', nb)
print('The significance is :',ns/np.sqrt(nb))

model.save('/home2/kalp_shah/datasets/models/s4')
