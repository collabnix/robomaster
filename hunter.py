pid_x = PIDCtrl()
pid_y = PIDCtrl()
pid_Pitch = PIDCtrl()
pid_Yaw = PIDCtrl()
variable_X = 0
variable_Y = 0
variable_Post = 0
list_MarkerList = RmList()
def start():
    global variable_X
    global variable_Y
    global variable_Post
    global list_MarkerList
    global pid_x
    global pid_y
    global pid_Pitch
    global pid_Yaw
    robot_ctrl.set_mode(rm_define.robot_mode_free)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    pid_Yaw.set_ctrl_params(115,0,5)
    pid_Pitch.set_ctrl_params(85,0,3)
    while True:
        list_MarkerList=RmList(vision_ctrl.get_marker_detection_info())
        if list_MarkerList[1] == 1:
            variable_X = list_MarkerList[3]
            variable_Y = list_MarkerList[4]
            pid_Yaw.set_error(variable_X - 0.5)
            pid_Pitch.set_error(0.5 - variable_Y)
            gimbal_ctrl.rotate_with_speed(pid_Yaw.get_output(),pid_Pitch.get_output())
            time.sleep(0.05)
            variable_Post = 0.01
            if abs(variable_X - 0.5) <= variable_Post and abs(0.5 - variable_Y) <= variable_Post:
                gun_ctrl.set_fire_count(1)
                gun_ctrl.fire_once()
                time.sleep(11)
        else:
            gimbal_ctrl.rotate_with_speed(0,0)
