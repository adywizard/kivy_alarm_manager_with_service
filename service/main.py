from time import localtime, asctime, sleep, time
from jnius import cast, autoclass


Intent = autoclass('android.content.Intent')
KivyAlarmReceiver = autoclass('org.kivy.android.KivyAlarmReceiver')
mService = autoclass('org.kivy.android.PythonService').mService
Intent = autoclass('android.content.Intent')
AlarmManager = autoclass('android.app.AlarmManager')
PendingIntent = autoclass('android.app.PendingIntent')
Context = autoclass('android.content.Context')


class KivyService:
    def __init__(self):
        pass

    def reschedule_alarm(self, minutes):
        context = mService.getApplicationContext()
        alarmSetTime = int(round(time() * 1000)) + 1000 * 60 * minutes
        alarmIntent = Intent()
        alarmIntent.setClass(context, KivyAlarmReceiver)
        alarmIntent.setAction("org.kivy.android.ACTION_START_ALARM")
        pendingIntent = PendingIntent.getBroadcast(
            context, 18, alarmIntent, PendingIntent.FLAG_UPDATE_CURRENT)
        alarm = cast(
            AlarmManager, context.getSystemService(Context.ALARM_SERVICE))
        alarm.setExactAndAllowWhileIdle(
            AlarmManager.RTC_WAKEUP, alarmSetTime, pendingIntent)

    def start(self):
        i = 0
        while True:
            sleep(2)
            i += 1
            print(asctime(localtime()).encode('utf8'))
            if i >= 30:
                self.reschedule_alarm(1)
                break


if __name__ == '__main__':
    service = KivyService()
    service.start()
