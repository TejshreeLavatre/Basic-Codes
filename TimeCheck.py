import time

print("The epoch on this system starts at " + time.strftime("%c", time.gmtime(0)))
print("The current timezone is {} with an offset of {}".format(time.tzname[0], time.timezone))
if time.tzname[time.localtime().tm_isdst] != 0:
    print("DST is in effect here")
    print("The DTS tz is " + time.tzname[1])
print("Local time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# import datetime
# print(datetime.datetime.today())
# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())

# print("The local time is \t\t\t\t{}".format(time.get_clock_info("time")))
# print("The perfect counter time is \t{}".format(time.get_clock_info("perf_counter")))
# print("The monotonic time is \t\t\t{}".format(time.get_clock_info("monotonic")))
# print("The process time is \t\t\t{}".format(time.get_clock_info("process_time")))
# print(time.gmtime())
# print(time.localtime())
# print(time.gmtime(0))
# print(time.strftime("%c", time.gmtime(0)))
# print("The epoch on this system starts at {}".format(time.strftime('%c', time.gmtime(0))))
# print(time.tzname)
# print(time.timezone)
# print(time.daylight)
# print(time.tzname[time.localtime().tm_isdst])
