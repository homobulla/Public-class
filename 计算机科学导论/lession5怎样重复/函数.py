
# 定义一个函数，即重复一段过程，要搞清楚输入和输出，即输入映射到输出中


def get_next_target(s):
    start_link = s.find('<a href=')
    start_quote = s.find('"', start_link)
    end_quote = s.find('"', start_quote + 1)
    url = s[start_quote:end_quote]
    return url, end_quote
