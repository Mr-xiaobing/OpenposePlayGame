#              	4399拳皇wing模拟器
​	这个项目可以通过姿态识别来识别动作操作游戏里面的人物使用对应的招式：

​	![效果](https://github.com/Mr-xiaobing/OpenposePlayGame/blob/master/image/%E6%B0%94%E5%8A%9F%E6%B3%A2.png)

​	项目的演示可以查看：https://www.bilibili.com/video/BV1vq4y1c7S7/

​    我电脑的配置是 1080TI + 5600x 玩起来是完全没有问题的。（但是对性能有一定要求的）

## 这个项目使用到的第三库和姿态识别模型有（前期准备）：

​		opencv ：https://opencv.org/（官网）

​		openpose（动作识别识别）：https://github.com/CMU-Perceptual-Computing-Lab/openpose （github）（大家也可以使用别的姿态识别模型）

​		pyautogui（释放招式）：https://github.com/asweigart/pyautogui

​		python版本 3.8

​		**我这边有一个编译好的openpose 我不知道能不能用，大家可以下载试试：**

​		大家也可以自己尝试编译。openpose编译的视频教程（**记得在cmake步骤的时候勾选python,编译出python的第三方库**）：

​		https://www.bilibili.com/video/BV1jQ4y1k76m?p=2



## 自定义设计角色动作和动作

​	我这里**只设计了里面的街霸角色——隆**的动作招式。

​	大家可以设计自己想玩的角色

​	**main.py文件读取摄像头得到关节点，action.py文件根据节点判断(动作设计），判断成功调用对应skill.py中的技能招式。**

（关于双人模式我有一个想法，就是分好区域一人一边，规定好谁控制谁。openpose是支持多人识别的。有同志想弄的话）

​	人体关节点图：

![人体关节点图](https://github.com/Mr-xiaobing/OpenposePlayGame/blob/master/image/%E4%BA%BA%E4%BD%93%E5%90%84%E4%B8%AA%E8%8A%82%E7%82%B9.jpg)

```
print( motion.operation(datum.poseKeypoints[0]))
打印出的人体关节点的信息（记得动作设计的时候注意区分左右）

数组：

[
   第一个人
    [
            坐标X             坐标 Y         准确度
          [0.00000000e+00 0.00000000e+00 0.00000000e+00] // 鼻子  0
          [2.09311020e+02 1.64949844e+02 2.93577045e-01] // 脖子下面（不知道这个位置）  1
          [2.02802353e+02 1.63670731e+02 2.05316409e-01] // 剩下的依次按图  2 右边肩膀
          [0.00000000e+00 0.00000000e+00 0.00000000e+00]   // 右边肘 （记得动作设计的时候注意区分左右）
          [0.00000000e+00 0.00000000e+00 0.00000000e+00]
          [0.00000000e+00 0.00000000e+00 0.00000000e+00]
          [0.00000000e+00 0.00000000e+00 0.00000000e+00]
          [0.00000000e+00 0.00000000e+00 0.00000000e+00]
          [2.04113098e+02 2.01509033e+02 2.93194354e-01]
          [2.01507797e+02 2.01491440e+02 2.47375146e-01]
          [1.94979874e+02 2.23672958e+02 1.17320523e-01]
          [1.93663696e+02 2.45888687e+02 1.00509174e-01]
          [2.09321976e+02 2.02781281e+02 2.85587937e-01]
          [2.04107986e+02 2.22376419e+02 1.47930026e-01]
          [2.02821365e+02 2.49784515e+02 1.39970988e-01]
          [0.00000000e+00 0.00000000e+00 0.00000000e+00]
          [0.00000000e+00 0.00000000e+00 0.00000000e+00]
          [0.00000000e+00 0.00000000e+00 0.00000000e+00]
          [0.00000000e+00 0.00000000e+00 0.00000000e+00]
          [2.01489700e+02 2.53707657e+02 1.24115810e-01]
          [2.01500916e+02 2.54990494e+02 1.16797745e-01]
          [2.04113480e+02 2.53660400e+02 1.36032313e-01]
          [1.91053360e+02 2.47195160e+02 7.76875839e-02]
          [0.00000000e+00 0.00000000e+00 0.00000000e+00]
          [1.93689651e+02 2.48496048e+02 1.02683805e-01]
    ]
    第二个人
    [
          [0.00000000e+00 0.00000000e+00 0.00000000e+00]
          [2.09311020e+02 1.64949844e+02 2.93577045e-01]
          [2.02802353e+02 1.63670731e+02 2.05316409e-01]
          [0.00000000e+00 0.00000000e+00 0.00000000e+00]
          [0.00000000e+00 0.00000000e+00 0.00000000e+00]
          [0.00000000e+00 0.00000000e+00 0.00000000e+00]
          [0.00000000e+00 0.00000000e+00 0.00000000e+00]
          [0.00000000e+00 0.00000000e+00 0.00000000e+00]
          [2.04113098e+02 2.01509033e+02 2.93194354e-01]
          [2.01507797e+02 2.01491440e+02 2.47375146e-01]
          [1.94979874e+02 2.23672958e+02 1.17320523e-01]
          [1.93663696e+02 2.45888687e+02 1.00509174e-01]
          [2.09321976e+02 2.02781281e+02 2.85587937e-01]
          [2.04107986e+02 2.22376419e+02 1.47930026e-01]
          [2.02821365e+02 2.49784515e+02 1.39970988e-01]
          [0.00000000e+00 0.00000000e+00 0.00000000e+00]
          [0.00000000e+00 0.00000000e+00 0.00000000e+00]
          [0.00000000e+00 0.00000000e+00 0.00000000e+00]
          [0.00000000e+00 0.00000000e+00 0.00000000e+00]
          [2.01489700e+02 2.53707657e+02 1.24115810e-01]
          [2.01500916e+02 2.54990494e+02 1.16797745e-01]
          [2.04113480e+02 2.53660400e+02 1.36032313e-01]
          [1.91053360e+02 2.47195160e+02 7.76875839e-02]
          [0.00000000e+00 0.00000000e+00 0.00000000e+00]
          [1.93689651e+02 2.48496048e+02 1.02683805e-01]
    ]
]

```