#!/bin/bash

adb shell rm -rf /data/dji_scratch/sdk
adb push dji_scratch/sdk /data/dji_scratch/.

adb push dji_scratch/bin/dji_scratch.py /data/dji_scratch/bin/.

adb push dji.json /data/.

adb push dji_hdvt_uav /data/.

adb push patch.sh /data/.

