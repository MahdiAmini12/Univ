# import random
# import math

# def value(a, b, c, d):
#     return (a + 2 * b + 3*c + 4*d - 30)
    


# zhen= []
# for i in range(6):
#     zhen.append([random.randint(0,100) for i in range(4)])

#     a, b, c, d = zhen[0][0], zhen[0][1], zhen[0][2], zhen[0][3]
#     print('value = ', value(a, b, c, d))
#     print(f"n{i} -> {zhen[i]}")


# average1 = [(sum(zhen[i])/4) for i in range (len(zhen))]
# # print(average)
# for i in range(2):
#     average1.remove(max(average1))
# print("first average: ", average1)

# zhen= [average1]    # fagat n0 hast toosh

# for i in range(6):
#     # zhen = []
#     zhen.append([random.randint(0,60) for i in range(4)])
#     print(f"n{i} -> {zhen[i]}")
    

# average2 = [(sum(zhen[i])/4) for i in range (len(zhen))]
# # print(average)
# for i in range(2):
#     average2.remove(max(average2))
# print("second average: ", average2)

# zhen= [average1, average2]    # fagat n0, n1 hast toosh
# for i in range(6):
#     # zhen = []
#     zhen.append([random.randint(0,30) for i in range(4)])
#     print(f"n{i} -> {zhen[i]}")
    


# average3 = [(sum(zhen[i])/4) for i in range (len(zhen))]
# # print(average)
# for i in range(2):
#     average3.remove(max(average3))
# print("third average: ", average3)

# zhen= [average1, average2, average3]    # fagat n0, n1, n2 hast toosh
# for i in range(6):
#     # zhen = []
#     zhen.append([random.randint(0,10) for i in range(4)])
#     print(f"n{i} -> {zhen[i]}")
    

# average4 = [(sum(zhen[i])/4) for i in range (len(zhen))]
# # print(average)
# for i in range(2):
#     average4.remove(max(average4))
# print("forth average: ", average4)

# zhen= [average1, average2, average3, average4]    # fagat n0, n1, n2, n3 hast toosh
# for i in range(6):
#     # zhen = []
#     zhen.append([random.randint(0,5) for i in range(4)])
#     print(f"n{i} -> {zhen[i]}")
    

# average5 = [(sum(zhen[i])/4) for i in range (len(zhen))]
# # print(average)
# for i in range(2):
#     average5.remove(max(average5))
# print("fifth average: ", average5)

# zhen= [average1, average2, average3, average4, average5]    # fagat n0, n1, n2, n3, n4 hast toosh
# for i in range(6):
#     # zhen = []
#     zhen.append([random.randint(0,6) for i in range(4)])
#     print(f"n{i} -> {zhen[i]}")


# average6 = [(sum(zhen[i])/4) for i in range (len(zhen))]
# # print(average)
# for i in range(7):
#     average6.remove(max(average6))
# for j in range (len(average6)):
#     a, b,c,d = average6[0], average6[1], average6[2], average6[3]
#     # print("value is :", value(a, b, c, d))
# print("sixth average: ", average6)


# for i in range(6):
#     print(f"n{i} -> {zhen[i]}")
#     a = zhen[0]
    


# zhen= [average1, average2, average3, average4, average5, average6]    # fagat n0, n1, n2, n3, n4, n5 hast toosh
# # print("Lennnnn: " , len(zhen))
# print(zhen)


# # for i in zhen[i]:
# #     for j in zhen[i][j]:
# #         print('value = ', value(a, b, c, d))cmd


# a, b, c, d = zhen[5][0], zhen[5][1], zhen[5][2], zhen[5][3]
# print('value = ', value(a, b, c, d))

########################################################################

# from collections import deque
# import pygame
# import sys
# import random

# # تنظیمات اولیه pygame
# pygame.init()
# width, height = 600, 600  # ابعاد صفحه نمایش
# rows, cols = 8, 8  # تعداد سطرها و ستون‌ها در صفحه شطرنجی
# cell_size = width // rows  # اندازه هر خانه بر اساس ابعاد صفحه

