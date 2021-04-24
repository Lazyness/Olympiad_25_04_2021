import csv

class gettFile:
    def csv_reader(file_obj):
        """
        Read a csv file

        """
        # reader = csv.reader(file_obj)
        # for row in reader:
        #     print(" ".join(row))

        reader = csv.DictReader(file_obj, delimiter=',')
        return reader;
        # for line in reader:
        #     print("device_name: " + line["device_name"]),
        #     print("mac_addr: "+line["mac_addr"]),
        #     print("eddystone_instance_id: " + line["eddystone_instance_id"]),
        #     print("rssi: "+line["rssi"]),
        #     print("timestamp: "+line["timestamp"] +"\n")
    
    if __name__ == "__main__":
        csv_path = "D:\\Olimp_24_05_2021\\Olympiad_25_04_2021\\data-1-1.csv"
        with open(csv_path, "r") as f_obj:
            csv_reader(f_obj)
            
def printfunc(reader):
    for line in reader:
        print("device_name: " + line["device_name"]),
        print("mac_addr: "+line["mac_addr"]),
        print("eddystone_instance_id: " + line["eddystone_instance_id"]),
        print("rssi: "+line["rssi"]),
        print("timestamp: "+line["timestamp"] +"\n")