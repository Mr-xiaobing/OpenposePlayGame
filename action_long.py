import math

import skill_long


# 动作
def operation(points):
    # 鼻子
    nose = points[0]
    # 胸骨
    core = points[1]
    # 右边肩膀
    shoulder_right = points[2]
    # 左边肩膀
    shoulder_left = points[5]
    # 右边肘
    elbow_right = points[3]
    # 左边肘
    elbow_left = points[6]
    # 右手掌
    palm_right = points[4]
    # 左手掌
    palm_left = points[7]
    # 裆部
    jj = points[8]
    # 右髋骨
    hip_right = points[9]
    # 左髋骨
    hip_left = points[12]
    # 右膝盖
    knee_right = points[10]
    # 左膝盖
    knee_left = points[13]
    # 右脚踝
    ankle_right = points[11]
    # 左脚踝
    ankle_left = points[14]
    # 曝气 双手交叉在胸前

    # 翻滚 弯背
    if roll_left(palm_right, palm_left, knee_right, knee_left):
        return
    # 曝气 双手交叉在胸前
    if unparalleled(palm_left, elbow_left, palm_right, elbow_right, shoulder_left, shoulder_right, jj, core):
        return

    # 旋风腿 踢腿加直拳 （左右方向）
    if whirlwind_leg_left(palm_left, elbow_left, shoulder_left, hip_left, knee_left,elbow_right,hip_right,knee_right, ankle_left,ankle_right):
        return

    # 右边旋风腿
    if whirlwind_leg_right(palm_right, elbow_right, shoulder_right, hip_right, knee_right, hip_left, knee_left, elbow_left, ankle_right,ankle_left):
        return

    # 冲击波 推波
    if qi_gong_right(core, elbow_left, elbow_right):
        return

    if qi_gong_left(core, elbow_left, elbow_right):
        return

    # 技能升龙拳 高举双手
    if real_sheng_long_boxing(nose, palm_left, palm_right):
        return

    # 升龙拳 高举左右手
    if sheng_long_boxing_left(nose, palm_left):
        return

    if sheng_long_boxing_right(nose, palm_right):
        return

    # 右边移动 格挡
    if move_right(palm_left, elbow_left, shoulder_left,core):
        return
    #
    # # 左边移动 格挡
    if move_left(palm_right, elbow_right, shoulder_right,core):
        return

    # 腿 踢腿
    if leg(knee_right, hip_left, hip_left, knee_left):
        return

    # 拳头 直拳
    if boxing(palm_left, elbow_left, shoulder_left, palm_right, elbow_right, shoulder_right):
        return

    return


# 气功波 右边
def qi_gong_right(core, elbow_left, elbow_right):
    if core[2] > 0.1 and elbow_left[2] > 0.1 and elbow_right[2] > 0.1:
        if elbow_left[0] < core[0] and elbow_right[0] < core[0]:
            # 调用按键使用技能
            skill_long.shock_wave_right()
            return True
    return False


# 气功波 左边
def qi_gong_left(core, elbow_left, elbow_right):
    if core[2] > 0.1 and elbow_left[2] > 0.1 and elbow_right[2] > 0.1:
        if elbow_left[0] > core[0] and elbow_right[0] > core[0]:
            skill_long.shock_wave_left()
            return True
    return False


# 升龙拳 左边
def sheng_long_boxing_left(nose, palm_left):
    if nose[2] > 0.1 and palm_left[2] > 0.1:
        if palm_left[1] < nose[1]:
            skill_long.sheng_long_boxing_left();
            return True
    return False


# 升龙拳 右边
def sheng_long_boxing_right(nose, palm_right):
    if nose[2] > 0.1 and palm_right[2] > 0.1:
        if palm_right[1] < nose[1]:
            skill_long.sheng_long_boxing_right()
            return True
    return False


# 大招旋风拳
def real_sheng_long_boxing(nose,palm_left,palm_right):
    if nose[2] > 0.1 and palm_right[2] > 0.1 and palm_left[2] > 0.1:
        if palm_right[1] < nose[1] and palm_left[1] < nose[1]:
            skill_long.i()
            return True
    return False


