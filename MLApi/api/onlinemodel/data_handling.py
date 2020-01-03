import os
import json
import numpy as np 
import pandas as pd 

# print(os.getcwd())
class dataHandler():
    def __init__(self, dataset_name):
        self.dataset_name  = dataset_name
        # parent_dir = os.getcwd()
        # directory = "data"
        # path = os.path.join(parent_dir, directory)
        # self.path = path

        if not os.path.isdir("data"):
            os.mkdir("data")

    def save_records(self, record):
        print("save_records called with : {} ".format(record))
        if not os.path.isdir("data/{}".format(self.dataset_name)):
            os.mkdir("data/{}".format(self.dataset_name))
        # col names
        with open("data/{}/{}.csv".format(self.dataset_name, "column_names"), "w") as f:
            l = ",".join([str(x) for x in list(record.keys())])
            f.writelines(l)
        with open("data/{}/{}.csv".format(self.dataset_name, "values"), "a") as f:
            l = ",".join([str(x) for x in list(record.values())])
            
            f.writelines(l + "\n")
    
    
    def get_records(self):
        print("get_records called with : {} ".format(self.dataset_name))
       
        with open("data/{}/{}.csv".format(self.dataset_name, "column_names"), "r") as f:
            col_names = [line.rstrip().split(",") for line in f][0]
            
        with open("data/{}/{}.csv".format(self.dataset_name, "values"), "r") as f:
            data = [line.rstrip().split(",") for line in f]
        df = pd.DataFrame(data)
        df.columns = col_names  
        print(df)
        return data,col_names

    def get_mean(self):
        print("get_records called with : {} ".format(self.dataset_name))
       
        with open("data/{}/{}.csv".format(self.dataset_name, "column_names"), "r") as f:
            col_names = [line.rstrip().split(",") for line in f][0]
            
        with open("data/{}/{}.csv".format(self.dataset_name, "values"), "r") as f:
            data = [line.rstrip().split(",") for line in f]
        df = pd.DataFrame(data)
        df.columns = col_names
        df = df.apply(lambda x : x.astype("float"))
        data_dict = {}
        for k in col_names:
            data_dict[k] = {"mean" : df.loc[:,k].mean(),
                            "min" : df.loc[:,k].min(),
                            "max" : df.loc[:,k].max()}
        return data_dict