# # تعریف رنگ‌ها
# WHITE = (255, 255, 255)  # رنگ سفید
# BLACK = (0, 0, 0)  # رنگ سیاه
# GREEN = (0, 255, 0)  # رنگ سبز برای خانه شروع
# RED = (255, 0, 0)  # رنگ قرمز برای خانه هدف
# BLUE = (0, 0, 255)  # رنگ آبی برای مسیر طی شده

# # صفحه نمایش برای رسم شطرنج
# screen = pygame.display.set_mode((width, height))

# # ایجاد صفحه شطرنجی با خانه‌های سفید
# board = [[WHITE for _ in range(cols)] for _ in range(rows)]

# # اضافه کردن چندین خانه سیاه به صورت تصادفی
# for _ in range(10):  # تعداد خانه‌های سیاه که به صورت تصادفی تعیین می‌شوند
#     x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
#     board[x][y] = BLACK  # تغییر رنگ خانه به سیاه

# # موقعیت شروع و موقعیت هدف روی صفحه شطرنج
# start_pos = (0, 1)  # مختصات خانه شروع
# target_pos = (7, 6)  # مختصات خانه هدف

# # تابعی برای رسم کل صفحه شطرنج
# def draw_board():
#     for row in range(rows):
#         for col in range(cols):
#             color = board[row][col]  # تعیین رنگ خانه
#             # رسم خانه
#             pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))
#             # اضافه کردن حاشیه سیاه برای هر خانه
#             pygame.draw.rect(screen, BLACK, (col * cell_size, row * cell_size, cell_size, cell_size), 1)

# # حرکت‌های مجاز در صفحه (چهار جهت اصلی)
# directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # راست، پایین، چپ، بالا

# # تابع BFS برای پیدا کردن کوتاه‌ترین مسیر از شروع تا هدف
# def bfs_shortest_path(start, target):
#     queue = deque([(start, [start])])  # ایجاد صف برای ذخیره موقعیت‌ها و مسیرها
#     visited = set([start])  # مجموعه‌ای از خانه‌های بازدید شده برای جلوگیری از بازدید تکراری

#     # جستجوی در طول صف تا زمانی که مسیر به هدف برسد یا صف خالی شود
#     while queue:
#         (x, y), path = queue.popleft()  # گرفتن موقعیت فعلی و مسیر طی شده

#         # بررسی رسیدن به خانه هدف
#         if (x, y) == target:
#             return path  # بازگشت مسیر بهینه در صورت رسیدن به هدف

#         # بررسی حرکت به چهار جهت مختلف از خانه فعلی
#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy  # مختصات خانه جدید بعد از حرکت

#             # بررسی مرزها، رنگ خانه (نباید سیاه باشد) و عدم بازدید قبلی
#             if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] != BLACK and (nx, ny) not in visited:
#                 visited.add((nx, ny))  # اضافه کردن خانه جدید به لیست بازدیدها
#                 queue.append(((nx, ny), path + [(nx, ny)]))  # افزودن خانه جدید به صف به همراه مسیر طی شده

#     return None  # بازگشت None در صورت نبودن مسیر به هدف

# # پیدا کردن مسیر بهینه از خانه شروع به هدف
# optimal_path = bfs_shortest_path(start_pos, target_pos)

# # اگر مسیر بهینه پیدا شد، آن را گرافیکی نمایش می‌دهیم
# if optimal_path:
#     print("تعداد حرکت‌های مسیر بهینه:", len(optimal_path) - 1)  # نمایش تعداد کل حرکت‌ها در مسیر بهینه

#     # حلقه برای نمایش گرافیکی حرکت در مسیر بهینه
#     index = 0
#     while index < len(optimal_path):
#         screen.fill(WHITE)  # پاک کردن صفحه برای رسم جدید
#         draw_board()  # رسم صفحه شطرنج
        
#         # رسم خانه‌های شروع و هدف به رنگ‌های مخصوص
#         pygame.draw.rect(screen, GREEN, (start_pos[1] * cell_size, start_pos[0] * cell_size, cell_size, cell_size))
#         pygame.draw.rect(screen, RED, (target_pos[1] * cell_size, target_pos[0] * cell_size, cell_size, cell_size))
        
