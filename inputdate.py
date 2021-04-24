from constants import filename
import csv
def getdate():
    arr = []
    with open(filename, encoding='utf-8') as r_file:
        # Создаем объект DictReader, указываем символ-разделитель ","
        file_reader = csv.DictReader(r_file, delimiter = ",")
        # Счетчик для подсчета количества строк и вывода заголовков столбцов
        count = 0
        device_name = []
        mac_addr = []
        eddystone_instance_id = []
        rssi = []
        timestamp = []
        for row in file_reader:
            device_name.append(row["device_name"])
            mac_addr.append(row["mac_addr"])
            eddystone_instance_id.append(row["eddystone_instance_id"])
            rssi.append(float(row["rssi"]))
            timestamp.append(row["timestamp"])

        arr.append(device_name)
        arr.append(mac_addr)
        arr.append(eddystone_instance_id)
        arr.append(rssi)
        arr.append(timestamp)
    return arr

