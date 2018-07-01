import datetime
stop_time = datetime.datetime.now() + datetime.timedelta(seconds=1)
import sys 


while True:
    if datetime.datetime.now() > stop_time: 
        print('one second has passed {}'.format(stop_time), file=sys.stderr)
        stop_time = datetime.datetime.now() + datetime.timedelta(seconds=1)