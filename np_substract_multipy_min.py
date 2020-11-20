#导入numpy
"""

加法
[[10 11 12]
 [13 14 15]
 [16 17 18]]
[[10 11 12]
 [13 14 15]
 [16 17 18]]
减法
[[10  9  8]
 [ 7  6  5]
 [ 4  3  2]]
[[10  9  8]
 [ 7  6  5]
 [ 4  3  2]]
[[ 0 10 20]
 [30 40 50]
 [60 70 80]]
[ 0.         -0.98803162 -0.30481062  0.89399666]
around: [  1.   5. 123.   1.  25.]
ceil: [  1.   5. 123.   1.  26.]
floor: [  1.   4. 123.   0.  25.]
原数组a
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
power: [[  1   4   9  16]
 [ 25  36  49  64]
 [ 81 100 121 144]]
[ 1.  2.  4.  8. 16.  0.  0.  0.  0.  0.]
2.5
3.0
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
垂直方向  [5. 6. 7. 8.]
水平方向  [ 2.5  6.5 10.5]
3.2
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
axis=0 垂直方向 [5. 6. 7. 8.]
axis=1 水平方向 [ 2.5  6.5 10.5]
max: 5
sum: 16
min: 2
argmin: 2
argmax: 3


"""
import numpy as np
a=np.arange(9).reshape(3,3)
print(np.arange(9))
b=np.array([10,10,10])
print('加法')
print(np.add(a,b))
print(a+b)
print('减法')
print(np.subtract(b,a))
print(b-a)

#out参数的使用
y=np.empty((3,3),dtype=np.int)
np.multiply(a,10,out=y)
print(y)

#三角函数
a=np.array([0,30,60,90])
print(np.sin(a))

#around ceil floor
a = np.array([1.0,4.55,  123,  0.567,  25.332])
print('around:',np.around(a))
print('ceil:',np.ceil(a))
print('floor:',np.floor(a))

#统计函数
# power()
a=np.arange(1,13).reshape(3,4)
print('原数组a')
print(a)
print('power:',np.power(a,2))

#power中out的使用
x=np.arange(5)
y=np.zeros(10)
np.power(2,x,out=y[:5])
print(y)

#  median ()
#一维数组的中位数
a=np.array([4,3,2,5,2,1]) #对数组排序 [1,2,2,3,4,5]  数组中元素个数为偶数 中位数指：中间两个数的平均值
print(np.median(a))

a=np.array([4,3,2,5,2]) #对数组排序 [2,2,3,4,5]  数组中元素个数为奇数 中位数指：中间的数
print(np.median(a))

#二维数组  要通过axis指定轴
a=np.arange(1,13).reshape(3,4)
print(a)
print('垂直方向 ',np.median(a,axis=0))
print('水平方向 ',np.median(a,axis=1))

#mean 求平均值
#一维数组
a=np.array([4,3,2,5,2])
print(np.mean(a))
#二维数组   axis指定轴求平均
a=np.arange(1,13).reshape(3,4)
print(a)
print('axis=0 垂直方向',np.mean(a,axis=0))
print('axis=1 水平方向',np.mean(a,axis=1))

#sum()  max()  min()
a=np.array([4,3,2,5,2])
print('max:',np.max(a))
print('sum:',np.sum(a))
print('min:',np.min(a))

#argmax argmin
print('argmin:',np.argmin(a))
print('argmax:',np.argmax(a))

a = np.arange(4).reshape(2,2)
print(a)
x,y = np.min(a,axis = 0)
print(x)
print(y)