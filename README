* Robomaster S1 SDK Support.

*** WARNING ***

AS IT IS TRUE FOR VIRTUALLY ALL HACKS, THIS HAS THE POTENTIAL TO BREAK YOUR S1
(IT DID NOT BREAK ANY OF MINE BUT I KNEW WHAT I WAS DOING). USE AT YOUR OWN
RISK. THERE IS NO IMPLICIT OR EXPLICIT GUARANTEE THAT IT WILL WORK FOR YOU.

***************

This is a collection of files and scripts required to get the Robomaster S1 to
have access to most functionality provided by the SDK that comes with the
Robomaster EP. DJI has so far refused to provide the SDK to S1 owners in an
official manner so a non-official one will have to do.

This is the full and mostly unmodified SDK as present in th EP (all the changes
are related to getting it to work with the S1). It should support everything the
EP one supports (I do not have an EP, so I can not be sure) except, of course,
for controlling hardware that is only present in the EP.

In any case, anything that might not be working can be made to work. Contrary to
what DJI want you to believe, the EP is basically just an S1 with extra hardware
(there are some other minor differences, but they really do not matter for SDK
support).

* How to install.

Note this has been designed to work out of the box in Linux. For other platforms
you will have to manually replicate the steps in the provided "upload.sh"
script.

1 - Read the "How to Root - Robomaster S1.pdf". It is mostly up-to-date except
    that the root script used to root the S1 does not work anymore. Instead use
    the contents of the "root.py_s1" file as the root script.
2 - After you got it to work, have adb installed (as per instructions) and
    connect to the S1 using "adb shell", open a Terminal window, switch to the
    directory where this README and the other files that came with it were
    extracted and simply run the upload.sh script.
3 - Restart the S1 (turn it off and on again). When it is booting, you should
    hear 2 chimes instead of the usual single chime. This will tell you that it 
    worked.

* New Features

- v0.0.3
Reenabled adb by default. This convenient in case of issues but it disables
rndis (etehrnet over USB) support. If you want to control the S1 with sometyhing
connected through USB you will need to comment the adb line in patch.sh (one can
still start adb with the root script.

- v0.0.2
Now scanning QR codes should work again (and we did not lose support for the
vision module).

- v0.0.1
Vision module should now be working correctly with the binary protocol (I
actually tested this now for a change).

- v0.0.0
This now should also support the new DJI binary protocol for the Robomaster EP.
This feature was only lightly tested (as due to DJI's handling of all this, I
lost interest in the S1 and moved to other more interesting things) but it
appears to work even if it is a bit flaky sometimes (specally on initial
connection).

* What is Actually Confirmed Working.

I did not do extensive testing on this, but there are some things I know are
definitelly working:

- Robomaster app still works and reports the robot as an S1.
- SDK connections can be made (both text and binary protocols).
- Getting the robot version works. :)
- Vision module is working in both protocols (I can get a video stream).

I will try to fix whatever might not be working as long I know it is not
working (I have not been using my S1 extensively).

That is it, you can try SDK support using some 3rd party libraries like:

https://github.com/brunoga/robomaster (Go) 
https://github.com/nanmu42/robomasterpy (Python)

Official SDK Sample Code Repository:

https://github.com/dji-sdk/RoboMaster-SDK

Official SDK Documentation:

https://robomaster-dev.readthedocs.io/zh_CN/latest/ (In Chinese)

