try:
    from CreaterNotificationForWindows import MainCode_CreaterNotificationForWindows
    from CreaterNotificationForWindows import vbOKOnly
except ImportError:
    try:
        from .CreaterNotificationForWindows import MainCode_CreaterNotificationForWindows
    except ImportError as IE:
        import datetime, time
        date_write = datetime.datetime.now()
        print(f'[ Sos1ska ] - [ ImportError: {IE} ] - [ {date_write} ]')
        time.sleep(120)
        quit()
def TestStart():
    MainCode_CreaterNotificationForWindows().CreateNotification('Test Completed', 'Test', vbOKOnly, True)
