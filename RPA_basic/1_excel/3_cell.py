from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Nadosheet"

ws["A1"] = 1
ws["A2"] = 2
ws["A3"] = 3

ws["B1"] = 4
ws["B2"] = 5
ws["B3"] = 6

print(ws["A1"]) # A1 셀의 정보를 출력
print(ws["A1"].value) # A1 셀의 '값'을 출력
print(ws["A10"].value) # 값이 없을 땐 'None'출력


# row = 1,2,3,....
# column = A, B, C, ....
print(ws.cell(row=1, column=2).value)

ws.cell(row=1, column=3, value=10) #C1 에 10 입력

wb.save("sample.xlsx")
