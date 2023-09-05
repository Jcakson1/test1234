import os
import configparser

def read_ini_file(file_path):
    try:
        config = configparser.ConfigParser()
        config.read(file_path)

        project_path = config.get('project', 'project_path')
        login_Excel_account = config.get('project', 'login_Excel_account')
        login_Excel_element = config.get('project', 'login_Excel_element')
        get_Eng_report = config.get('project', 'Eng_report')
        EngineeringRecordForm = config.get('project', 'EngineeringRecordForm')
        config_data = {}
        # 将数据打包成一个字典进行返回
        config_data = {
            'project_path': project_path,
            'login_Excel_account': login_Excel_account,
            'login_Excel_element': login_Excel_element,
            'get_Eng_report': get_Eng_report,
            'test_EngineeringRecordForm': EngineeringRecordForm
        }

        return config_data

    except configparser.Error as e:
        print("Error reading INI file:", e)
        return None


# # 用法示例：
# file_path = 'config.ini'  # 假设INI文件名为config.ini，并与Python脚本在同一目录下
#
# project_path, full_login_Excel_path, full_login_Excel_element = read_ini_file(file_path)
#
# if project_path and full_login_Excel_path and full_login_Excel_path:
#     print("完整的登录Excel元素路径：", full_login_Excel_element)
#     print("完整的登录Excel路径：", full_login_Excel_path)
# else:
#     print("读取INI文件失败。")
