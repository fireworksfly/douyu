import pandas as pd

if __name__ == '__main__':
    headers = ['房间号', '标题', '主播名', '主播称号', '热度', '分区']
    df_lol = pd.read_excel('./英雄联盟.xlsx')
    df_wz = pd.read_excel('./王者荣耀.xlsx')
    df_yz = pd.read_excel('./颜值.xlsx')
    df_yzh = pd.read_excel('./颜值横屏.xlsx')
    df = pd.DataFrame(columns=headers)
    df.to_excel('./直播间信息.xlsx', index=False)
    excel_writer = pd.ExcelWriter('./直播间信息.xlsx')
    df_lol.to_excel(excel_writer, sheet_name='英雄联盟', index=False)
    df_wz.to_excel(excel_writer, sheet_name='王者荣耀', index=False)
    df_yz.to_excel(excel_writer, sheet_name='颜值', index=False)
    df_yzh.to_excel(excel_writer, sheet_name='颜值横屏', index=False)
    excel_writer.close()
