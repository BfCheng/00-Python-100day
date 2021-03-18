# 分支结构
# 刷题01 分支结构
# 英制单位与公制厘米的互换
# class Interconvert:
#     def __init__(self, value, unit):
#         self.value = value
#         self.unit = unit
#     def InInterconvertCm(self):
#         self.value = float(input('请输入长度: '))
#         self.unit = input('请输入单位: ')
#         if self.unit == 'in' or self.unit == '英寸':
#             return ('%f英寸 = %f厘米' % (value, value * 2.54))
#         elif self.unit == 'cm' or self.unit == '厘米':
#             return('%f厘米 = %f英寸' % (value, value / 2.54))
#         else:
#             return('请输入有效的单位')
#             return('你错了')
# value = Interconvert(45, 'cm')
# # unit = Interconvert('cm')
# =======================*****************************=========================== #
# 刷题02 百分制成绩转换为等级制成绩
# score = float(input('请输入成绩：'))
# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     grade = 'E'
# print('对应的等级是：', grade)
# =======================*****************************=========================== #
# # 刷题03 输入三条边，如果能构成三角形就计算周长和面积
# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
# if a + b > c and a + c > b and b + c > a:
#     print('周长: %f' % (a + b + c))
#     p = (a + b + c) / 2
#     area = (p * (p - a) * (p - b) * (p - c)) ** 0.5     #海伦公式
#     print('面积: %f' % (area))
# else:
#     print('不能构成三角形')
# =======================*****************************=========================== #
# 循环结构
# 刷题03 输入三条边，如果能构成三角形就计算周长和面积
# numbers = [12, 34, 45, 67, 76, 37, 89, 1]
# even = []
# odd = []
# while len(numbers) >0:
#     number = numbers.pop()
#     if number % 2 == 0:
#         even.append(number)
#     else:
#         odd.append(number)
# print(even)
# print(odd)
# =======================*****************************=========================== #
# 循环

