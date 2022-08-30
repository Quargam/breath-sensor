# python -m pip install pyserial
import serial
import datetime
import csv
import matplotlib.pyplot as plt


def main():
    x_list = []
    y_list = []
    try:
        ArduinoSerial = serial.Serial('com4', 115200)
        now_start = datetime.datetime.now()
        times_start = now_start.microsecond / 1000. + now_start.second * 1000. + now_start.minute * 60 * 1000. + now_start.hour * 60 * 60 * 1000.
        # time.sleep(1)
        with open("new_file3.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=";")
            while 1:
                now = datetime.datetime.now()
                times = now.microsecond / 1000. + now.second * 1000. + now.minute * 60 * 1000. + now.hour * 60 * 60 * 1000.
                text = ArduinoSerial.readline()
                # writer.writerow([int(float(text.decode('utf8')[2:])), int(times-times_start)])
                writer.writerow([int(times-times_start), int(float(text.decode('utf8')[7:]))])
                # print(f"{times};{text.decode('utf8')}", end='')
                print(f"{int(times-times_start)};{int(float(text.decode('utf8')[7:]))}", end='\n')
                x_list.append(int(float(text.decode('utf8')[7:])))
                y_list.append(int(times-times_start))
    except KeyboardInterrupt:
        print('программа закрыта')
        plt.plot(y_list, x_list, label='test')
        plt.legend()
        plt.show()

def exemple():
    ArduinoSerial = serial.Serial('COM5', 115200)
    while True:
        text = ArduinoSerial.readline()
        print(text)

if __name__ == '__main__':
    # exemple()
    main()