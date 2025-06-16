import random
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# تعریف شبکه 10x10 و مختصات شروع و مقصد
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2],  # 2 نشان‌دهنده مقصد (D) در خانه (9, 0)
]

start_position = (9, 0)  # موقعیت شروع (ردیف، ستون)
destination = (0, 9)     # تغییر موقعیت مقصد به (9, 0)

current_position = start_position
moves = 0
failures = 0
running = False
speed = 0.06  # سرعت حرکت مهره به ثانیه (۵ برابر سریع‌تر از قبل)

def is_valid_move(grid, position):
    """بررسی می‌کند که حرکت معتبر است یا خیر."""
    rows, cols = len(grid), len(grid[0])
    x, y = position
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] != 1  # خانه سیاه با مقدار 1 غیرمعتبر است

def plot_grid(grid, current_position):
    """نمایش گرافیکی شبکه و موقعیت فعلی."""
    plt.clf()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                plt.fill_between([j, j+1], i, i+1, color='black')
            elif grid[i][j] == 2:
                plt.fill_between([j, j+1], i, i+1, color='green')
            else:
                plt.fill_between([j, j+1], i, i+1, color='white')

    # رسم خطوط شطرنجی
    for i in range(len(grid) + 1):
        plt.plot([0, len(grid[0])], [i, i], color='gray', linewidth=0.5)
    for j in range(len(grid[0]) + 1):
        plt.plot([j, j], [0, len(grid)], color='gray', linewidth=0.5)

    # رسم موقعیت فعلی مهره
    plt.plot(current_position[1] + 0.5, len(grid) - current_position[0] - 0.5, 'ro', markersize=15)
    plt.xlim(0, len(grid[0]))
    plt.ylim(0, len(grid))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xticks(range(len(grid[0])))
    plt.yticks(range(len(grid)))
    plt.gca().invert_yaxis()
    plt.draw()

def random_walk(event):
    global current_position, moves, failures, running, speed
    if running:
        return
    running = True
    previous_position = current_position
    while current_position != destination:
        plot_grid(grid, current_position)
        plt.pause(speed)
        n = random.random()
        if 0 <= n <= 0.25 : 
            direction = (0,1)
        elif 0.25 < n <= 0.5 : 
            direction = (0, -1)
        elif 0.5 < n <= 0.75 : 
            direction = (1,0)
        elif 0.75 < n <= 1 : 
            direction = (-1,0)
        # direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])  # راست، چپ، پایین، بالا
        new_position = (current_position[0] + direction[0], current_position[1] + direction[1])

        if is_valid_move(grid, new_position):
            # اگر به خانه سیاه نرفته باشیم، حرکت به خانه جدید می‌کنیم
            previous_position = current_position
            current_position = new_position
        else:
            # اگر به خانه سیاه (1) برویم، به خانه قبلی برمی‌گردیم
            current_position = previous_position
            failures += 1  # شکست ثبت می‌شود

        # اگر مهره قرمز وارد خانه سبز (مقصد) شد، متوقف می‌شود
        if current_position == destination:
            break

        moves += 1

    # محاسبه نسبت یکنواخت بودن
    ratio = moves / (moves + failures)
    uniformity = 'یکنواخت' if 0.4 <= ratio <= 0.6 else 'غیریکنواخت'

    plot_grid(grid, current_position)
    
    # چاپ نتایج
    print(f"تعداد حرکات لازم برای رسیدن به مقصد: {moves}")
    print(f"تعداد شکست‌ها قبل از رسیدن به مقصد: {failures}")
    print(f"آیا دنباله A/(A+B) یکنواخت است؟ {uniformity}")

    running = False

def reset(event):
    global current_position, moves, failures, running
    current_position = start_position
    moves = 0
    failures = 0
    running = False
    
    plot_grid(grid, current_position)

def exit_program(event):
    plt.close()

# راه‌اندازی پنجره رسم
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
plot_grid(grid, current_position)

# دکمه‌ها
start_ax = plt.axes([0.1, 0.05, 0.2, 0.075])
reset_ax = plt.axes([0.4, 0.05, 0.2, 0.075])
exit_ax = plt.axes([0.7, 0.05, 0.2, 0.075])

start_button = Button(start_ax, 'Start')
reset_button = Button(reset_ax, 'reset')
exit_button = Button(exit_ax, 'exit')

start_button.on_clicked(random_walk)
reset_button.on_clicked(reset)
exit_button.on_clicked(exit_program)

plt.show()
