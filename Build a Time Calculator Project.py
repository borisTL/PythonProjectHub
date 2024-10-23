def add_time(start, duration, day=None):
    
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
   
    time, period = start.split(" ")
    f_time, f_minute = map(int, time.split(":"))
    e_time, e_minute = map(int, duration.split(":"))

  
    if period == "PM" and f_time != 12:
        f_time += 12
    if period == "AM" and f_time == 12:
        f_time = 0

   
    total_hours = f_time + e_time
    total_minutes = f_minute + e_minute


    if total_minutes >= 60:
        total_minutes -= 60
        total_hours += 1

  
    count_days = total_hours // 24
    final_hour = total_hours % 24


    if final_hour >= 12:
        period = "PM"
        if final_hour > 12:
            final_hour -= 12
    else:
        period = "AM"
        if final_hour == 0:
            final_hour = 12


    format_minute = f"{total_minutes:02}"

  
    if day is not None:
        index_of_day = days_of_week.index(day.capitalize())
        new_day_index = (index_of_day + count_days) % 7
        new_day = days_of_week[new_day_index]
    
  
    if day:
        if count_days == 0:
            return f"{final_hour}:{format_minute} {period}, {new_day}"
        elif count_days == 1:
            return f"{final_hour}:{format_minute} {period}, {new_day} (next day)"
        else:
            return f"{final_hour}:{format_minute} {period}, {new_day} ({count_days} days later)"
    else:
        if count_days == 0:
            return f"{final_hour}:{format_minute} {period}"
        elif count_days == 1:
            return f"{final_hour}:{format_minute} {period} (next day)"
        else:
            return f"{final_hour}:{format_minute} {period} ({count_days} days later)"


print(add_time("3:00 PM", "3:10", "Tuesday"))
