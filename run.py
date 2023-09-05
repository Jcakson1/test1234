import pytest

import subprocess
import os



# 获取当前脚本文件的路径
script_path = os.path.dirname(os.path.abspath(__file__))

# 组装测试脚本文件的绝对路径
file_path = os.path.join(script_path, 'test_case/test_E_report.py')


# 组装 Allure 报告的目录绝对路径
allure_report_dir = os.path.join('temp')

# 运行 PyTest 测试并生成 Allure 报告
pytest.main(['-s', '-vv', file_path, '--alluredir', allure_report_dir])

# 使用 subprocess 运行 Allure 生成报告命令
allure_command = f'allure generate {allure_report_dir} --clean -o {os.path.join("report", "results")}'
subprocess.run(allure_command, shell=True)
