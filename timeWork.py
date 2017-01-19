import time
import calcToday
SECONDS_PER_DAY = 24 * 60 * 60
 
def getSleepTime():
    from datetime import datetime, timedelta
    curTime = datetime.now()
    desTime = curTime.replace(hour=4, minute=0, second=0, microsecond=0)
    delta = curTime - desTime
    skipSeconds = SECONDS_PER_DAY - delta.total_seconds()
    print "Must sleep %d seconds" % skipSeconds
    return skipSeconds

while (calcToday.checkToday() < 0) :
        print "err, do again"
        
while 1:
    sleepTime = getSleepTime()
    time.sleep(sleepTime)
    while (calcToday.checkToday() < 0) :
        print "err, do again"

# time.sleep(skipSeconds)

# while (calcToday.checkToday() < 0) :
#     print "err, do again"
