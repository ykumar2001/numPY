import numpy as np
# arr1=np.array([1,2,3,4])
# arr2=np.array([[1,2],[3,4]])

# print(arr1)
# print(arr2)

# zeros=np.zeros((2,3))
# ones=np.ones((3,3))
# random_arr=np.random.rand(3,3)
# print(zeros)
# print(ones)
# print(random_arr)

# arr=np.arange(0,10)
# arr_linspace=np.linspace(0,1)
# print(arr)
# print(arr_linspace)

# arr=np.array([1,2,3,4,5,6])
# print(arr[0])
# print(arr[-1])
# print(arr[1:3])
# print(arr[:3])

# a=np.array([1,2,3])
# b=np.array([4,5,6])
# print(a+b)
# print(a*b)
# print(a**2)

# a=np.array([[1,2],[3,4]])
# b=np.array([[5,6],[7,8]])
# c=np.dot(a,b)
# print(c)

# arr=np.array([1,2,3,4,5,6])
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.std(arr))
# print(np.max(arr))
# print(np.min(arr))

# arr=np.array([1,2,3,4,5,6])
# reshaped_arr=arr.reshape((2,3))
# print(reshaped_arr)

# a=np.array([1,2,3])
# b=np.array([[1],[2],[3]])
# print(a+b)

arr=np.array([1,2,3])
view=arr.view()
view[0]=100
print(arr)


arr=np.array([1,2,3])
copy=arr.copy()
copy[0]=100
print(arr)