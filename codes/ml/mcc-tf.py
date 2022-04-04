#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Dropout, BatchNormalization
from sklearn.utils import shuffle
from PIL import ImageFont
import datetime


# In[2]:


import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

import tensorflow as tf


# In[12]:
# In[13]:


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


# In[27]:
# In[5]:


def get_res(x):
    res = np.zeros(shape=(x.shape[0],5))
    #print(x.shape[0],5)
    for i in range(len(x)):
        #print(i.x[i])
        res[i,x[i]] = 1
    
    return res


# In[6]:


no_of_files = {'ttbar':0,
          'wmp':0,
          'wpwm':0,
          'zwpm':0,
          'n2n2':0
        }


# In[7]:


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


# In[8]:


df[-1].head()


# In[9]:


dtset = pd.concat(df,ignore_index=True)
dtset = shuffle(dtset)
dtset['met'] = np.fabs(dtset['met'])


# In[10]:


## Analysis Level Cuts
dtset = dtset[dtset['ptl'] >= 120.0][dtset['ptj'] >= 120.0][dtset['etaj'] <= 2.0][dtset['etaj'] >= -2.0]


# In[11]:


train_len = int(0.8*len(dtset))
x_train = dtset.T[:-2].T[:train_len]
y_train = get_res(dtset['type'][:train_len].values)

x_test = dtset.T[:-2].T[train_len:]
y_test = get_res(dtset['type'][train_len:].values)

print('Shapes : ',x_train.shape,y_train.shape,x_test.shape,y_test.shape)


# In[16]:


backup_callback = tf.keras.callbacks.experimental.BackupAndRestore(backup_dir="/home2/kalp_shah/tmp/backup")

log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)


# In[80]:


def significance(y_true, y_pred):
    y_pred = tf.argmax(y_pred,axis=1,output_type = 'int32')
    y_pred = tf.cast(y_pred,'float32')
    
    y_true = tf.argmax(y_true,axis=1,output_type = 'int32')
    y_true = tf.cast(y_true,'float32')
    
    cross_sec = [6538.845366086956,91227.27272727272,692.2567850586979,199.5908264705882,0.399]
    L = 3000
    
    # Signal
    values = tf.logical_and(tf.equal(y_true,tf.cast(4,'float32')), tf.equal(y_pred, tf.cast(4,'float32')))
    values = tf.cast(values,'float32')
    
    total_sum = tf.reduce_sum(tf.cast(tf.equal(y_true,tf.cast(4,'float32')),'float32'))
    ns = (tf.reduce_sum(values)*cross_sec[4]*L)/total_sum
    
    nb = 0
    for i in range(3):
        values = tf.logical_and(tf.equal(y_true,tf.cast(i,'float32')), tf.equal(y_pred, tf.cast(4,'float32')))
        values = tf.cast(values, 'float32')
        
        total_sum = tf.reduce_sum(tf.cast(tf.equal(y_true,tf.cast(i,'float32')),'float32'))
        nb += (tf.reduce_sum(values)*cross_sec[i]*L)/total_sum
    
    print(ns,nb)
    
    return ns/tf.sqrt(nb)


# In[91]:


class Significance(tf.keras.metrics.Metric):

    def __init__(self, name='significane', **kwargs):
        super(Significance, self).__init__(name=name, **kwargs)
        self.significance = self.add_weight(name='tp', initializer='zeros')

    def update_state(self, y_true, y_pred, sample_weight=None):
        y_pred = tf.argmax(y_pred,axis=1,output_type = 'int32')
        y_pred = tf.cast(y_pred,self.dtype)

        y_true = tf.argmax(y_true,axis=1,output_type = 'int32')
        y_true = tf.cast(y_true,self.dtype)

        cross_sec = [6538.845366086956,91227.27272727272,692.2567850586979,199.5908264705882,0.399]
        L = 3000

        # Signal
        values = tf.logical_and(tf.equal(y_true,tf.cast(4,self.dtype)), tf.equal(y_pred, tf.cast(4,self.dtype)))
        values = tf.cast(values,self.dtype)

        total_sum = tf.reduce_sum(tf.cast(tf.equal(y_true,tf.cast(4,self.dtype)),self.dtype))
        ns = (tf.reduce_sum(values)*cross_sec[4]*L)/total_sum

        nb = 0
        for i in range(3):
            values = tf.logical_and(tf.equal(y_true,tf.cast(i,self.dtype)), tf.equal(y_pred, tf.cast(4,self.dtype)))
            values = tf.cast(values, self.dtype)

            total_sum = tf.reduce_sum(tf.cast(tf.equal(y_true,tf.cast(i,self.dtype)),self.dtype))
            nb += (tf.reduce_sum(values)*cross_sec[i]*L)/total_sum

        self.significance.assign(ns/tf.sqrt(nb))

    def result(self):
        return self.significance


