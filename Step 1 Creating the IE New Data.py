# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Importing all the libraries
import pandas as pd 
import numpy as np 

# Building the IE Database from IE 2021 Data


# Reading the IE 2021 Database from the folder
ie_data = pd.read_excel("2021.07.14_MyIE_Database - Copy.xlsx")

# Selecting the required columns from the entire database
ie_data= ie_data[["unique_id"
,"phase"
,"ietitle"
,"iecode"
,"TTL"
,"TTL_dime"
,"i2i_type"
,"prev_i2i"
,"i2i_call"
,"Unit"
,"region"
,"country"
,"fcs_country"
,"ida_country"
,"income_country"
,"wb_network"
,"program"
,"GP"
,"theme"
,"CCSA"
,"Gender"
,"sectorFCS",
"cn_yes"
,"CN_rev_date"
,"ie_start_date"
,"ie_end_date"
,"status"
,"status_followup_no"
,"WBG_proj_associated"
,"WBG_proj_ID"
,"WBG_proj_name"
,"WBG_proj_TTL_name"
]]

# Renaming the columns
ie_data.columns = ["unique_id"
,"phase"
,"ietitle"
,"iecode"
,"TTL"
,"TTL_dime"
,"i2i_type"
,"prev_i2i"
,"i2i_call"
,"Unit"
,"region"
,"country"
,"fcs_country"
,"ida_country"
,"income_country"
,"wb_network"
,"program"
,"GP"
,"theme"
,"CCSA"
,"Gender"
,"sectorFCS",
"cn_yes"
,"CN_rev_date"
,"ie_start_date"
,"ie_end_date"
,"status"
,"status_followup_no"
,"WBG_proj_associated"
,"ProjectId"
,"WBG_proj_name"
,"WBG_proj_TTL_name"]

# Drop the rows with the Null values from the dataset 
ie_data.dropna(subset = ['ProjectId'], inplace = True)

# Keep the first observation of the Project ID with multiple observations
ie_data.drop_duplicates(subset = ["ProjectId"], keep = "first", inplace = True)

# Make a column with IE = 1, to represent the projects that attended
ie_data["IE"] = 1

# Output the dataset 
ie_data.to_csv("ie 2021 Data New.csv", index = False)