# 旋风腿 右边
def whirlwind_leg_right(palm_right, elbow_right, shoulder_right, hip_right, knee_right,hip_left,knee_left, elbow_left, ankle_right, ankle_left):
    if palm_right[2] > 0.1 and elbow_right[2] > 0.1 and shoulder_right[2] > 0.1 and hip_right[2] > 0.1 and knee_right[2] > 0.1 and hip_left[2] > 0.1 and knee_left[2] > 0.1 and elbow_left[2] > 0.1 and ankle_right[2] > 0.1 and ankle_left[2] > 0.1 and palm_right[1] < elbow_left[1] :
        temp_palm_elbow = [palm_right[0], palm_right[1], elbow_right[0], elbow_right[1]]
        temp_elbow_shoulder = [elbow_right[0], elbow_right[1], shoulder_right[0], shoulder_right[1]]
        result_angle = angle(temp_palm_elbow, temp_elbow_shoulder)
        if result_angle > 40:
            temp_hip_knee_right = [hip_right[0], hip_right[1], knee_right[0], knee_right[1]]
            temp_hip_knee_left = [hip_left[0], hip_left[1], knee_left[0], knee_left[1]]
            angle2 = angle(temp_hip_knee_right, temp_hip_knee_left)
            if angle2 < 40:
                skill_long.xuan_feng_leg_right()
                return True
    return False


# 旋风腿 左边
def whirlwind_leg_left(palm_left, elbow_left, shoulder_left,  hip_left, knee_left, elbow_right,hip_right,knee_right, ankle_left ,ankle_right):
    if palm_left[2] > 0.1 and elbow_left[2] > 0.1 and shoulder_left[2] > 0.1  and hip_left[2] > 0.1 and knee_left[2] > 0.1 and elbow_right[2] > 0.1 and hip_right[2] > 0.1 and ankle_left[2] > 0.1 and ankle_right[2] > 0.1 and knee_right[2] > 0.1 and palm_left[1] < elbow_right[1]:
        temp_palm_elbow = [palm_left[0], palm_left[1], elbow_left[0], elbow_left[1]]
        temp_elbow_shoulder = [elbow_left[0], elbow_left[1], shoulder_left[0], shoulder_left[1]]
        result_angle = angle(temp_palm_elbow, temp_elbow_shoulder)
        if result_angle > 40:
            temp_hip_knee_left = [hip_left[0], hip_left[1], knee_left[0], knee_left[1]]
            temp_hip_knee_right = [hip_right[0], hip_right[1], knee_right[0], knee_right[1]]
            angle2 = angle(temp_hip_knee_left, temp_hip_knee_right)
            if angle2 < 40:
                skill_long.xuan_feng_leg_left()
                return True
    return False


# 往左走
def move_left(palm_right, elbow_right, shoulder_right,core):
    if palm_right[2] > 0.1 and elbow_right[2] > 0.1 and shoulder_right[2] > 0.1:
        temp_palm_elbow = [palm_right[0], palm_right[1], elbow_right[0], elbow_right[1]]
        temp_shoulder_elbow = [elbow_right[0], elbow_right[1], shoulder_right[0], shoulder_right[1]]
        result = angle(temp_palm_elbow, temp_shoulder_elbow)
        if palm_right[1] < core[1]:
            skill_long.left()
            return True
    return False


# 往右走
def move_right(palm_left, elbow_left, shoulder_left,core):
    if palm_left[2] > 0.1 and elbow_left[2] > 0.1 and shoulder_left[2] > 0.1:

        temp_palm_elbow = [palm_left[0], palm_left[1], elbow_left[0], elbow_left[1]]
        temp_shoulder_elbow = [elbow_left[0], elbow_left[1], shoulder_left[0], shoulder_left[1]]
        result = angle(temp_palm_elbow, temp_shoulder_elbow)
        if  palm_left[1] < core[1]:
            skill_long.right()
            return True
    return False


