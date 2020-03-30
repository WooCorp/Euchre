#Euchre Simulation Data Processing
# Ben Gochanour
# Last Modified 18 February, 2020

# Imports and Helper Function Definitions

import pandas as pd
import os
import glob

# Define Helper Functions
def is_Euched(num):
    if num==0:
        val=1
    else:
        val=0
    return val

def is_Majority(num):
    if num==1:
        val=1
    else:
        val=0
    return val

def is_AllFive(num):
    if num==2:
        val=1
    else:
        val=0
    return val

# Get file names and divide into groups of 14
os.chdir("C:\\Users\\Ben Gochanour\Documents\GitHub\EuchreBot\\Raw Data\\SS Lone")
path="C:\\Users\\Ben Gochanour\Documents\GitHub\EuchreBot\\Raw Data\\SS Lone"

all_files = glob.glob(path + "/*.csv")


n = 14 # Define a chunk size
files_list = [all_files[i*n:(i + 1)*n] for i in range((len(all_files)+n-1)//n)]  
len(files_list)

result=[]

n_files=0

# Process Data
for sublist in files_list:
    data = pd.concat((pd.read_csv(f,sep=",", header=None) for f in sublist),sort=False)
    print("Data Read In")
    data.columns=["Pos","Top","C1","C2","C3","C4","C5","Result"]
    data["Euched"]=data["Result"].map(is_Euched)
    data["Majority"]=data["Result"].map(is_Majority)
    data["AllFive"]=data["Result"].map(is_AllFive)
    print("Basic Processing Done")
    
    data['TotEuched']=data.groupby(['Pos',"Top","C1", "C2","C3","C4","C5"])['Euched'].transform(func='sum')
    data['TotMajority']=data.groupby(['Pos',"Top","C1", "C2","C3","C4","C5"])['Majority'].transform(func='sum')
    data['TotAllFive']=data.groupby(['Pos',"Top","C1", "C2","C3","C4","C5"])['AllFive'].transform(func='sum')
    print("Advanced Processing Done!")
    
    data=data.drop_duplicates(subset=['Pos',"Top","C1", "C2","C3","C4","C5"])
    data=data.drop(columns=["Result","Euched","Majority","AllFive"])
    result.append(data)
    n_files=n_files+n
    print("Number of Files Processed:")
    print(n_files)
    

# Second batching step
result_list = [result[i*n:(i + 1)*n] for i in range((len(result)+n-1)//n)]  
len(result_list)


result_list
last_step=[]
for df in result_list:
    df=pd.concat(df)
    df['TotEuched']=df.groupby(['Pos',"Top","C1", "C2","C3","C4","C5"])['TotEuched'].transform(func='sum')
    df['TotMajority']=df.groupby(['Pos',"Top","C1", "C2","C3","C4","C5"])['TotMajority'].transform(func='sum')
    df['TotAllFive']=df.groupby(['Pos',"Top","C1", "C2","C3","C4","C5"])['TotAllFive'].transform(func='sum')
    df=df.drop_duplicates(subset=['Pos',"Top","C1", "C2","C3","C4","C5"])
    last_step.append(df)

final_result=pd.concat(last_step)
final_result['TotEuched']=final_result.groupby(['Pos',"Top","C1", "C2","C3","C4","C5"])['TotEuched'].transform(func='sum')
final_result['TotMajority']=final_result.groupby(['Pos',"Top","C1", "C2","C3","C4","C5"])['TotMajority'].transform(func='sum')
final_result['TotAllFive']=final_result.groupby(['Pos',"Top","C1", "C2","C3","C4","C5"])['TotAllFive'].transform(func='sum')
final_result["TotOverall"]=final_result["TotEuched"]+final_result["TotMajority"]+final_result["TotAllFive"]
final_result=final_result.drop_duplicates(subset=['Pos',"Top","C1", "C2","C3","C4","C5"])

# Write CSV
final_result.to_csv("ShortSuitLone_Chunk1_FinalResults.csv") #change this each time


#len(final_result)
# Read in CSVs and combine them
#os.chdir("C:\\Users\\Ben Gochanour\\Documents\\GitHub\\EuchreBot\\Processed Data")
#data1=pd.read_csv("Loner_Processed_Data1.csv")
#data2=pd.read_csv("Loner_Processed_Data2.csv")
#data3=pd.read_csv("Loner_Processed_Data3.csv")
#df=pd.concat([data1,data2,data3])
df=final_result
df['TotEuched']=df.groupby(['Pos',"Top","C1", "C2","C3","C4","C5"])['TotEuched'].transform(func='sum')
df['TotMajority']=df.groupby(['Pos',"Top","C1", "C2","C3","C4","C5"])['TotMajority'].transform(func='sum')
df['TotAllFive']=df.groupby(['Pos',"Top","C1", "C2","C3","C4","C5"])['TotAllFive'].transform(func='sum')
df=df.drop_duplicates(subset=['Pos',"Top","C1", "C2","C3","C4","C5"])

df["TotOverall"]=df["TotEuched"]+df["TotMajority"]+df["TotAllFive"]
df['PctEuched']=df["TotEuched"]/df['TotOverall']
df['PctMajority']=df["TotMajority"]/df['TotOverall']
df['PctAllFive']=df["TotAllFive"]/df['TotOverall']
# Changed this to +4 for loners
df['ExpectedPoints']=df['PctEuched']*-2+df['PctMajority']*1+df['PctAllFive']*2

os.chdir("C:\\Users\\Ben Gochanour\Documents")
df.to_csv("ShortSuitLone_Chunk1_FinalResults.csv")

df['TotOverall'].sum() # total processed
# 567 million for regular
# 532 million for loner
# 567867167
len(df)/807576 # coverage # Now we have overcoverage, just remove extras and
# should be good
#94.76 coverage

# Check for which hands are missing and which are extras
os.chdir("C:\\Users\\Ben Gochanour\\Documents\\GitHub\\EuchreBot\\RawData")
final_result=pd.read_csv("Loner_Processed_Data1.csv")
os.chdir("C:\\Users\\Ben Gochanour\\Documents\\GitHub\\EuchreBot")
final_result
allscenarios=pd.read_csv("AllScenarios.txt",sep=",", header=None)
allscenarios=allscenarios.iloc[0:len(allscenarios),0:7]
allscenarios.columns=["Pos","Top","C1","C2","C3","C4","C5"]

allscenarios
common=final_result.merge(allscenarios,on=["Pos","Top","C1","C2","C3","C4","C5"])

len(common)

common.to_csv("OrderUp_FinalResults.csv")

testing = final_result.merge(allscenarios, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='left_only']
testing2=final_result.merge(allscenarios, how = 'outer' ,indicator=True).loc[lambda x : x['_merge']=='right_only']
 
extras=testing[testing["_merge"]=="left_only"]
missing=testing2[testing2["_merge"]=="right_only"]

extras

extras=extras.iloc[0:len(extras),0:7]
missing=missing.iloc[0:len(missing),0:7]
missing
extras.to_csv("Extras.csv")
missing.to_csv("Missing.csv")


final_result[(~final_result.Pos.isin(common.Pos)) & (~final_result.Top.isin(common.Top))
& (~final_result.C1.isin(common.C1)) & (~final_result.C2.isin(common.C2))
& (~final_result.C3.isin(common.C3)) & (~final_result.C4.isin(common.C4)) &
(~final_result.C5.isin(common.C5))]


# Random Exploration
final_result[final_result.ExpectedPoints>0]
final_result['ExpectedPoints'].mean()



final_result=final_result.sort_values(by="PctMajority",ascending=False)
final_result.head(20)

807576-len(final_result)
final_result[final_result['PctEuched']==.5]

final_result[(final_result["Pos"]==3) & (final_result["Top"]==6)]

final_result[(final_result["Pos"]==3) & (final_result["Top"]==5) & (final_result["C1"]==6)
             & (final_result["C2"]==7) & (final_result["C3"]==9) & (final_result["C4"]==15)
             & (final_result["C5"]==20)]



final_result.TotOverall.mean()