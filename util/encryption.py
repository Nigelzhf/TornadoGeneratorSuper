from random import Random
def random_str(randomlength=8):
    """
    随机字符串生成函数

    :auth: Exborn
    :param randomlength:
    :return: 随机的字符串
    """
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str