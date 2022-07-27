# python -m pip install pyserial
import serial
import datetime
import csv
import time


def main():
    ArduinoSerial = serial.Serial('com4', 9600)
    now_start = datetime.datetime.now()
    times_start = now_start.microsecond / 1000. + now_start.second * 1000. + now_start.minute * 60 * 1000. + now_start.hour * 60 * 60 * 1000.
    time.sleep(1)
    with open("new_file2.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        while 1:
            now = datetime.datetime.now()
            times = now.microsecond / 1000. + now.second * 1000. + now.minute * 60 * 1000. + now.hour * 60 * 60 * 1000.
            text = ArduinoSerial.readline()
            # writer.writerow([int(float(text.decode('utf8')[2:])), int(times-times_start)])
            writer.writerow([int(times-times_start), int(float(text.decode('utf8')[2:]))])
            # print(f"{times};{text.decode('utf8')}", end='')
            print(f"{int(times-times_start)};{int(float(text.decode('utf8')[2:]))}", end='\n')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('программа закрыта')
