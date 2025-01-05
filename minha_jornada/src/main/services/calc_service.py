def sum_hour(init_time=str, final_time=str):
    init_hour = int(init_time.rsplit(':')[0])
    init_minute = int(init_time.rsplit(':')[1])
    final_hour = int(final_time.rsplit(':')[0])
    final_minute = int(final_time.rsplit(':')[1])
    cached_hour = get_hour()
    total_hour = cached_hour.rsplit(':')[0]
    total_minute = cached_hour.rsplit(':')[1]
    hour_result = int(total_hour)
    minute_result = int(total_minute)

    if init_hour > final_hour:
        hour_result += ((24 - init_hour) + final_hour)
    else:
        hour_result += final_hour - init_hour

    if init_minute > final_minute:
        minute_result += ((60 - init_minute) + final_minute)
        hour_result -= 1
    else:
        minute_result += final_minute - init_minute

    if minute_result > 59:
        hour_result += 1
        minute_result -= 60

    total_hour = zero_control(hour_result)
    total_minute = zero_control(minute_result)

    update_worked_time(f'{total_hour}:{total_minute}')
    return f'{total_hour}:{total_minute}'


def get_hour():
    with open('cache/worked_time.txt', 'r') as f:
        hour = f.read()
        return hour


def update_worked_time(new_hour):
    with open('cache/worked_time.txt', 'w') as f:
        f.write(new_hour)


def clean_cache():
    with open('cache/worked_time.txt', 'w') as f:
        f.write('00:00')


def zero_control(value):
    if value < 10:
        return f'0{value}'
    else:
        return f'{value}'


def valid_hour(time):
    try:
        for sub in time.split(':'):
            test = int(sub)
            if len(sub) != 2:
                return False
        return True
    except:
        return False
