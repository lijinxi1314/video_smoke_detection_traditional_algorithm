# video_smoke_detection_traditional_algorithm


使用传统算法进行视频烟雾检测
1 使用optical flow 获得视频内的移动区域候选框（使用光流法进行目标跟踪（确定视频当前帧的像素的移动）open operation -> threshold->来查找物体的轮廓—>将这些的物体轮廓进行proposal 候选框的提取）

2	判断烟雾的形状是否为凸型->一个区域被平行5条线，垂直5条线均分，检验每条线上的属于背景区域的像素，若背景像素大于三个，说明这条线上有背景区域。一共10条线，若3条线满足上述条件，则说明有烟雾的存在

3 通过小波能量的变换判断是否有烟雾。提取每一个候选区图片的小波信息选择HL,LH,HH高低频区域的像素的绝对值之和，作为其小波能量特征。由于烟雾出现，该候选区域的物体的边界会变的模糊，其小波能量也会减少。(求能量的时候，能量值太大可进行归一化，如能量和除以候选区内元素的个数)

4 通过烟雾的色度来判断是否有烟雾。由于烟雾的出现图像的u,v channel的值也会变小

