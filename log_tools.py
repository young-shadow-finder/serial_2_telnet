# 查找两份日志中某个关键字，并导出
def log_find(log_file_in_path: str, log_file_out_path: str, ket_words: str):
    with open(log_file_in_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(log_file_out_path, 'w', encoding='utf-8') as output_file:
        for line in lines:
            if ket_words in line:
                output_file.write(line)


# 两份日志中，按照长度去除行头部的时间戳
def log_del_line_number_head(log_file_in_path: str, log_file_out_path: str, number_words: int):
    with open(log_file_in_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(log_file_out_path, 'w', encoding='utf-8') as output_file:
        for line in lines:
            output_file.write(line[number_words: ])


if __name__ == "__main__":
    # 日志文件路径
    log_file1_path = 'D:\\Users\\Administrator\\Desktop\\src1.txt'
    log_file2_path = 'D:\\Users\\Administrator\\Desktop\\src2.txt'
    # 输出文件路径
    output_file1_path = 'D:\\logs\\dst1.txt'
    output_file2_path = 'D:\\logs\\dst2.txt'
    # 需要匹配的字符串
    search_string = '--->'

    log_find(log_file1_path, output_file1_path, search_string)
    log_find(log_file2_path, output_file2_path, search_string)
#    log_del_line_number_head(log_file1_path, output_file1_path, 29)
#    log_del_line_number_head(log_file2_path, output_file2_path, 29)
