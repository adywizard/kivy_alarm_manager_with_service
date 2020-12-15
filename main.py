import time
from jnius import autoclass, cast
from kivy.app import App
from kivy.lang import Builder
from kivy.utils import platform


if platform == 'android':
    Intent = autoclass('android.content.Intent')
    Context = autoclass('android.content.Context')
    KivyAlarmReceiver = autoclass('org.kivy.android.KivyAlarmReceiver')
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    mActivity = PythonActivity.mActivity
    Intent = autoclass('android.content.Intent')
    AlarmManager = autoclass('android.app.AlarmManager')
    PendingIntent = autoclass('android.app.PendingIntent')
    Context = autoclass('android.content.Context')


KV = """
FloatLayout:
    TextInput:
        id: t
        pos_hint: {'center': (.5, .65)}
        size_hint: .3, .05
        filter: int
    Label:
        pos_hint: {'center': (.5, .6)}
        text: 'after how many minutes should be fired'
    Button:
        pos_hint: {'center': (.5, .45)}
        size_hint: .3, .1
        text: 'start service'
        on_release: app.start_alarm(t.text)
    Label:
        id: lbl
        pos_hint: {'center': (.5, .35)}
        text: 'kivy alarm manger with service'
"""


class Application(App):

    def build(self):
        return Builder.load_string(KV)

    def start_alarm(self, min):
        if not min:
            min = 1
        context = mActivity.getApplicationContext()
        alarmSetTime = int(round(time.time() * 1000)) + 1000 * 60 * int(min)
        alarmIntent = Intent()
        alarmIntent.setClass(context, KivyAlarmReceiver)
        alarmIntent.setAction("org.kivy.android.ACTION_START_ALARM")
        pendingIntent = PendingIntent.getBroadcast(
            context, 18, alarmIntent, PendingIntent.FLAG_UPDATE_CURRENT)
        alarm = cast(
            AlarmManager, context.getSystemService(Context.ALARM_SERVICE))
        alarm.setExactAndAllowWhileIdle(
            AlarmManager.RTC_WAKEUP, alarmSetTime, pendingIntent)


if __name__ == "__main__":
    app = Application()
    app.run()
