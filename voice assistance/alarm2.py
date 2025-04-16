import winsound
import datetime
def alarm(timing):
    alttime = str(datetime.datetime.now().strptime(timing,"%I:%M %p"))
    print(alttime)
    alttime = alttime[11:-3]
    horeal = alttime[:2]
    horeal = int(horeal)
    mireal = alttime[3:5]
    mireal = int(mireal)
    print(f"Done, alarm is set for {timing}")

    while True:
        if horeal == datetime.datetime.now().hour:
            if mireal == datetime.datetime.now().minute:
                print("alarm is running")
                winsound.PlaySound('C:\\Users\\goyal\\OneDrive\\Documents\\Desktop\\music\\music\\New folder\\infect.wav',winsound.SND_LOOP)

            elif mireal<datetime.datetime.now().minute:
                break

if __name__ == '__main__':
    alarm('8:10 PM')