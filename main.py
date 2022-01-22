import argparse
import os
import sys
import cv2
import action_long

if __name__ == '__main__':
    try:
        # 导入 openpose 库
        # 这里改为你的  openpose放置的地址
        path = "C:\\Users\\Administrator\\Desktop\\openpose-master\\build\\python\\openpose\\Release"
        # 这里改为你的  openpose放置的地址
        bin_path = "C:\\Users\\Administrator\\Desktop\\openpose-master\\build\\bin"
        sys.path.append(path)
        # 追加到系统环境变量
        os.environ['Path'] =os.environ['Path']+";"+"C:\\Users\\Administrator\\Desktop\\openpose-master\\build\\x64\\Release;"+bin_path+";"+path+";"
        print(os.environ["Path"])
        import pyopenpose as op
        # Flags
        parser = argparse.ArgumentParser()
        args = parser.parse_known_args()
        # Custom Params (refer to include/openpose/flags.hpp for more parameters)
        params = dict()
        # 需要加载模型
        # 这里改为你openpose放置的地址
        params["model_folder"] = "C:\\Users\\Administrator\\Desktop\\openpose-master\\models/"
        # Add others in path?
        for i in range(0, len(args[1])):
            curr_item = args[1][i]
            if i != len(args[1]) - 1:
                next_item = args[1][i + 1]
            else:
                next_item = "1"
            if "--" in curr_item and "--" in next_item:
                key = curr_item.replace('-', '')
                if key not in params:  params[key] = "1"
            elif "--" in curr_item and "--" not in next_item:
                key = curr_item.replace('-', '')
                if key not in params: params[key] = next_item
        opWrapper = op.WrapperPython()
        opWrapper.configure(params)
        opWrapper.start()
        # 获取摄像头的视频（opencv是按帧来获取的，然后用while进行一帧一帧的识别
        cap = cv2.VideoCapture(0)
        # 录制
        # fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 视频存储的格式
        # size = (516, 516)
        # out = cv2.VideoWriter("output.avi", fourcc, 8, size)
        while cap.isOpened():
            ref, image = cap.read()
            datum = op.Datum()
            x, y = image.shape[0:2]
            imageToProcess = image
            datum.cvInputData = imageToProcess
            # 模型识别识别操作
            opWrapper.emplaceAndPop(op.VectorDatum([datum]))
            if datum.poseKeypoints is not None:
                # 生成的结果  datum.poseKeypoints 这是一个数组.详细数组的解释请查看 README 这个打印可以去掉
                # openpose可以检测多人。检测到的人数(可以开发多人对打模式。)
                personNum = len(datum.poseKeypoints)
                for i in range(personNum):
                    action_long.operation(datum.poseKeypoints[i])
                    # 如果有人观看我的电脑，并且屏幕在游戏页面的话  则切换到工作页面
            #  在你的电脑进行展示
            image_new = cv2.flip(datum.cvOutputData,1)
            cv2.imshow("真人拳皇", image_new)
            # 视频的录制,生成一个 (out = cv2.VideoWriter("output.avi", fourcc, 8, size))  output.avi的视频
            # out.write(datum.cvOutputData)
            cv2.waitKey(127)
        cap.release()
    except Exception as e:
        print(e)
        sys.exit(-1)


