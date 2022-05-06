# Android alarm manager and service with Kivy

Simple demonstration of how to build an app using Andoid's alarm manager and service implemented in Kivy

## How to?

Inside your project locate PythonActivity.java it should be inside

```.buildozer/android/platform/python-for-android/pythonforandroid/bootstraps/sdl2/build/src/main/java/org/kivy/android/PythonActivity.java```

and replace it with one from java_scr folder, then add KivyAlarmReceiver.java to the same folder where PythonActivity.java is, then replace AndroidManifest.tmpl.xml 

it should be inside ```.buildozer/android/platform/python-for-android/pythonforandroid/bootstraps/sdl2/build/templates/AndroidManifest.tmpl.xml``` with the one from java_scr folder

then check buildozer.spec file or simply copy it.

If you've alredy built some app before you should ```buildozer android clean``` before building your app again with this changes.

Already built app is in the bin folder.
