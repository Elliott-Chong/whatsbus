from multiprocessing.connection import wait
import datetime
import requests
import pywhatkit as pwk
base_url = 'http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2'
def main():
    response = requests.get(base_url, headers={'AccountKey':'eKgQmw7hT9a/Y9oG22WMMQ=='}, params={'BusStopCode':'42169', 'ServiceNo':'173'})
    right = response.json()['Services'][0]
    yes = right['NextBus']['EstimatedArrival']
    um = yes.split('T')
    print(um[1].split('+')[0])
    print()
    bus_arrival_time = um[1].split('+')[0]
    year = int(um[0].split('-')[0])
    month = int(um[0].split('-')[1])
    day = int(um[0].split('-')[2])
    hour = int(bus_arrival_time.split(':')[0])
    minute = int(bus_arrival_time.split(':')[1])
    second = int(bus_arrival_time.split(':')[2])
    time1 = datetime.datetime(year=year,month=month,day=day,hour=hour, minute=minute,second=second)
    inter_time_delta=str(time1-datetime.datetime.now())
    timedelta_minute = inter_time_delta.split('.')[0].split(':')[1]
    timedelta_second = inter_time_delta.split('.')[0].split(':')[2]
    # pwk.sendwhatmsg_instantly("+6594565177", f'Bus 173 will arrive in {timedelta_minute} and {timedelta_second} seconds at {bus_arrival_time}', wait_time=5, tab_close=True, close_time=2)
    pwk.sendwhatmsg_instantly("+6590452020", f'Bus 173 will arrive in {timedelta_minute} and {timedelta_second} seconds at {bus_arrival_time}', wait_time=5)

    # pwk.sendwhatmsg_to_group_instantly("Fe8IIF34v46DjyMlS1CmlJ", f'Bus 173 will arrive in {timedelta_minute} and {timedelta_second} seconds at {bus_arrival_time}', wait_time=8, tab_close=True, close_time=2)
       




if __name__ == '__main__':
    main()
