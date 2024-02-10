# from openpyxl import load_workbook
#
# from testCases.test_login import Test_001_Login

# workbook = load_workbook("C:\\Users\\Administrator\\Desktop\\Book1.xlsx")
# sheet = workbook.active
# data = []
# for row in sheet.iter_rows(min_row=1, values_only=True):
#     data.append(row)
#     print(data)
#
# print(sheet["A1"].value)
dict1 = {"name":"Rajesh", "class":"1st class", "sal" : 1000, "desg" : "tester"}
for i in dict1:
    print(i,dict1[i],sep="|")
dict1.update({"last":"value"})
for i in dict1:
    print(i,dict1[i],sep="|")
print(dict1.popitem())
dict1["name"] = "Raj"
print(dict1)




