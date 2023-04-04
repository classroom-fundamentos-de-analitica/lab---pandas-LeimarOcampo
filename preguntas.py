import pandas as pd

tb0 = pd.read_csv("tbl0.tsv", sep="\t")
tb1 = pd.read_csv("tbl1.tsv", sep="\t")
tb2 = pd.read_csv("tbl2.tsv", sep="\t")

def pregunta_01():
    return len(tb0)

def pregunta_02():
    return tb0.shape[1]

def pregunta_03():
    return tb0['_c1'].value_counts().sort_index(0)

def pregunta_04():
    return tb0.groupby('_c1')["_c2"].mean()

def pregunta_05():
    return tb0.groupby('_c1')['_c2'].max()

def pregunta_06():
    x = tb1['_c4'].str.upper().unique()
    return sorted(x)

def pregunta_07():
    return tb0.groupby('_c1')['_c2'].sum()

def pregunta_08():
    x = tb0
    x['suma'] = x['_c0'] + x['_c2']
    return x

def pregunta_09():
    x = tb0
    x['year'] = x['_c3'].str[0:4]
    return x

def pregunta_10():

    x = tb0
    y = x.groupby('_c1').agg({'_c2': lambda x: sorted(list(x))})
    for index, row in y.iterrows():
        row['_c2'] = ":".join([str(int) for int in row['_c2']])
    return y

def pregunta_11():

    x = tb1
    y = x.groupby('_c0').agg({'_c4': lambda x: sorted(list(x))})
    for index, row in y.iterrows():
        row['_c4'] = ",".join([str(int) for int in row['_c4']])
    y.insert(0, '_c0', range(0, 40))
    return y

def pregunta_12():

    x = tb2
    x['_c5'] = x['_c5a'] + ':' + x['_c5b'].astype(str)
    y = x.groupby('_c0').agg({'_c5': lambda x: sorted(x)})
    for index, row in y.iterrows():
        row['_c5'] = ",".join([str(int) for int in row['_c5']])
    y.insert(0, '_c0', range(0, 40))
    return y

def pregunta_13():

    x = pd.merge(
        tb0,
        tb2,
        how="outer",
    )
    return x.groupby('_c1')['_c5b'].sum()
