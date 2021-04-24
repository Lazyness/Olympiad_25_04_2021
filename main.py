from inputdate import getdate
from our_math import get_predict
from constants import videoWriter
#main
def main():
    date = getdate()
    time1 = date[4][0]
    time2 = 0
    for i in range(int(len(date[4])/10)):
        time2 = date[4][i*10]
        get_predict(time1,time2)
        time1 = time2
    videoWriter.release()

main()