# In[92]:


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
model.add(Dense(5,activation = 'softmax',input_dim = 8))

model.compile(optimizer='adam', loss='binary_crossentropy',metrics=['accuracy',Significance()])


# In[93]:


model.fit(x_train,y_train,epochs=100,batch_size=512,validation_split=0.2,class_weight={0:5,1:7,2:4,3:4,4:.005})


# In[94]:


tot_pred = model.predict(dtset.T[:-2].T)


# In[95]:


def get_back_ax(x):
    return x.argmax(axis=1)


# In[96]:


sol = get_back_ax(tot_pred)


# In[97]:


sol.shape


# In[98]:


sol[2:100]


# In[99]:


pred_set = dtset.copy()
pred_set['pred'] = sol


# In[100]:


cor_pred = len(pred_set[train_len:][pred_set['pred'] == 4][pred_set['tag'] == 1]) + len(pred_set[train_len:][pred_set['pred'] != 4][pred_set['tag'] == 0])
print('The accuracy of the test set is : ',cor_pred/(len(pred_set[train_len:])))


# In[101]:


import warnings
warnings.filterwarnings('ignore')


# In[102]:


print('Correctly identified signal (True Positive)     : ',len(pred_set[pred_set['pred'] == 4][pred_set['tag'] == 1]))
print('Falsely identified signal (False Positive)      : ',len(pred_set[pred_set['pred'] == 4][pred_set['tag'] == 0]))
print('Correctly identified background (True Negative) : ',len(pred_set[pred_set['pred'] != 4][pred_set['tag'] == 0]))
print('Falsely identified background (False Negative)  : ',len(pred_set[pred_set['pred'] != 4][pred_set['tag'] == 1]))


# In[103]:


print('The amount of signal left is     :', len(pred_set[pred_set['pred'] == 4][pred_set['tag'] == 1])/len(df[-1]))
print('The amount of background left is :', len(pred_set[pred_set['pred'] == 4][pred_set['tag'] == 0])/np.sum([len(i) for i in df[:-1]]))


# In[104]:


print('Thus, the rate of correct signal prediction is : ',len(pred_set[pred_set['pred'] == 4][dtset['tag'] == 1])/(len(pred_set[pred_set['pred'] == 4])))


# In[105]:


L = 3000


# In[106]:


ns = cs_corr['n2n2']*(len(pred_set[pred_set['pred'] == 4][pred_set['tag'] == 1])/(no_of_files['n2n2']*1e5))*L
print('n2n2',(len(pred_set[pred_set['pred'] == 4][pred_set['tag'] == 1])),cs_corr['n2n2'])
nb = 0

for i in range(len(files)-1):
    nb += cs_corr[files[i]]*(len(pred_set[pred_set['pred'] == 4][pred_set['tag'] == 0][pred_set['type'] == i])/((no_of_files[files[i]]*1e5)))*L
    print(files[i],len(pred_set[pred_set['pred'] == 4][pred_set['tag'] == 0][pred_set['type'] == i]),cs_corr[files[i]])


# In[107]:


print('The number of signal is :', ns)
print('The number of background is :', nb)
print('The significance is :',ns/np.sqrt(nb))


# In[43]:


df[2].head()


# In[44]:


model.save('/home/iiit/Datasets/Models/s5')

