import pandas
import zipfile
import os

datapath = ('Enter file path: ')

os.chdir(datapath)

df_list = ['Plan name', 'Plan ID', 'Zip code', 'Group Size', 'EE', 'ES', 'EC', 'FAM', 'Ortho EE', 'Ortho ES', 'Ortho EC', 'Ortho FAM']

#List of states in column A to filter and grab corresponding data
df_states = ['AL', 'AR', 'AZ']

# Returns a DataFrame
df = pd.read_excel("2021 UHC Dental Rates Parser Sheet.xlsx", converter = {'Zip Code': '{:0>3}'.format})

# Start of loop for each state and corresponding data
for item in df_states:

# To select rows whose column value equals a condition 'mask', some_value, use ==:
# mask = function return an obj. of same shape as self and corresponding entries
    mask = df ['State Abbrev.'].valus == item

# To select rows whose cilumn calue is in an iterable, some_values, use isin:
    df_new = df[df_list]

# New DataFrame
    df_new = df[mask]

# del is also an option, you can delete a column by del df['Column Name']
# The Python would map this operation to df.__delitem__('Column name'), Which is an internal method of DataFrame
    del df_new["State Abbrev."]

# Save data with different file names 'item' == State Abbrev. Index = False drops/removes unamed column [0]
    df_new.to_excel("2021"+item+" UHC Rates Upload.xlsx", index = False)

#This code will create a new ZIP file names 2021 XX Ameritas/UHC ZIP.zip that has the compressed contents of 2021 +State+Ameritas Rates Upload.xlsx
    newZip = zipfile.ZipFile('2021 '+item+' UHC Zip.zip', 'w')

    newZip.write("2021 "+item+" UHC Rates Upload.xlsx", compress_type=zipfile.ZIP_DEFLATED)

    newZip.write("2021 UHC SIC Code.xlsx", compress_type=zipfile.ZIP_DEFLATED)

    newZip.write("2021 UHC Group Life Factors.xlsx", compress_type=zipfile.ZIP_DEFLATED)

    newZip.close()

# Deletes/Removes ALL extra RateUPLOAD File that is not in .ZIP
filelist = [ f for f in os.listdir(datapath) if f.endswith("Upload.xlsx") ]
for f in filelist:
    os.remove(os.path.join(datapth, f))