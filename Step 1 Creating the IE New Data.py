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
# We are taking the first observations for a reason, three project id, have more than one observation 
# about 2021 adoption, including Before CN Review, Afte Reviwe, but we need the latest observation ,
# In this case, the data is descending order of dates, hence we take the latest one
ie_data.drop_duplicates(subset = ["ProjectId"], keep = "first", inplace = True)

# Make a column with IE = 1, to represent the projects that attended
ie_data["IE"] = 1

# Output the dataset 
ie_data.to_csv("ie 2021 Data New.csv", index = False)

#%%

# Reading the Adoption Final File  
adoption = pd.read_excel("Adoption_final.xlsx")

# Left Merging the adoption final with the ie_data based on WB Project ID
merge_together = pd.merge(adoption,ie_data, left_on = "project_id", 
                          right_on = "ProjectId", how = "left" )

# Reading the operations data
operationsdata = pd.read_excel("PROJECT_MASTER_V2.xlsx")

# Selected Columns from the final dataset
# Selecting the neccessry columns from the merged data, the deleted columns 
# Either are entirely null or do not possess any relevance to the study

columns  = [
"PROJ_ID                "
,"PROJ_DISPLAY_NAME      "
,"PROJ_APPRVL_FY         "
,"CNTRY_CODE             "
,"CNTRY_LONG_NAME        "
,"RGN_ABBR_CODE          "
,"RGN_NAME               "
,"PROD_LINE_CODE         "
,"PROD_LINE_NAME         "
,"PROD_LINE_TYPE_CODE    "
,"PROJ_PHASE_NAME        "
,"PROJ_STAT_NAME         "
,"TEAM_LEAD_UPI          "
,"TEAM_LEAD_FULL_NAME    "
,"CO_TEAM_LEAD1_UPI      "
,"CO_TEAM_LEAD2_UPI      "
,"CO_TEAM_LEAD1_FULL_NAME"
,"CO_TEAM_LEAD2_FULL_NAME"
,"PROJ_DROP_DATE         "
,"PROJ_DROP_FY           "
,"LEAD_GP_CODE           "
,"LEAD_GP_NAME           "
,"JOINT_IFC_IND          "
,"FRAGILE_STATE_IND      "
,"INC_GRP_CODE           "
,"IS_ASA                 "
,"IS_RAS                 "
]

strip_column_names = [i.strip() for i in columns ]

# Strip the column names to remove the white spaces from the dataset
operationsdata_new = operationsdata[strip_column_names]

# Merging the above dataset with the operationsdata_new
left_join = pd.merge(adoption, operationsdata_new, 
                     left_on = "project_id", right_on = "PROJ_ID",
                     how = "left")

# Send the data to an excel file 
left_join.to_excel("AdoptionFinal_OperationsData.xlsx", index = False)
#%%
 
## Reading the Wb project and ooperations data from api for closing date and other relevant inforamtion
wb_op_projectdata = pd.read_excel("World_Bank_Projects_downloaded_8_2_2021.xls")

# Selecting the important columns from the data 
wb_op_projectdata = wb_op_projectdata[['id', 'pdo', 'impagency', 'cons_serv_reqd_ind', 'url',
       'boardapprovaldate', 'closingdate', 'projectfinancialtype',
       'curr_project_cost', 'curr_ibrd_commitment', 'curr_ida_commitment',
       'curr_total_commitment', 'grantamt', 'borrower', 'lendinginstr',
       'envassesmentcategorycode', 'esrc_ovrl_risk_rate', 'sector1', 'sector2',
       'sector3', 'theme1', 'theme2']]

# left join Adoption final, operations combined data with the API DATA
left_join2 = pd.merge(left_join,wb_op_projectdata, 
                      left_on = "PROJ_ID" , right_on = "id" )
# Get the excel; file of all the dat a
left_join2.to_excel("AdoptionFinal_OperationsData_ProjectData.xlsx", index = False)
#%%

#Join the IE data with the combination of Adoption Final, Operations and Project Data
left_join3 = pd.merge(left_join2,ie_data, left_on = "project_id", right_on= "ProjectId" , how = "left")

# Get the excel; file of all the data combined
left_join3.to_excel("AdoptionFinal_OperationsData_ProjectData_IE20201.xlsx", index = False)
#%%
