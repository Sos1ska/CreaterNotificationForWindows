![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)

# CreaterNotificationForWindows
This code is intended to create a vbs script in the form of a message for Windows.<br>
Also, you will soon be able to leave executable vbs scripts next to the executable file in the Buffer folder
# Tests
![Total-tests](https://img.shields.io/badge/Total%20Test-20-brightgreen)<br>
![Fail-tests](https://img.shields.io/badge/Fail%20Test-5-red)
# Version
_version_ = 0.1<br>
_typeversion_ = [BETA]<br>
# Install 
1. Follow the link <code>https://github.com/Sos1ska/CreaterNotificationForWindows/archive/refs/heads/sos-utils.zip</code><br>
2. Unzip zip file to download folder<br>
3. Run <code>setup.py</code><br>
4. End
# Donate
qiwi.com/n/SOSISKA<br>
Copy link and paste into any browser
# Use
1. <code>from CreaterNotificationForWindows import MainCode_CreaterNotificationForWindows as Notification</code><br>
2. <code>from CreaterNotificationForWindows import (vbAbortRetryIgnore, vbApplicationModal,
                                                    vbCritical, vbDefaultButton1, vbDefaultButton2,
                                                    vbDefaultButton3, vbDefaultButton4,
                                                    vbExclamation, vbInformation,
                                                    vbMsgBoxHelpButton, vbMsgBoxRight,
                                                    vbMsgBoxRtlReading, vbMsgBoxSetForeground,
                                                    vbOKCancel, vbOKOnly, vbQuestion,
                                                    vbRetryCancel, vbSystemModal, vbYesNo,
                                                    vbYesNoCancel)</code><br>
3. <code>Notification().CreateNotification('Text', 'Title', ParametersMSG, False)</code> True does not work<br>
# Start Test
1. <code>from CreaterNotificationForWindows import TestStart</code><br>
2. <code>TestStart()</code><br>
# Soon
The 'log' argument - This argument will output information about the work of the code<br>
The 'win10' argument - This argument can generate notifications for Windows 10 + icon<br>
