# style.use('ggplot')
# style.use('fivethirtyeight')
# unicode
# write_file


DataFrame(dic)
dic = {'key':[1,2,3],'key2':[3,4]}
df.set_index('indexname') return a new df /df.set_index('name',inplace = true)
df['columnname'].tolist()/ df.columnname
df = pd.DataFrame(np.array(df[['c','c1']]))
df.to_csv('',header = False)
read_csv(,index_col = 0,names = ['','']) 第一列作为index
df.columns = ['',''] 除index外的列名修改

df.empty
df.tohtml
df.rename()

import Quandl
df = Quandl.get('' , authtoken = open('','r').read())
pd.read_html('')
list[0][0]（html返回列表，列表内容为df，这里取df第一列）

pd.concat([df1,df2]) 
df1.append(df2) 列相同,列名不同则为NaN

s = pd.Series([80,2,3],index = ['df.column1','',''])
df.append(s,ignore_index=True) 追加一行

pd.merge()
join

import pickle
pickle_out =open(path,'wb')
pickle.dump(df,pickle_out)
pickle_out.close()

pickle_in =open(path,'rb')
pickle.load(pickle_in)


data.to_pickle('name')
data2=pd.read_pickle('name')

data2.legend().remove()
data2.show()

plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))
data2.plot(ax = ax1,color = 'k',linewidth = 10, label='')

data.corr() 为所有列correlation table 
df.describe() 基于列给出

df[0].resample('A',how = 'mean') how ='ohlc'


range = pd.date_range('2015-01-01', '2015-12-31', freq='15min')
df.columnname.cumsum()
pd.rolling_mean('',)
pd.rolling_std('',12)










