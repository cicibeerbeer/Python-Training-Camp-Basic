"""
练习: 字典操作

描述：
实现对学生成绩字典的添加、删除、修改和查询操作。

请补全下面的函数，对学生成绩字典进行各种操作。
"""

def student_dict_operations(students_dict, operation, *args):
    """
    对学生字典进行操作
    
    参数:
    - students_dict: 学生字典 {姓名: 成绩}
    - operation: 操作类型 ("add", "remove", "update", "get")
    - args: 操作所需的额外参数
    
    返回:
    - 根据操作返回不同结果
    """
    # 请在下方编写代码
    result = students_dict
    if operation == "add":
        if len(args)>=2:
            result[args[0]] = args[1]
        return result
    elif operation == "remove":
        if args and args[0]  in result:
            del result[args[0]]
        return result
    elif operation == "update":
        if len(args)>=2 and args[0] in result:
            result[args[0]] = args[1]
        return result
    elif operation == "get":
        # 获取学生成绩
        if args and args[0] in result:
            return result[args[0]]
    return None
    pass 
    