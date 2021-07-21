#!/system/bin/sh

# Run adbd for convenience. Not required to get SDK support.
/system/bin/adb_en.sh &

# Stop affected services.
stop dji_sys
stop dji_hdvt_uav
stop dji_vision

# Overwrite S1's dji.json with EP's one. Use a bind mount as the file is in the
# system partition.
mount -o bind /data/dji.json /system/etc/dji.json

# This allows accessing the robot with DJI's binary protocol on port 20020.
mount -o bind /data/dji_hdvt_uav /system/bin/dji_hdvt_uav

# Restart services.
start dji_sys
start dji_hdvt_uav
start dji_vision

