import openpyxl


class testrun():
    def open(path):
        df = openpyxl.load_workbook(path)
        sheet = df["闭环转标注"]
        test_data = []
        for x in range(2, 3):
            data = []
            for y in range(5,9):
                d = sheet.cell(x,y).value
                data.append(d)
            test_data.append(data)
        print(test_data[0][0])


testrun.open("/Users/bytedance/Downloads/testcase.xlsx")

space_id = 1012
token = "管理"
tokenb = "标注"

headers = {
    "Algorithm-Space": space_id,
    "Content-Type": "application/json",
    "token": token
}

headers["Algorithm-Space1"] = space_id
# print(headers)
