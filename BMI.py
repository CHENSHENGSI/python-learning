# BMI = 体重（kg）/身高(m)^2

weight = float(input('请输入您的体重（kg）:'))
height = float(input('请输入您的身高（m）:'))

BMI = weight/height**2
print("您的BMI为:",BMI)


# 函数写法
# 1.定义身高和体重两变量  以及BMI
# 2.返回BMI
def BMI(w,h):

    w  = input('请输入您的体重:')
    h = input('请输入您的身高:')
    result = float(w)/float(h)**2
    return result

print(BMI(65,1.62))