import time
#---------------------------------------
# epoch = a data and time from which a computer measures system time
##        aka when your computer thinks time began
# Time object is tm_year=2022, tm_mon=4, tm_mday=13, tm_hour=9, tm_min=51, tm_sec=15, tm_wday=2, tm_yday=103, tm_isdst=0
# #time is a class

print(time.ctime(1000))        # convert a time expressed in seconds since epoch to a readable string
print(time.time())             # return current seconds since epoch

# get the current date and tiem
print(time.ctime(time.time())) 

time_object = time.localtime()
time_object_UTC = time.gmtime() #universal time
print(time_object)

# https://strftime.org/
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)


# will parse a string representation of a time or date and return to a time object
time_string = "20 April, 2020"
time_object_2 = time.strptime(time_string, "%d %B, %Y")
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple) # a string representations
print(time_string)

#mktime will take a tuple repressentation of a time or a time object converting to seconds since epoch
time_string_2 = time.mktime(time_tuple)
print(time_string_2)