#         # رسم مسیر طی شده تا مرحله فعلی به رنگ آبی
#         for i in range(index + 1):
#             x, y = optimal_path[i]
#             pygame.draw.rect(screen, BLUE, (y * cell_size, x * cell_size, cell_size, cell_size))

#         index += 1  # حرکت به خانه بعدی در مسیر
#         pygame.display.flip()  # به‌روزرسانی صفحه نمایش
#         pygame.time.delay(300)  # تأخیر کوتاه برای نمایش بهتر حرکت‌ها

#         # بررسی رخداد خروج برای بستن برنامه
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#     while True:
#         for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()

# # اگر مسیری بهینه یافت نشد، پیام مناسب را چاپ می‌کند
# else:
#     print("مسیر بهینه‌ای یافت نشد.")


# ----DNA

import random

# تابع هدف (محاسبه میزان انطباق یا fitness)
# این تابع بررسی می‌کند که چقدر از مقدار هدف (30) دور هستیم
def fitness(a, b, c, d):
    return abs(a + 2*b + 3*c + 4*d - 30)
    

# تولید جمعیت اولیه (6 کروموزوم با 4 ژن)
# هر ژن نمایانگر یک مقدار برای a, b, c, d است
def create_population(pop_size):
    population = []
    for _ in range(pop_size):
        # تولید کروموزوم با مقادیر تصادفی برای a, b, c, d بین -10 و 10
        individual = [random.randint(-10, 10) for _ in range(4)]
        population.append(individual)
    return population

# انتخاب والدین (2 کروموزوم با بهترین fitness)
# کروموزوم‌ها بر اساس نزدیکی به جواب مرتب می‌شوند
def selection(population):
    # مرتب‌سازی جمعیت بر اساس مقدار fitness (کمترین مقدار بهتر است)
    population.sort(key=lambda x: fitness(*x))
    return population[:2]  # انتخاب دو کروموزوم اول (بهترین‌ها)

# عملگر تقاطع (Crossover)
# این عملگر دو والد را ترکیب کرده و دو فرزند تولید می‌کند

def crossover(parent1, parent2):
    # انتخاب یک نقطه تصادفی برای تقاطع
    point = random.randint(1, 3)
    # تولید دو فرزند از طریق ترکیب والدین
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# عملگر جهش (Mutation)
# یک ژن تصادفی را با احتمال 10 درصد تغییر می‌دهد
def mutation(child):
    if random.random() < 0.1:  # احتمال جهش 10 درصد
        index = random.randint(0, 3)  # انتخاب یک ژن تصادفی
        child[index] = random.randint(-10, 10)  # مقدار جدید تصادفی برای آن ژن
    return child

# الگوریتم ژنتیک 
def genetic_algorithm(pop_size=6, generation=100):
    # تولید جمعیت اولیه
    population = create_population(pop_size)
    
    # اجرای الگوریتم برای تعداد مشخصی از نسل‌ها
    for generation in range(generations):
        # انتخاب والدین
        parent1, parent2 = selection(population)
        
        # تولید فرزندان با استفاده از تقاطع
        child1, child2 = crossover(parent1, parent2)
        
        # اعمال جهش بر روی فرزندان
        child1 = mutation(child1)
        child2 = mutation(child2)
        
        # جایگزینی فرزندان در جمعیت
        population = population[2:]  # حذف دو والد
        population.extend([child1, child2])  # اضافه کردن فرزندان جدید
        
        # بررسی اینکه آیا به جواب رسیده‌ایم
        for individual in population:
            if fitness(*individual) == 0:  # اگر مقدار fitness صفر باشد، جواب پیدا شده است
                print(f"حل پیدا شد در نسل {generation}: {individual}")
                return individual  # بازگشت جواب
    
    # اگر جواب پیدا نشد
    print("حل پیدا نشد")
    return None

# اجرای الگوریتم ژنتیک
solution = genetic_algorithm()
print(fitness(solution[0],solution[1], solution[2], solution[3]))