# 拳
def boxing(palm_left, elbow_left, shoulder_left,palm_right, elbow_right, shoulder_right):
    if palm_left[2] > 0.1 and elbow_left[2] > 0.1 and shoulder_left[2] > 0.1 and palm_left[1] < elbow_right[1] and elbow_left[1] < elbow_right[1]:
        temp_palm_elbow = [palm_left[0], palm_left[1], elbow_left[0], elbow_left[1]]
        temp_elbow_shoulder = [elbow_left[0], elbow_left[1], shoulder_left[0], shoulder_left[1]]
        result_angle = angle(temp_palm_elbow, temp_elbow_shoulder)
        if result_angle < 70:
            skill_long.j()
            return True
    if palm_right[2] > 0.1 and elbow_right[2] > 0.1 and shoulder_right[2] > 0.1 and palm_right[1] < elbow_left[1] and elbow_right[1] < elbow_left[1]:
        temp_palm_elbow = [palm_left[0], palm_left[1], elbow_right[0], elbow_right[1]]
        temp_elbow_shoulder = [elbow_right[0], elbow_right[1], shoulder_right[0], shoulder_right[1]]
        result_angle = angle(temp_palm_elbow, temp_elbow_shoulder)
        if result_angle < 60:
            skill_long.j()
            return True
    return


# 腿
def leg(hip_right, knee_right, hip_left, knee_left):
    if hip_right[2] > 0.1 and knee_right[2] > 0.1:
        temp_hip_knee_right = [hip_right[0], hip_right[1], knee_right[0], knee_right[1]]
        temp_hip_knee_left = [hip_left[0], hip_left[1], knee_left[0], knee_left[1]]
        angle2 = angle(temp_hip_knee_right, temp_hip_knee_left)
        if angle2 < 30:
            skill_long.k()
            return True
    # if hip_right[2] > 0.1 and knee_right[2] > 0.1:
    #     temp_hip_knee_right = [hip_right[0], hip_right[1], knee_right[0], knee_right[1]]
    #     temp_hip_knee_left = [hip_left[0], hip_left[1], knee_left[0], knee_left[1]]
    #     angle2 = angle(temp_hip_knee_right, temp_hip_knee_left)
    #     if angle2 > 30:
    #         move.k()
    #         return True
    return


# 曝气
def unparalleled(palm_left, elbow_left, palm_right, elbow_right, shoulder_left, shoulder_right, jj, core):
    if palm_left[2] > 0.1 and elbow_left[0] > 0.1 and palm_right[2] > 0.1 and elbow_right[2] > 0.1 and shoulder_left[2] > 0.1 and shoulder_right[2] > 0.1 and jj[2] > 0.1 and core[2] > 0.1:
        temp_palm_elbow_left = [[palm_left[0], palm_left[1]], [elbow_left[0], elbow_left[1]]]
        temp_palm_elbow_right = [[palm_right[0], palm_right[1]], [elbow_right[0], elbow_right[1]]]
        (result1, result2) = line_intersection(temp_palm_elbow_left, temp_palm_elbow_right)
        y_top = core[1]
        y_bottom = jj[1]
        x_left = shoulder_left[0]
        x_right = shoulder_right[0]
        if result1 < x_left and result1 > x_right and result2 > y_top and result2 < y_bottom and palm_left[0] < palm_right[0]:
            skill_long.o()
            return True
    return False


# 翻滚
def roll_left(palm_right, palm_left, knee_right, knee_left):
    if (palm_right[2] > 0.1 and knee_right[2] > 0.1) or (palm_left[2] > 0.1 and knee_left[2] > 0.1):
        if palm_right[1] > knee_right[1] or palm_right[1] > knee_right[1]:
            skill_long.roll_right()
            return True
        if palm_left[1] > knee_left[1] or palm_left[1] > knee_right[1]:
            skill_long.roll_left()
            return True
    return False


# 计算两个直线的夹角 只要夹角
def angle(v1, v2):
    dx1 = v1[2] - v1[0]
    dy1 = v1[3] - v1[1]
    dx2 = v2[2] - v2[0]
    dy2 = v2[3] - v2[1]
    angle1 = math.atan2(dy1, dx1)
    angle1 = int(angle1 * 180 / math.pi)
    # print(angle1)
    angle2 = math.atan2(dy2, dx2)
    angle2 = int(angle2 * 180 / math.pi)
    # print(angle2)
    if angle1 * angle2 >= 0:
        included_angle = abs(angle1 - angle2)
    else:
        included_angle = abs(angle1) + abs(angle2)
        if included_angle > 180:
            included_angle = 360 - included_angle
    return abs(90 - included_angle)


# 两个线的交点
def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])
    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]
    div = det(xdiff, ydiff)
    if div == 0:
        raise Exception('lines do not intersect')
    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y
