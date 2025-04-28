"""
练习: 列表操作

描述：
实现对学生列表的添加、删除和修改操作。

请补全下面的函数，对学生列表进行各种操作。
"""

def student_list_operations(students, operation, *args):
    """
    对学生列表进行操作
    
    参数:
    - students: 学生列表
    - operation: 操作类型 ("add", "remove", "update")
    - args: 操作所需的额外参数
    
    返回:
    - 操作后的学生列表
    """
    # 请在下方编写代码
    result = students
    if operation == "add":
        if args and args[0] not in result:
            result.append(args[0])
    elif operation == "remove":
        if args and args[0]  in result:
            result.remove(args[0])
    elif operation == "update":
        if len(args)>=2 and args[0] in result:
            index = result.index(args[0])
            result[index] = args[1]
    return result
    pass 