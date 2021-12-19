import os, getpass, time
user = getpass.getuser()
drive = os.getenv("SystemDrive")
def main():
    os.system(f"move {drive}\\Users\\{user}\\Downloads\\CreaterNotificationForWindows-sos-utils {drive}\\Users\\{user}\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\CreaterNotificationForWindows")
    from CreaterNotificationForWindows import MainCode_CreaterNotificationForWindows
    from CreaterNotificationForWindows import vbOKOnly
    Notification = MainCode_CreaterNotificationForWindows
    Notification().CreateNotification('Install Completed', 'Install', vbOKOnly, False)
if __name__ == '__main__':
    main()
