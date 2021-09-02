import camelot



# PDF file to extract tables from
file = "2021.pdf"

# extract all the tables in the PDF file
tables = camelot.read_pdf(file)

# number of tables extracted
#print("Total tables extracted:", tables.n)

# print the first table as Pandas DataFrame
print(tables[0].df)