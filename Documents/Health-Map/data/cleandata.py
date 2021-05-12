import pandas as pd
import string

data = pd.read_csv("data/inspections.csv")

# keep only the latest inspection at each facility
data.drop_duplicates(subset ="Facility_ID", keep = "last", inplace = True)

# delete all unnecessary columns in th edata
deletions = ["X", "Y", "OBJECTID", "Facility_ID", "ExternalID", "State", "Zip", "Service", "Activity_Date", "GlobalID"]
for column in deletions:
  data.pop(column)
  
# format capitalization for the address and facility name 
data["Facility_Name"] = data["Facility_Name"].apply(lambda x: string.capwords(x))
data["Address"] = data["Address"].apply(lambda x: string.capwords(x))

# format inspector comments to not include unnecessary quotes
data["Violation_Description"] = data["Violation_Description"].apply(lambda x: x.strip('"'))

# limit dataset to only include facilities in selected cities that have a grade
trivalleydata = data[data.City.isin(["DUBLIN", "PLEASANTON", "LIVERMORE", "FREMONT", "SUNOL", "NEWARK", "OAKLAND"]) & data.Grade.isin(["G", "Y", "R"])]
trivalleydata.pop("City")

# export data
trivalleydata.to_csv("data/trivalley.csv", index = False)

jsarray = [list(row) for row in trivalleydata.values]
print(jsarray)
