import time
import pandas as pd
BANKS ={
        "STATE BANK OF INDIA" : "sbi",
        "ICICI BANK LIMITED" : "icici",
        "ICICI BANK" : "icici",
        "ICICI" : "icici",
        "AXIS BANK" : "axis",
        "KOTAK MAHINDRA BANK LIMITED" : "kotak",
        "HDFC BANK" : "hdfc",
        "HDFC" : "hdfc",
        "HDFC BT" : "hdfc",
        "IDBI BANK" : "idbi",
        "BANK OF INDIA" : "boi",
        "INDIAN OVERSEAS BANK" : "iob",
        "ANDHRA BANK" : "andhra",
        "INDUSIND BANK" : "indusind",
        "INDIAN BANK" : "indbnk",
        "SYNDICATE BANK" : "syndicate",
        "UNITED BANK OF INDIA" : "ubi",
        "IDFC FIRST BANK" : "idfc",
        "CORPORATION BANK" : "corporation",
        "KARUR VYSYA BANK" : "karur",
        "VIJAYA BANK" : "vijaya",
        "DENA BANK" : "dena",
        "FEDERAL BANK" : "federal",
        "CENTRAL BANK" : "central",
        "YES BANK" : "yesbnk",
        "PUNJAB NATIONAL BANK" : "pnbbnk",
        "CANARA BANK" : "canara",
        "ORIENTAL BANK OF COMMERCE" : "obc",
        "BANK OF BARODA" : "baroda"
    }

start= time.time()

# bank_df = pd.DataFrame(list(BANKS.items()), columns=['Bank Name', 'bank_name'])
# bank_name = bank_df.loc[bank_df['Bank Name'] == "HDFC",'bank_name'].item()
bank_df = pd.DataFrame(BANKS.items())
bank_name = bank_df[bank_df[0] == "hdfc"]
print(bank_name)
print "{:.16f} df".format(float(time.time() - start))
for_start = time.time()
b="HDFC"
if b in BANKS:
    for i in BANKS.keys():
        if b == i:
            print BANKS.get(i)


# for i in BANKS:
#     if b == BANKS[i]:
#         print i

# print(a)

print "{:.16f} for".format(float(time.time() - for_start))