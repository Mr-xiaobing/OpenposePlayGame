import time

import pyautogui

# 技能


# 左移
def left():
    pyautogui.keyDown("a")
    time.sleep(0.2)
    pyautogui.keyUp("a")


# 又移
def right():
    pyautogui.keyDown("d")
    time.sleep(0.2)
    pyautogui.keyUp("d")


def top():
    pyautogui.hotkey("w")


def bottom():
    pyautogui.hotkey("s")


def j():
    pyautogui.hotkey("j")


def k():
    pyautogui.hotkey("k")


def l():
    pyautogui.hotkey("l")


def o():
    print("使用曝气/必杀技")
    pyautogui.hotkey("o")


def u():
    pyautogui.hotkey("u")


def i():
    print("使用大号升龙拳")
    pyautogui.hotkey("i")


def roll_right():
    print("使用翻滚")
    pyautogui.keyDown("d")
    pyautogui.press("l")
    pyautogui.keyUp("d")


def roll_left():
    print("使用翻滚")
    pyautogui.keyDown("a")
    pyautogui.press("l")
    pyautogui.keyUp("a")


# 只有在左边能用出来
def sheng_long_boxing_right():
    print("使用升龙拳")
    pyautogui.hotkey("s")
    pyautogui.hotkey("d", "j")


# 只有在左边能用出来
def sheng_long_boxing_left():
    print("使用升龙拳")
    pyautogui.hotkey("s")
    pyautogui.hotkey("a", "j")


# 冲击波
def shock_wave_right():
    print("使用冲击波")
    pyautogui.hotkey("d", "j")


# 冲击波
def shock_wave_left():
    print("冲击波")
    pyautogui.hotkey("a", "j")


# 旋风腿
def xuan_feng_leg_right():
    print("使用旋风腿")
    pyautogui.hotkey("a", "k")


# 旋风腿
def xuan_feng_leg_left():
    print("使用旋风腿")
    pyautogui.hotkey("d", "k")


if __name__ == '__main__':
     while(True):
        #  测试能不能按出对应的招式
        pyautogui.hotkey("a", "k")