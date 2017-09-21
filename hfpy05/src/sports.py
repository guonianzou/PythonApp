def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return data.strip().split(',')
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return None


sarah = get_coach_data('sarah2.txt')

# pop(0) 调用将删除并返回列表最前面的数据项.两个 pop(0) 调用会删除前两个数据值,并把它们赋给指定的变量
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)

print(sarah_name + "'s fastest times are: " +
      str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
