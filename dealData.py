import pandas as pd
import re
import openpyxl

if __name__ == '__main__':
    # df = pd.read_excel('./3.23.24直播间信息.xlsx')
    # for i in range(df.shape[0]):
    #     if re.match('.*万', df.loc[i, '热度']):
    #         number = int(float(df.loc[i, '热度'].strip('万')) * 10000)
    #         df.loc[i, '热度'] = number
    # df.to_excel('./3.23.24直播间信息.xlsx', index=False)
    document_name = './3.23.24分区热度.xlsx'
    excel_reader = pd.ExcelFile(document_name)
    sheet_names = excel_reader.sheet_names
    temp = []
    for i in range(5):
        df = pd.read_excel(document_name, sheet_name=sheet_names[i])
        for j in range(df.shape[0]):
            if re.match('.*万', str(df.loc[j, '热度'])):
                number = int(float(df.loc[j, '热度'].strip('万')) * 10000)
                df.loc[j, '热度'] = number
            elif re.match('.*亿', str(df.loc[j, '热度'])):
                number = int(float(df.loc[j, '热度'].strip('亿')) * 100000000)
                df.loc[j, '热度'] = number
        temp.append(df)
    excel_writer = pd.ExcelWriter(document_name)
    for i in range(5):
        df1 = temp[i]
        df1.to_excel(excel_writer, sheet_name=sheet_names[i], index=False)
    excel_writer.close()

