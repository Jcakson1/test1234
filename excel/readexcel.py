import os
import openpyxl

# 全局变量，用于保存工作簿和工作表对象
from config.read_ini import read_ini_file

import openpyxl

def read_excel_data(file_path, sheet_name, row, column):
    """
    读取 Excel 表格中指定单元格的数据
    :param file_path: Excel 文件的路径
    :param sheet_name: 表格名称
    :param row: 行号（从1开始）
    :param column: 列号（从1开始）
    :return: 单元格中的数据
    """
    # 打开 Excel 文件
    workbook = openpyxl.load_workbook(file_path)

    # 获取指定的工作表
    sheet = workbook[sheet_name]

    # 获取指定单元格的数据
    cell_value = sheet.cell(row=row, column=column).value

    # 关闭 Excel 文件
    workbook.close()

    return cell_value

def read_excel_locator(file_path, sheet_name, row, column):
    """
    读取 Excel 表格中指定单元格的定位方法和定位元素，并拆分为元组返回
    :param file_path: Excel 文件的路径
    :param sheet_name: 表格名称
    :param row: 行号（从1开始）
    :param column: 列号（从1开始）
    :return: (定位方法, 定位元素) 元组
    """
    # 读取合并的定位字符串
    locator_str = read_excel_data(file_path, sheet_name, row, column)

    # 将 locator_str 拆分为定位方法和定位元素
    locator_parts = locator_str.split(',')
    if len(locator_parts) == 2:
        method = locator_parts[0].strip()
        value = locator_parts[1].strip()
        return method, value
    else:
        # 处理拆分失败的情况
        print("Invalid locator format:", locator_str)
        # 或者抛出异常
        raise ValueError("Invalid locator format: " + locator_str)

# if __name__ == '__main__':
    # # 用法示例：
    # config_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.ini')
    #
    # # 调用read_ini_file函数并接收返回的三个值
    # project_path, full_login_Excel_element, full_login_Excel_path = read_ini_file(config_file_path)
    #
    # # file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.xlsx')
    # # 打开 full_login_Excel_element 这个目录文件
    # open_excel(full_login_Excel_element)
    #
    # # 调用 read_excel_cell 方法获取指定单元格数据
    # row = 2
    # col_num = 2
    # cell_value = read_excel_cell(row,col_num)
    # cell_value1 = read_excel_data(full_login_Excel_element,"Sheet1",2,2)
    # print(cell_value1)
    # if cell_value is not None:
    #     print(f"在 {sheet.title}工作表的第 {row} 行，第 {col_num} 列的单元格数据为：", cell_value)
    # else:
    #     print("读取单元格数据失败。")


# # 示例用法
# file_path = "path/to/excel.xlsx"
# sheet_name = "Sheet1"
# locator_row = 2
# locator_column = 2
# method, value = read_excel_locator(file_path, sheet_name, locator_row, locator_column)

# # 使用定位方法和定位元素进行定位
# element = driver.find_element(method, value)

# def read_excel_cell_from_config(config_file_path, sheet_name, row, column):
#     """
#     从配置文件指定的 Excel 表格中读取指定单元格的数据
#     :param config_file_path: 配置文件的路径
#     :param sheet_name: 表格名称
#     :param row: 行号（从1开始）
#     :param column: 列号（从1开始）
#     :return: 单元格中的数据
#     """
#     # 构建Excel文件的绝对路径
#     config_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.ini')
#
#     # 调用read_ini_file函数并接收返回的三个值
#     project_path, full_login_Excel_element, full_login_Excel_path = read_ini_file(config_file_path)
#     # 打开Excel文件
#     open_excel(full_login_Excel_element)
#
#     # 调用read_excel_cell方法获取指定单元格数据
#     cell_value = read_excel_cell(row, column)
#
#     if cell_value is not None:
#         print(f"在 {sheet.title} 工作表的第 {row} 行，第 {column} 列的单元格数据为：", cell_value)
#     else:
#         print("读取单元格数据失败。")
#
# if __name__ == '__main__':
#     # 用法示例：
#     config_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.ini')
#
#     read_excel_cell_from_config(config_file_path, "Sheet1", 2, 2)