import pandas as pd

# company_data = pd.read_excel("./data/preprocess_data/brand_model.xlsx")
# company_data.to_csv("./data/preprocess_data/brand_model.csv")
# get the company and type info
company_data = pd.read_csv("./data/preprocess_data/brand_model.csv")
companys = company_data["company"].to_list()
types = company_data["type"].to_list()

delete_list = [" ", "-"]
new_type = []
for type in types:
    # delete " ", "-" in type
    for delete_item in delete_list:
        if delete_item in type:
            type = "".join(type.split(delete_item))

    # lower character in type
    type = type.lower()
    new_type.append(type)

# lower character in company
new_company = []
for company in companys:
    company = company.lower()
    new_company.append(company)

company_type_list = list(zip(new_company, new_type))

# delete the duplicate items
deweight_company_type_list = list(set(company_type_list))

deweight_company_list = []
deweight_type_list = []
for company_type in deweight_company_type_list:
    deweight_company_list.append(company_type[0])
    deweight_type_list.append(company_type[1])

# write into csv
df = pd.DataFrame()
df["company"] = deweight_company_list
df["type"] = deweight_type_list
df.to_csv("./data/preprocess_data/processed_company_type.csv", index=False)

