import sys
from rdkit import Chem 
import pandas as pd
import numpy as np
import pickle,os    
import csv
from hob_predict import model_predict

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__)) 
modelpt = os.path.abspath(os.path.join(root, "..", "..", "checkpoints")) 

cutoffs = ['20', '50']
def my_model(smiles):  
    mols = [Chem.MolFromSmiles(smi) for smi in smiles]
    mols_right = []
    smiles_right=[]
    right_num = []
    mols_false = []
    smiles_false=[]
    false_num = []
    for i in range(len(mols)):
        if mols[i] != None:
            right_num.append(i)
            mols_right.append(mols[i])
            smiles_right.append(smiles[i])
        else:
            false_num.append(i)
            mols_false.append(mols[i])
            smiles_false.append(smiles[i])

    df_error=pd.DataFrame()
    df_right=pd.DataFrame()
    df_error['num'] = false_num
    df_error['smiles']=smiles_false
    df_right['num']=right_num
    df_right['smiles'] = smiles_right
    # get predictions for each cuttoff
    df_right['P(high)_HOB>20%'] = model_predict('20',smiles_right, mols_right, right_num,modelpt)
    df_right['P(high)_HOB>50%'] = model_predict('50',smiles_right, mols_right, right_num,modelpt)
    df = pd.concat([df_right,df_error],axis=0) 
    # Sort the DataFrame by the "smiles" column while preserving the original order
    df = df.sort_values('smiles', key=lambda x: x.map({**{smile: i for i, smile in enumerate(smiles)}, **{}}))

    # Fill NaN values with 'invalid smile' if 'smiles' column is not empty
    mask = df['smiles'] != ''
    df.loc[mask, ['P(high)_HOB>20%', 'P(high)_HOB>50%']] = df.loc[mask, ['P(high)_HOB>20%', 'P(high)_HOB>50%']].fillna('invalid smile')
    # print(df)
    # add each pair of the cutoff predictions as one output   
    predictions = df[['P(high)_HOB>20%', 'P(high)_HOB>50%']].values.tolist() 

    return predictions


# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs = my_model(smiles_list)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(['P(high)_HOB>20%', 'P(high)_HOB>50%'])  # header
    for r in outputs:
        writer.writerow(r)