from skpy import Skype
from datetime import datetime
import schedule
import time

print(str(datetime.now().replace(microsecond=0)) + ": Initiating...")

# Configuration
credentialId = ""                       # Skype Email
credentialPwd = ""                      # Skype Password (For safety, use app password)
channel_id = ""                         # Skype Group ID Example: '19:f642fc6241b047ca870e6a0790b76126@thread.skype'
checkInTime = ""                        # Time that send check-in message (E.g. 00:00)
checkOutTime = ""                       # Time that send check-out message (E.g. 24:59)
msgCheckIn = "Check-in"
msgCheckOut = "Check-out"
currentDate = datetime.now().date()
endDate = datetime(0000, 00, 00).date() # Date to stop the thread. Format: (yyyy,mm,dd)


# Check-in and Check-out functions
def post_checkin(msg, channel_id):
    sk = Skype(credentialId,credentialPwd)
    channel = sk.chats.chat(channel_id)
    channel.sendMsg(msgCheckIn)
    print(str(datetime.now().replace(microsecond=0)) + ": Check-in sent successful!")


def post_checkout(msg, channel_id):
    sk = Skype(credentialId,credentialPwd)
    channel = sk.chats.chat(channel_id)
    channel.sendMsg(msgCheckOut)
    print(str(datetime.now().replace(microsecond=0)) + ": Check-out sent successful!")

# Processing
while True:
print(str(datetime.now().replace(microsecond=0)) + ": Waiting for scheduled time...")

if currentDate == endDate or currentDate > endDate:
    print(str(datetime.now().replace(microsecond=0)) + ": Thread expired, exiting...")
    thread.exit()
else:
    if(int(currentDate.today().weekday()) == 5 or int(currentDate.today().weekday()) == 6):
        print(str(datetime.now().replace(microsecond=0)) + ": Program skipped... Today is weekend.")
        print(str(datetime.now().replace(microsecond=0)) + ": Waiting for next call...")
    else:
        schedule.every().day.at(checkInTime).do(post_checkin, msgCheckIn, channel_id)
        schedule.every().day.at(checkOutTime).do(post_checkout, msgCheckOut, channel_id)

        schedule.run_pending()
        print(str(datetime.now().replace(microsecond=0)) + ": Waiting for next call...")
        time.sleep(60)
