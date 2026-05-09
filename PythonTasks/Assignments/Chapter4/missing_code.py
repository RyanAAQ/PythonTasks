def seconds(hours, minutes, seconds):

    hour_in_seconds = hours * 3600
    minute_in_seconds = minutes * 60
    
    return hour_in_seconds + minute_in_seconds + seconds
    
print(seconds(13, 30, 45))
