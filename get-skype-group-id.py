from skpy import Skype

credentialId = ""                       # Skype Email
credentialPwd = ""                      # Skype Password (For safety, use app password)

skype_obj = Skype(credentialId, credentialPwd)
skype_obj.chats.recent()                # Return Skype group id