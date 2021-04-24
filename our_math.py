from inputdate import getdate
from constants import cordB1, cordB2, cordB3, cordB4, cordB5, cordB6,datelast
from results import video_write, outputf

def get_predict(time1,time2):
    date = getdate()
    time1 = time_Str_To_Int(time1)
    time2 = time_Str_To_Int(time2)
    print(time1)
    device_name = date[0]
    mac_addr = date[1]
    eddystone_instance_id = date[2]
    rssi = date[3]
    timestamp = date[4]
    indArr = []
    for timeId in range(len(timestamp)):
        
        time = timestamp[timeId]
        
        time = time_Str_To_Int(time)
        if time1 <= time and time2 >= time:
            indArr.append(timeId)
    for ind in indArr:
        datelast.setb(eddystone_instance_id[ind],rssi[ind])
        if -1 * rssi[ind] <= 45:
            print(-1 * rssi[ind])
            i = eddystone_instance_id[ind]
            i = int(i)
            if i == 1:
                xy = cordB1
                outputf("C3 B1\n")
            if i == 2:
                xy = cordB2
                outputf("C3 B2\n")
            if i == 3:
                xy = cordB3
                outputf("C1 B3\n")
            if i == 4:
                xy = cordB4
                outputf("C1 B4\n")
            if i == 5:
                xy = cordB5
                outputf("C2 B5\n")
            if i == 6:
                xy = cordB6
                outputf("C2 B6\n")
            video_write(xy[0],xy[1])
            
            return
        if  -1 * rssi[ind] > 45 and -1 * rssi[ind] < 55:
            
            i = eddystone_instance_id[ind]
            i = int(i)
            
            if i == 1:
                xy = cordB1.copy()
                xy[0] = xy[0] - 30
                outputf("C3 \n")
            if i == 2:
                xy = cordB2.copy()
                xy[0] = xy[0] - 30
                outputf("C3 \n")
            if i == 3:
                xy = cordB3.copy()
                xy[0] = xy[0] + 30
                outputf("C1 \n")
            if i == 4:
                xy = cordB4.copy()
                xy[0] = xy[0] + 30
                outputf("C1 \n")
            if i == 5:
                xy = cordB5.copy()
                xy[0] = xy[0] - 30
                outputf("C2 \n")
            if i == 6:
                xy = cordB6.copy()
                outputf("C2 \n")
                xy[0] = xy[0] + 30
            video_write(xy[0],xy[1])
            return
        if -1 * rssi[ind] >= 55 :
            xy = datelast.get2max()
            video_write(xy[0],xy[1])
    return 

    # old algoritm

    # arr = [-150,-150,-150,-150,-150,-150]
    
    # for ind in indArr:
        
    #     if rssi[ind] > arr[int(eddystone_instance_id[ind]) -1]:
    #     #     arr[int(eddystone_instance_id[ind]) -1] = rssi[ind]
    #         arr[int(eddystone_instance_id[ind]) -1] = (arr[int(eddystone_instance_id[ind]) -1] + rssi[ind])/2
    # print(arr)
    
    # for j in range(3):
    #     m = min(arr)
    #     for i in range(6):
    #         if arr[i] == m:
    #             arr[i] = 100
    #             break

    # xyd = [0,0,0,0,0,0,0,0,0]
    # xy = 0
    # d = 6
    # for i in range(6):
    #     if arr[i] != 100:
    #         if i == 0:
    #             xyd[xy] = cordB1[0] 
    #             xyd[xy+1] = cordB1[1]
    #             xyd[d] = arr[i]
    #         if i == 1:
    #             xyd[xy] = cordB2[0] 
    #             xyd[xy+1] = cordB2[1]
    #             xyd[d] = arr[i]
    #         if i == 2:
    #             xyd[xy] = cordB3[0] 
    #             xyd[xy+1] = cordB3[1]
    #             xyd[d] = arr[i]
    #         if i == 3:
    #             xyd[xy] = cordB4[0] 
    #             xyd[xy+1] = cordB4[1]
    #             xyd[d] = arr[i]
    #         if i == 4:
    #             xyd[xy] = cordB5[0] 
    #             xyd[xy+1] = cordB5[1]
    #             xyd[d] = arr[i]
    #         if i == 5:
    #             xyd[xy] = cordB6[0] 
    #             xyd[xy+1] = cordB6[1]
    #             xyd[d] = arr[i]
    #         xy = xy + 2
    #         d = d + 1
    # for i in range(3):
    #     xyd[i+6] = val_do_dis(xyd[i+6])
    # print(xyd)
    # print(arr)
    # xy = findxyd(xyd[0],xyd[2],xyd[4],xyd[1],xyd[3],xyd[5],xyd[6],xyd[7],xyd[8])
    # print(xy)
    # video_write(xy[0],xy[1])
    

# cotvert string to int
def time_Str_To_Int(time):
    if type(time) == int:
        return time
    newtime = time[8] + time[9] + time[11] + time[12] + time[14] + time[15] + time[17] + time[18] + time[20] + time[21] + time[22]
    return int(newtime) 


#find dot 
def findxyd(x1,x2,x3,y1,y2,y3,d1,d2,d3):
    x1 = float(x1)
    x2 = float(x2)
    x3 = float(x3)
    y1 = float(y1)
    y2 = float(y2)
    y3 = float(y3)
    d1 = float(d1)
    d2 = float(d2)
    d3 = float(d3)

    f1 = 2 * x2 - 2 * x1
    f4 = 2 * x3 - 2 * x1
    f3 = 2 * y1 - 2 * y2
    f6 = 2 * y1 - 2 * y3
    f2 = x2**2 + y2**2 + d1**2 - d2**2 - x1**2 - y1**2
    f5 = x3**2 + y3**2 + d1**2 - d3**2 - x1**2 - y1**2

    y = (f2 * f4 - f5 * f1 )/(f6*f1 - f3*f4)
    if f1 == 0:
        x = (f5 + y * f6)/f4
    else:
        x = (f2 + y * f3)/f1
    return ([x,y])

#convert rssi to distanse (doesn`t work)
def val_do_dis(val):
    val = - val
    if val <= 41:
        dis = 0.1
    elif val > 41 and val<= 50:
        dis = 0.0625 * val - 2.125
    elif val > 50 and val<= 56:
        dis = 1/12 * val - 196 
    elif val > 56 and val<= 60:
        dis = 0.125 * val - 5.5
    elif val > 60 and val <= 65:
        dis = 2.2
    elif val > 65 and val<= 70:
        dis = 2.6
    elif val > 70 and val<= 75:
        dis = 3
    elif val > 75 and val<= 80:
        dis = 4.1
    elif val > 80 and val<= 85:
        dis = 5.2
    else:
        dis = 6
    alpha = 0
    return dis * 42

