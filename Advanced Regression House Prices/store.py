def perform_log_transform(df,col_log):
    """#Perform Log Transformation of dataframe , and list of columns """
    for colname in col_log:
        df[colname + '_log'] = np.log(df[colname])
    #df.drop(col_log, axis=1, inplace=True)
    df.info()

def clean(df):

    df["MasVnrType"] = df["MasVnrType"].fillna('None')
    df["MasVnrArea"] = df["MasVnrArea"].fillna(0.0)

    df["Alley"] = df["Alley"].fillna('None')

    #there are few outliers in total basement area lets remove them
    upperlimit = np.percentile(df.TotalBsmtSF.values, 99.5)
    df['TotalBsmtSF'].loc[df['TotalBsmtSF']>upperlimit] = upperlimit

    basement_cols=['BsmtQual','BsmtCond','BsmtExposure','BsmtFinType1','BsmtFinType2','BsmtFinSF1','BsmtFinSF2']
    for col in basement_cols:
        if 'FinSF' not in col:
            df[col] = df[col].fillna('None')

    #GarageArea has got some outliers lets remove them.
    upperlimit = np.percentile(df.GarageArea.values, 99.5)
    df['GarageArea'].loc[df['GarageArea']>upperlimit] = upperlimit

    garage_cols=['GarageType','GarageQual','GarageCond','GarageYrBlt','GarageFinish','GarageCars','GarageArea']
    for col in garage_cols:
        if df[col].dtype==np.object:
            df[col] = df[col].fillna('None')
        else:
            df[col] = df[col].fillna(0)

    #dealing with the LotArea SQRT
    df['SqrtLotArea']=np.sqrt(df['LotArea'])
    df['LotFrontage'].corr(df['SqrtLotArea'])
    df.drop(['LotArea'], axis='columns', inplace=True)

    filter = df['LotFrontage'].isnull()
    df.LotFrontage[filter]=df.SqrtLotArea[filter]

    #  making a list of categorical columns

    catCol = []
    for i in df.columns.to_list():
        dataTypeObj = df.dtypes[i]
        if (dataTypeObj == "object"):
            catCol.append(i)
    
        #If PoolArea is 0, that means that df doesn't have a pool.
    #So we can replace PoolQuality with None.
    df["PoolQC"] = df["PoolQC"].fillna('None')
    df["Fence"] = df["Fence"].fillna('None')
    df["MiscFeature"] = df["MiscFeature"].fillna('None')
    df["FireplaceQu"] = df["FireplaceQu"].fillna('None')

    #Let's confirm that we have removed all missing values
    df.isnull().sum()

    

