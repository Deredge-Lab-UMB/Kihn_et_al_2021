
###
Script used to process the ideal fitting gamma value *_final_weights.dat file from the HDXer reweighing into a weights file useable for the iterative TICA clustering described in Kihn et. al., 2021.
###



import pandas as pd



file_path = '/home/dderedge/Desktop/HDXer_and_Clustering_Tutorial/Reweighting/Demo_Data/ERK2_SCH_w_Mg_2x10^0_final_weights.dat'
save_loc = '/home/dderedge/Desktop/HDXer_and_Clustering_Tutorial/Clustering/'


def load_exp(file_path):
    df = pd.read_csv(file_path, sep="\s+", header=None)
    df.columns = ["Weight"]
    df.at['Frame'] = ''
    x = 0
    for row in df.iterrows():
            df.at[x, 'Frame'] = x
            x = x + 1
    df.drop(df.tail(2).index, inplace=True)
    return df


def find_top_5(df, save_loc):
    df = df.sort_values('Weight', ascending=False)
    df.to_csv(save_loc + 'Weights_labeled.csv', index=False)
    return df


new_df = load_exp(file_path)
df2 = find_top_5(new_df, save_loc)
