import configparser
import pymysql
import threading
# 创建 ini文件

def create_ini_file():

    config = configparser.ConfigParser()

    # 添加[Mysql]配置段
    config['Mysql'] = {
        'host': '192.168.98.163',
        'port': '3307',
        'database': '工程报表-test环境',
        'username': 'root',
        'password': 'eVTajWX6LUPKos6K'
    }

    # 写入INI文件
    with open('config.ini', 'w') as config_file:
        config.write(config_file)

    print("INI文件创建成功")

# 插入
def insert_data_to_table():
    # 读取INI文件中的数据库配置
    config = configparser.ConfigParser()
    config.read('config.ini')

    db_config = config['Mysql1']

    # 连接数据库
    connection = pymysql.connect(
        host=db_config['host'],
        port=int(db_config['port']),
        user=db_config['username'],
        password=db_config['password'],
        database=db_config['database']
    )

    try:
        # 创建游标对象
        cursor = connection.cursor()

        # 循环插入数据到表
        for i in range(1, 500):  # ID递增从1到100000
            # 构建插入数据的SQL语句 工程月度积分--表扬信情况统计表
            # sql = """INSERT INTO report_project_dept_praise (id, org_id, org_name, project_id, project_name, company_name, sub_dept_name, accept_date, praise_item, praise_date, praise_type, praise_unit, praise_unit_type, praise_mode, score, remark, approve_status, year_and_month, create_level, info1, info2, approve_msg) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            # 构建插入数据的SQL语句 工程月度积分 --表扬信情况统计表 工程检查排名表
            # sql = """INSERT INTO `engineering_report`.`report_project_check_praise` (`id`, `org_id`, `org_name`, `project_id`, `project_name`, `score_reason`, `fill_date`, `check_type`, `score`, `file_info1`, `approve_status`, `year_and_month`, `create_level`, `file_info2`, `file_info3`, `check_ranked`, `approve_msg`)"""

            # 构建数据值
            # values = (
            # start_id + i, 69, '广西分公司', 318, '广西儿童医疗中心项目', '呃呃呃', '华南分局', '2023-07-11', '呃呃呃', '2023-07-03', None, None, '政府', '饿死',
            # 3, None, '1', '2023-07', 0, None, None, '123214')
            # values = (73 + i, 69, '广西分公司', 318, '广西儿童医疗中心项目', None, '2023-07-11', '1', 3, None, '1', '2023-07', 0, None, None, '第一名', '十多个')

            # sql = """INSERT INTO `engineering_report`.`report_project_check_praise` (`id`, `org_id`, `org_name`, `project_id`, `project_name`, `score_reason`, `fill_date`, `check_type`, `score`, `file_info1`, `approve_status`, `year_and_month`, `create_level`, `file_info2`, `file_info3`, `check_ranked`, `approve_msg`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            #
            # # 插入的值
            # values = (
            # 73+i, 69, '广西分公司', 318, '广西儿童医疗中心项目', None, '2023-07-11', '1', 3, None, '1', '2023-07', 0, None, None, '第一名',
            # '十多个')

            # 执行SQL语句插入数据

            # # 构建插入语句 欠钱线索收集
            # sql = """INSERT INTO `engineering_report`.`sm_back_pay` (`id`, `edit_date`, `org_id`, `org_name`, `project_id`, `project_name`, `name`, `id_card`, `phone`, `subcontractor`, `worker_type`, `headman_name`, `headman_phone`, `problem_content`, `unpaid_wages`, `feed_back_content`, `is_outside_complain`, `is_completed`, `resolve_detail`, `appendix`, `completed_date`, `lock_status`, `delete`, `edit_status`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            #
            # # 提供插入值
            # values = (
            # 1068 + i, '2023-07-05 11:56:37', None, None, None, None, '220722199312056811', '18812345678', '分包999', '班组999',
            # '陈杰', '18911112222', '问题999', '99999', None, None, None, 0, None, None, None, 0, None, 0)
            #
            # # 构建插入语句    劳务管理黑名单
            # sql = """INSERT INTO `engineering_report`.`labor_service_blacklist` (`id`, `org_id`, `org_name`, `project_id`, `project_name`, `sub_unit`, `sub_content`, `worker_name`, `worker_sex`, `worker_post`, `id_card`, `native_place`, `entry_date`, `entry_reason`, `lock_state`, `update_date`, `user_code`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            #
            # # 提供插入值
            # values = (
            # 620+i , 53, '深圳分公司', 332, '东莞深业松湖云诚花园工程', '深圳市西城建筑工程劳务有限公司', '主体劳务', '周祝庆'+ str(i), '男', '木工', '441722197310186674',
            # '广东省阳江市阳春县', '2023-01-10 00:00:00', '恶意讨薪，往局总部打电话投诉', '有效', '2023-03-08 17:37:48', '202A3462')

            # # 构建插入语句 花名册管理--花名册
            # sql = """INSERT INTO `engineering_report`.`sm_roster` (`id`, `org_id`, `org_name`, `project_id`, `project_name`, `subcontractor`, `name`, `teams`, `worker_type`, `id_card`, `nation`, `political_landscape`, `work_license`, `home_address`, `native_place`, `contact`, `entry_date`, `contract_code`, `salary_standards`, `bank_card`, `opening_bank`, `bank_card_category`, `work_location`, `leave_date`, `work_license_img`, `edit_status`, `is_frozen`, `create_user`, `create_date`, `file_name`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            #
            # # 提供插入值
            # values = (
            # 119+i, 69, '广西分公司', 191, '南宁东盟威宁文创中心项目', '234', '第三个', '说的', '木工', '110101199007280200', 'w人员', '人也', '而已',
            # 'w儿童', '问题', '11111111111', '2023-05-31 00:00:00', 'SFWERT', '洒脱', '问题', '问题', '一类卡', '问题',
            # '2023-05-30 00:00:00', '1 (3) (1).jpg', 1, 1, '202A0077', '2023-05-31 09:01:32', None)

            # # 构建插入语句 产值报表--产值计划
            # sql = """INSERT INTO `engineering_report`.`opv_plan` (`id`, `org_id`, `org_name`, `project_id`, `project_name`, `year`, `estimated_settlement_amount`, `left_amount`, `plan_construction_amount`, `plan_january_amount`, `plan_february_amount`, `plan_march_amount`, `plan_april_amount`, `plan_may_amount`, `plan_june_amount`, `plan_july_amount`, `plan_august_amount`, `plan_september_amount`, `plan_october_amount`, `plan_november_amount`, `plan_december_amount`, `approve_status`, `create_time`, `create_user`, `org_project_year`, `is_edit`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            #
            # # 提供插入值
            # values = (
            #     112 + i, 69, '广西分公司', 473, '南宁市党员干部廉政教育基地项目', '2026', 333.00, 222.00, 52.00, 2.00, 3.00, 3.00, 4.00,
            #     4.00,
            #     2.00, 3.00, 3.00, 4.00, 8.00, 8.00, 8.00, '4', '2023-03-21 12:08:08', '202A0189',
            #     '广西分公司南宁市党员干部廉政教育基地项目2026'+str(i), 'false'
            # )

            # # 构建插入语句  月度施工产值报表
            # sql = """INSERT INTO `engineering_report`.`opv_monthly_sign` (`id`, `company_name`, `company_id`, `sub_company_name`, `sub_company_id`, `year_and_month`, `user_num`, `new_user_num`, `remark`, `approve_status`, `create_time`, `create_user`, `sub_year_month`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            #
            # # 提供插入值
            # values = (61+i, '中国建筑第八工程局有限公司南方公司', None, '广西分公司', None, '2023-07', 34, 23, '32', '1', '2023-03-21 11:20:33',
            #           '202A0189', '广西分公司2023-07'+str(i))

            # # 构建插入语句  新能源统计报表
            # sql = """INSERT INTO `engineering_report`.`energy_statistics_report` (`id`, `org_id`, `org_name`, `project_id`, `project_name`, `year_and_month`, `prower_used`, `gasoline_used`, `diesel_oil_used`, `oil_gas_used`, `total_water_volume`, `total_water_money`, `surface_water_volume`, `surface_water_money`, `tap_water_volume`, `tap_water_money`, `purified_water_volume`, `purified_water_money`, `energy_consumption`, `month_output_value`, `kgce`, `environment_protect_money`, `approve_status`, `update_user_code`, `update_time`, `quarter`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            #
            # # 提供插入值
            # values = (
            # 53+i, 69, '广西分公司', 229, '百色市右江区综合产业创业园项目总承包（EPC）', '2021-07', 2222, 2333, 333, 33, 699, 699, 333, 333, 333,
            # 33, 33, 333, 333, 0, 0, 2222, '1', '202B0180', '2023-07-05', 3)

            # # 构建插入语句  新能源统计报表 公司汇总
            # sql = """INSERT INTO `engineering_report`.`energy_statistics_report_org` (`id`, `org_id`, `org_name`, `year_and_month`, `prower_used`, `gasoline_used`, `diesel_oil_used`, `oil_gas_used`, `total_water_volume`, `total_water_money`, `surface_water_volume`, `surface_water_money`, `tap_water_volume`, `tap_water_money`, `purified_water_volume`, `purified_water_money`, `energy_consumption`, `month_output_value`, `kgce`, `environment_protect_money`, `update_user_code`, `update_time`, `quarter`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            #
            # # 提供插入值
            # values = (
            # 48+i, 85, '广州分公司', '2023-09', 100, 100, 100, 300, 300, 600, 100, 200, 100, 200, 100, 200, 288.3483928, 0, 0,
            # 9999111, '202A0161', '2023-03-15', 3)

            # # 构建插入语句 项目策划台账--项目策划计划
            # sql = """INSERT INTO `engineering_report`.`ppa_project_plan` (`id`, `org_id`, `org_name`, `project_id`, `project_name`, `year_and_month`, `org_meeting_plan_time`, `project_level`, `contract_amount`, `meeting_content`, `join_leader`, `project_manager`, `complete_time`, `remark`, `status`, `update_user`, `update_date`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            #
            # # 提供插入值
            # values = (
            # 3+i, 85, '广州分公司', 378, '广州市从化方舱医院', None, None, None, '66', None, None, '的故事', None, None, 1, '202A0161',
            # '2023-05-11 17:19:46')

            # # 构建插入语句 中建八局南方公司项目分阶段策划台账
            # sql = """INSERT INTO `engineering_report`.`ppa_stage_planning_account` (`id`, `org_id`, `org_name`, `project_id`, `project_name`, `year_and_month`, `project_contract_mode`, `project_manager`, `phone`, `project_management_num`, `scene_management_num`, `contract_completion_time`, `plan_completion_time`, `stage_meeting_time`, `complete_meeting_time`, `main_participants`, `Resolutions`, `Resolutions_status`, `status`, `del_flag`, `update_user`, `update_date`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            #
            # # 提供插入值
            # values = (
            # 1+i, 69, '广西分公司', 473, '南宁市党员干部廉政教育基地项目'+str(i), None, '1', '2', '11111111111', '2', '而且他', '2023-05-10 00:00:00',
            # '2023-05-08 00:00:00', '2023-05-10 00:00:00', '2023-05-08 00:00:00', '放弃', '去微软', 'qw人', 1, 0, '202A0077',
            # '2023-05-10 10:18:33')

            # 构建插入语句 临建统计信息表

            #插入 建筑垃圾费用统计
            # sql = """INSERT INTO `engineering_report`.`cw_fee` (`id`, `company_name`, `org_id`, `org_name`, `project_id`, `project_name`, `year_and_month`, `current_month_quantity`, `project_total_quantity`, `current_month_recycling_quantity`, `project_total_recycling_quantity`, `current_month_delivery_quantity`, `project_total_delivery_quantity`, `resolve_unit_price`, `current_month_delivery_fee`, `project_total_fee`, `status`, `del_flag`, `update_user`, `update_date`)
            # VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            #
            # values = (
            #     37+i, '南方公司', 85, '广州分公司', 212 , '三角岛度假酒店及度假屋（一期）设计施工总承包项目', '2023年04月'+str(i), 10.11, 10.11, 5.00, 10.11, 0.00,
            #     0.00, 12.00, 14.00, 12.00, 5, 0, '202A0189', '2023-04-23 15:11:25'
            # )
            #
            # #  插入 建筑垃圾分类管理情况
            #
            # sql = """INSERT INTO `engineering_report`.`cw_classify` (`id`, `company_name`, `org_id`, `org_name`, `year`, `total_project_num`, `waste_classify_project_num`, `project_promition_list`, `status`, `del_flag`, `update_user`, `update_date`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            #
            # values = (
            #     55+i , '南方公司', 53, '深圳分公司', '2023'+str(i), 300, 50, '100', 1, 0, '202A1007', '2023-04-25 12:08:03'
            # )
            # # 插入maintenance_project_report表的语句 维保项目台账
            # sql = """INSERT INTO `engineering_report`.`maintenance_project_report` (`id`, `org_id`, `org_name`, `project_id`, `project_name`, `year_and_month`, `project_complete_date`, `qa_date`, `qa_total_money`, `qa_unrecover_money`, `qa_status`, `qa_manager`, `phone`, `qa_worker`, `qa_woker_num`, `current_year_qa_money`, `total_qa_money`, `corp_pay_money`, `labor_pay_money`, `problem`, `visit_record_file`, `repair_record_file`, `satisfaction_record_file`, `warranty_notice_record_file`, `remark`, `status`, `update_user`, `update_time`)
            #  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            #
            # values = (
            #     12+i, 85, '广州分公司', 279, '云浮市西江新城图书馆建设项目', '2023-07'+str(i), '2023-05-04', '2023-05-31', 10, 10, '2', '赵四',
            #     '13323238888', '赵四', '99', 9999, 40, 10, 30, '问题12345', '图片.png', '图片.png', '图片.png', '图片.png', None,
            #     '2', '202A0161', '2023-05-04 15:16:04'
            #
            # 执行插入语句 工期管理 已竣工
            # sql = """INSERT INTO `engineering_report`.`ongoing_project_list` (`id`, `crop_name`, `org_id`, `org_name`, `project_id`, `project_name`, `project_start_year`, `project_status`, `province`, `city`, `region`, `street`, `project_address`, `substation`, `jurisdictional_unit`, `undertaking_name`, `project_type`, `project_bussiness_format`, `bureau_level_major_customers`, `crop_level_major_customers`, `image_progress`, `design_unit_name`, `contract_mode`, `build_unit_name`, `build_unit_type`, `survey_unit_name`, `consulting_unit_name`, `construct_control_unit_name`, `contract_build_area`, `on_build_area`, `contract_project_mileage`, `contract_individual_project_number`, `on_build_individual_project_number`, `max_individual_project_meters`, `project_problem`, `main_construct_scope`, `orign_contract_money`, `own_constract_contract_amount`, `orign_contract_start_date`, `orign_contract_end_date`, `orign_contract_limit_time`, `start_order_start_date`, `postpone_end_date`, `postpone_limit_date`, `extend_contract_postpone_limit_date`, `real_start_date`, `real_end_date`, `current_peior_manage_num`, `certificate_of_filing_manager`, `filing_manager_is_project_peole`, `filing_manager_name`, `filing_manager_age`, `filing_manager_work_year`, `filing_manager_manage_year`, `filing_manager_school`, `filing_manager_phone`, `real_manager_name`, `real_manager_age`, `real_manager_work_year`, `real_manager_manager_year`, `real_manager_school`, `real_manager_certificate`, `project_safety_director_name`, `project_safety_director_phone`, `real_manager_phone`, `project_chief_engineer_work_year`, `project_product_manager_work_year`, `project_business_manager_work_year`, `0_3_year_people_num`, `0_3_year_people_rate`, `0_5_year_people_num`, `0_5_year_people_rate`, `5_10_year_people_num`, `5_10_year_people_rate`, `over_10_year_people_num`, `over_10_year_people_rate`, `has_construct_permit`, `no_construct_permit_reason`, `real_manager_rank`, `real_manager_has_national_level_awards`, `real_manager_has_national_excellent_project_manager`, `sumbit_time`, `status`, `create_user`, `create_time`, `update_user`, `update_time`)
            # VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            #
            # values = (
            #     316 + i, '南方公司', 69, '广西分公司', 500+i, '百色市右江区综合产业创业园项目总承包（EPC）', '2023'+str(i), '6', '7', '97', '853', '未确认',
            #     '广西(省)南宁(市)邕宁区(区)未确认', '1', '去微软', 'wq人', '1', '去微软', '1', '挖人', '2', '啊', '1', '去微软', '1', '却认为',
            #     'qwr ', '热舞', 22.22, 55.55, 77.77, 5, 7, '88.88', '房管局', '萨芬', 4, 3, '2023-05-18', '2023-05-23', 5,
            #     '2023-05-10', '2023-05-24', 14, 1, '2023-05-16', '2023-05-22', 3, '1', '1', 'ew发', 3, 4, 4, '3',
            #     '11111111111', '二万人', 3, 3, 3, '4', '1', '热帖', '44444444444', '44444444444', 4, 5, 3, 4, 1.3333, 3, 1,
            #     2, 0.6667, 3, 1, '1', 'w儿童', '1', '1', '1', '2023-05-10 10:11:44', '2', '202B0180',
            #     '2023-05-09 17:20:06', '202A3462', '2023-05-10 10:11:44'
            # )

            # 执行插入语句 工期管理 在建中
            # sql = """INSERT INTO `engineering_report`.`ongoing_project_list` (`id`, `crop_name`, `org_id`, `org_name`, `project_id`, `project_name`, `project_start_year`, `project_status`, `province`, `city`, `region`, `street`, `project_address`, `substation`, `jurisdictional_unit`, `undertaking_name`, `project_type`, `project_bussiness_format`, `bureau_level_major_customers`, `crop_level_major_customers`, `image_progress`, `design_unit_name`, `contract_mode`, `build_unit_name`, `build_unit_type`, `survey_unit_name`, `consulting_unit_name`, `construct_control_unit_name`, `contract_build_area`, `on_build_area`, `contract_project_mileage`, `contract_individual_project_number`, `on_build_individual_project_number`, `max_individual_project_meters`, `project_problem`, `main_construct_scope`, `orign_contract_money`, `own_constract_contract_amount`, `orign_contract_start_date`, `orign_contract_end_date`, `orign_contract_limit_time`, `start_order_start_date`, `postpone_end_date`, `postpone_limit_date`, `extend_contract_postpone_limit_date`, `real_start_date`, `real_end_date`, `current_peior_manage_num`, `certificate_of_filing_manager`, `filing_manager_is_project_peole`, `filing_manager_name`, `filing_manager_age`, `filing_manager_work_year`, `filing_manager_manage_year`, `filing_manager_school`, `filing_manager_phone`, `real_manager_name`, `real_manager_age`, `real_manager_work_year`, `real_manager_manager_year`, `real_manager_school`, `real_manager_certificate`, `project_safety_director_name`, `project_safety_director_phone`, `real_manager_phone`, `project_chief_engineer_work_year`, `project_product_manager_work_year`, `project_business_manager_work_year`, `0_3_year_people_num`, `0_3_year_people_rate`, `0_5_year_people_num`, `0_5_year_people_rate`, `5_10_year_people_num`, `5_10_year_people_rate`, `over_10_year_people_num`, `over_10_year_people_rate`, `has_construct_permit`, `no_construct_permit_reason`, `real_manager_rank`, `real_manager_has_national_level_awards`, `real_manager_has_national_excellent_project_manager`, `sumbit_time`, `status`, `create_user`, `create_time`, `update_user`, `update_time`)
            # VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            #
            # values = (
            #     1000 + i, '南方公司', 69, '广西分公司', 1100+i, '百色市右江区综合产业创业园项目总承包（EPC）', '2023'+str(i), '2', '7', '97', '853', '未确认',
            #     '广西(省)南宁(市)邕宁区(区)未确认', '1', '去微软', 'wq人', '1', '去微软', '1', '挖人', '2', '啊', '1', '去微软', '1', '却认为',
            #     'qwr ', '热舞', 22.22, 55.55, 77.77, 5, 7, '88.88', '房管局', '萨芬', 4, 3, '2023-05-18', '2023-05-23', 5,
            #     '2023-05-10', '2023-05-24', 14, 1, '2023-05-16', '2023-05-22', 3, '1', '1', 'ew发', 3, 4, 4, '3',
            #     '11111111111', '二万人', 3, 3, 3, '4', '1', '热帖', '44444444444', '44444444444', 4, 5, 3, 4, 1.3333, 3, 1,
            #     2, 0.6667, 3, 1, '1', 'w儿童', '1', '1', '1', '2023-05-10 10:11:44', '2', '202B0180',
            #     '2023-05-09 17:20:06', '202A3462', '2023-05-10 10:11:44'
            # )
            # # 定义SQL语句
            # sql = """
            # INSERT INTO `engineering_report`.`opv_target_construction` (
            #     `id`, `company_name`, `company_id`, `sub_company_name`, `sub_company_id`, `year`,
            #     `total_plan_construction_amount`, `plan_january_amount`, `plan_february_amount`,
            #     `plan_march_amount`, `plan_april_amount`, `plan_may_amount`, `plan_june_amount`,
            #     `plan_july_amount`, `plan_august_amount`, `plan_september_amount`,
            #     `plan_october_amount`, `plan_november_amount`, `plan_december_amount`, `remark`,
            #     `create_time`, `company_name_year`
            # ) VALUES (
            #     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            # )"""
            #
            # # 定义要插入的值
            # values = (
            #     65+i, '中国建筑第八工程局有限公司南方公司', 1, '广西分公司', 69, '2023', 43.00, 2.00, 3.00, 4.00,
            #     2.00, 3.00, 5.00, 4.00, 6.00, 3.00, 5.00, 2.00, 4.00, '3', None, '广西分公司2023'+str(i)
            # )

            cursor.execute(sql, values)

            print("数据插入成功:第 %d 条" % i)

        # 提交事务
        connection.commit()

        print("数据插入成功")

    except Exception as e:
        # 发生错误时回滚
        connection.rollback()
        print("插入数据时发生错误:", e)

    finally:
        # 关闭数据库连接
        connection.close()

