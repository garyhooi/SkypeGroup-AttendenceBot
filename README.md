# Auto send attendence to Skype Group
This is an console program which is written in Python 3. It can help you to send check-in and check-out message to specific Skype group.

## Configuration (send-groupmsg-skype.py)
You may only change the value in the configuration section.

##### # Configuration
```
credentialId = ""                       # Skype Email
credentialPwd = ""                      # Skype Password (For safety, use app password)
channel_id = ""                         # Skype Group ID Example: '19:f642fc6241b047ca870e6a0790b76126@thread.skype'
checkInTime = ""                        # Time that send check-in message (E.g. 00:00)
checkOutTime = ""                       # Time that send check-out message (E.g. 24:59)
msgCheckIn = "Check-in"
msgCheckOut = "Check-out"
currentDate = datetime.now().date()
endDate = datetime(0000, 00, 00).date() # Date to stop the thread. Format: (yyyy,mm,dd)
```

## Skype Group ID (get-skype-group-id.py)
To get your Skype group ID, use the below Python code.
You may also download from the repository.
```
from skpy import Skype

credentialId = ""                       # Skype Email
credentialPwd = ""                      # Skype Password (For safety, use app password)

skype_obj = Skype(credentialId, credentialPwd)
skype_obj.chats.recent()                # Return Skype group id
```
