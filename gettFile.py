# import csv

# class gettFile:
#     def csv_reader(file_obj):
#         """
#         Read a csv file

#         """
#         # reader = csv.reader(file_obj)
#         # for row in reader:
#         #     print(" ".join(row))

#         reader = csv.DictReader(file_obj, delimiter=',')
#         # return reader;
#         for line in reader:
#             print("device_name: " + line["device_name"]),
#             print("mac_addr: "+line["mac_addr"]),
#             print("eddystone_instance_id: " + line["eddystone_instance_id"]),
#             print("rssi: "+line["rssi"]),
#             print("timestamp: "+line["timestamp"] +"\n")

#     # def printfunc(reader):
#     #     for line in reader:
#     #         print("device_name: " + line["device_name"]),
#     #         print("mac_addr: "+line["mac_addr"]),
#     #         print("eddystone_instance_id: " + line["eddystone_instance_id"]),
#     #         print("rssi: "+line["rssi"]),
#     #         print("timestamp: "+line["timestamp"] +"\n")

#     if __name__ == "__main__":
#         csv_path = "D:\\Olimp_24_05_2021\\Olympiad_25_04_2021\\data-1-1.csv"
#         with open(csv_path, "r") as f_obj:
#             csv_reader(f_obj)

# printfunc(csv_reader())

import csv

def getdate():
    arr = []
    with open("D:\\Olimp_24_05_2021\\Olympiad_25_04_2021\\data-1-1.csv", encoding='utf-8') as r_file:
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
        timestamp.sort()
        # arr.append(device_name)
        # arr.append(mac_addr)
        # arr.append(eddystone_instance_id)
        # arr.append(rssi)
        arr.append(timestamp)
    return arr

print(getdate())