# 删


# 修改


# 查询

def insert_data(connection, cursor, values):
    try:
        # 执行插入数据的SQL语句
        sql = """
            INSERT INTO personnel_information (
                id, insert_time, sysid, eno, name, sex, gzzd, gzzd_type, idcard, birthday, jzjz, mzmz, phone, indate, lrrq,
                cardid, gid, group_name, permission, jy_state, kq_state, JB, sfzzp, hfhf, sfzzm, sfzfm, htfj, htno,
                sfqdht, htstart, htend, contract_period, htfjlx, id_card_type, kq_date, yglx, jnsp, grlx, cyaqjy,
                zzmm, khyh, yhkh, jgjg, jtzh, fzgg, qfrq, dqrq, sfzyry, cardno, grdj, whcd, gidDz, oname, szdw, gxdate,
                yhlh, yhzh, state, zzdi, swbzz
            )
            VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """

        # 执行SQL语句插入数据
        cursor.execute(sql, values)

        # 提交事务
        connection.commit()

        print("数据插入成功:", values)

    except Exception as e:
        # 发生错误时回滚
        connection.rollback()
        print("插入数据时发生错误:", e)

def configure_database():
    # 读取INI文件中的数据库配置
    config = configparser.ConfigParser()
    config.read('config.ini')

    db_config = config['Mysql']

    # 连接数据库
    connection = pymysql.connect(
        host=db_config['host'],
        port=int(db_config['port']),
        user=db_config['username'],
        password=db_config['password'],
        database=db_config['database']
    )

    try:
        # 创建游标对象
        cursor = connection.cursor()

        # 创建线程列表
        threads = []
        start_id = 978
        # 循环执行插入操作
        for i in range(1, 3):
            # 构建数据值
            values = (
                start_id + i, '2023-07-12 15:00:00', 432381, '2300432381', '姓名' + str(i), '男', '钢筋班', 0,
                '532627199310023136', '1990-10-30', 'upload/photo/jzjz/532627199310023136.jpg',
                '汉族', '15187606650', '2023-07-11', '9999-12-31', '67216', 11599, '邓云龙', '0', 0, 0,
                '工人', '', '未婚', '', '', '', '', '', '1900-01-01T00:00:00', '9999-12-31T00:00:00',
                '固定期限合同', '', '居民身份证', '2023-04-18T13:45:19', '自有工人', '无(普通)', '建筑工人', '是', '群众',
                '邮储银行', '123456789', '广东', '深圳市龙岗区', '深圳市龙岗区公安局', '2012-10-30', '2032-10-30',
                '', '901', 0, '本科', '0', '国际交流中心（一期）', '福建巨申建筑劳务有限公司-邓云龙',
                '2023-04-17T11:56:07', '', '', '0', '', '0'
            )

            # 创建线程并启动
            thread = threading.Thread(target=insert_data, args=(connection, cursor, values))
            thread.start()

            # 将线程添加到线程列表
            threads.append(thread)

        # 等待所有线程完成
        for thread in threads:
            thread.join()

        print("所有数据插入操作已完成")

    except Exception as e:
        # 发生错误时回滚
        connection.rollback()
        print("插入数据时发生错误:", e)

    finally:
        # 关闭数据库连接
        connection.close()

if __name__ == '__main__':
    insert_data_to_table()
    # 调用函数配置数据库
    # configure_database()
