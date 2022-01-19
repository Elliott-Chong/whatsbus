import datetime
import requests
import pywhatkit as pwk
from dotenv import load_dotenv, dotenv_values
base_url = 'http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2'
BusStopCode = '42169'
ServiceNo = '61'
load_dotenv()
config = dotenv_values(".env")


def main() -> None:
    response = requests.get(base_url, headers={'AccountKey': config["ACCOUNT_KEY"]}, params={
                            'BusStopCode': BusStopCode, 'ServiceNo': ServiceNo})
    timing1 = response.json()['Services'][0]
    timing2 = timing1['NextBus']['EstimatedArrival']
    timing3 = timing2.split('T')
    bus_arrival_time = timing3[1].split('+')[0]
    year = int(timing3[0].split('-')[0])
    month = int(timing3[0].split('-')[1])
    day = int(timing3[0].split('-')[2])

    hour = int(bus_arrival_time.split(':')[0])
    minute = int(bus_arrival_time.split(':')[1])
    second = int(bus_arrival_time.split(':')[2])
    time1 = datetime.datetime(
        year=year, month=month, day=day, hour=hour, minute=minute, second=second)
    if time1 > datetime.datetime.now():
        inter_time_delta = str(time1-datetime.datetime.now())
        timedelta_minute = inter_time_delta.split('.')[0].split(':')[1]
        timedelta_second = inter_time_delta.split('.')[0].split(':')[2]
        pwk.sendwhatmsg_instantly(
            config['PHONE_NUMBER'], f'Bus *{ServiceNo}* will arrive in *{timedelta_minute}* minutes and *{timedelta_second}* seconds at {bus_arrival_time}', wait_time=5)
    else:
        pwk.sendwhatmsg_instantly(
            config['PHONE_NUMBER'], f'Bus *{ServiceNo}* should be arriving soon', wait_time=5)


if __name__ == '__main__':
    main()
