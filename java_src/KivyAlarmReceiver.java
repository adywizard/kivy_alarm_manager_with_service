package org.kivy.android;

import android.content.BroadcastReceiver;
import android.content.Intent;
import android.content.Context;

public class KivyAlarmReceiver extends BroadcastReceiver{

    @Override
    public void onReceive(Context context, Intent intent) {
        context.sendBroadcast(new Intent("KIVY_ALARM_SERVICE"));
    }
}