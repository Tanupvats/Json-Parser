from combination_check import comb_check


###############----------------------json check-----------------------##################


file_name = "brand_info-India (1).json"
with open(file_name, "r") as f:
    data = f.read()
resl_data = comb_check(data.strip())
if resl_data is not None:
    print(resl_data)
    print("-------congrats bitch this shit is working --------")
else:
    print("---------oops ! this shit is fucked up----------")