import pygame
import random
import time

# اندازه صفحه
CELL_SIZE = 50
GRID_SIZE = 10

# رنگ‌ها
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# تنظیمات تاس
DICE_SIZE = 100
DICE_POS = (GRID_SIZE * CELL_SIZE + 20, 20)

# مقصد
destination = (0, GRID_SIZE - 1)  # خانه مقصد در بالا سمت راست

# ساخت صفحه شطرنج
def create_grid():
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    
    # قرار دادن موانع سیاه به طور تصادفی
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if random.random() < 0.2:  # 20% احتمال برای قرار دادن مانع
                grid[i][j] = 1
    return grid

# نمایش صفحه شطرنج
def draw_grid(screen, grid, red_pos, dice_roll):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            color = WHITE if grid[row][col] == 0 else BLACK
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, (200, 200, 200), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
    
    pygame.draw.circle(screen, RED, (red_pos[1] * CELL_SIZE + CELL_SIZE // 2, red_pos[0] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

    # نمایش تاس
    draw_dice(screen, dice_roll)

    # نمایش مقصد
    pygame.draw.circle(screen, GREEN, (destination[1] * CELL_SIZE + CELL_SIZE // 2, destination[0] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

# رسم تاس
def draw_dice(screen, roll):
    font = pygame.font.Font(None, 74)
    pygame.draw.rect(screen, YELLOW, (DICE_POS[0], DICE_POS[1], DICE_SIZE, DICE_SIZE))
    pygame.draw.rect(screen, BLACK, (DICE_POS[0], DICE_POS[1], DICE_SIZE, DICE_SIZE), 5)
    text = font.render(str(roll), True, BLACK)
    screen.blit(text, (DICE_POS[0] + DICE_SIZE // 2 - text.get_width() // 2, DICE_POS[1] + DICE_SIZE // 2 - text.get_height() // 2))

# شبیه‌سازی پرتاب تاس
def roll_dice():
    return random.randint(1, 6)

# حرکت مهره قرمز بر اساس نتیجه تاس
def move_piece(red_pos, roll, grid):
    previous_pos = red_pos  # ذخیره موقعیت قبلی
    if roll == 1 or roll == 2 or roll == 3:  # حرکت به بالا
        if red_pos[0] > 0:
            red_pos = (red_pos[0] - 1, red_pos[1])
    elif roll == 4:  # حرکت به پایین
        if red_pos[0] < GRID_SIZE - 1:
            red_pos = (red_pos[0] + 1, red_pos[1])
    elif roll == 5:  # حرکت به راست
        if red_pos[1] < GRID_SIZE - 1:
            red_pos = (red_pos[0], red_pos[1] + 1)
    elif roll == 6:  # حرکت به چپ
        if red_pos[1] > 0:
            red_pos = (red_pos[0], red_pos[1] - 1)

    # بررسی برخورد با خانه سیاه
    if grid[red_pos[0]][red_pos[1]] == 1:  # اگر خانه سیاه باشد
        red_pos = previous_pos  # به خانه قبلی برگرد
    return red_pos

# اجرای بازی
def main():
    pygame.init()
    screen = pygame.display.set_mode((GRID_SIZE * CELL_SIZE + DICE_SIZE + 40, GRID_SIZE * CELL_SIZE))
    pygame.display.set_caption('Chessboard Navigation with Dice')
    
    grid = create_grid()
    red_pos = (GRID_SIZE - 1, 0)  # شروع از گوشه پایین چپ
    move_count = 0  # شمارش حرکت‌ها
    failure_count = 0  # شمارش شکست‌ها
    move_delay = 50  # تاخیر حرکت مهره قرمز (10 برابر سریع‌تر)
    roll_sequence = []  # دنباله تاس‌ها
    running = True
    clock = pygame.time.Clock()
    dice_roll = roll_dice()  # پرتاب اولیه تاس
    
    while running:
        screen.fill((255, 255, 255))  # پس‌زمینه سفید
        draw_grid(screen, grid, red_pos, dice_roll)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # حرکت مهره قرمز بر اساس تاس
        previous_pos = red_pos
        red_pos = move_piece(red_pos, dice_roll, grid)

        # اگر حرکت شکست خورد (به خانه سیاه خورد یا از صفحه خارج شد)
        if red_pos == previous_pos:
            failure_count += 1

        move_count += 1  # افزایش شمارش حرکت‌ها

        # تاس زدن بعدی
        dice_roll = roll_dice()
        roll_sequence.append(dice_roll)  # ذخیره دنباله تاس‌ها
        
        # بررسی رسیدن به مقصد
        if red_pos == destination:
            print(f"مهره قرمز به مقصد رسید!")
            print(f"تعداد حرکت‌ها: {move_count}")
            print(f"تعداد شکست‌ها: {failure_count}")
            
            # تحلیل دنباله تصادفی
            A = sum(1 for roll in roll_sequence if roll in [1, 2, 3])  # تعداد حرکات به بالا
            B = sum(1 for roll in roll_sequence if roll == 4)  # تعداد حرکات به پایین
            ratio = A / (A + B) if A + B > 0 else 0
            print(f"دنباله تصادفی A/(A+B): {ratio:.2f}")
            
            # بررسی یکنواختی دنباله
            if ratio == 0.5:
                print("دنباله تصادفی یکنواخت است.")
            else:
                print("دنباله تصادفی غیر یکنواخت است.")
            
            running = False

        # بعد از هر حرکت، 0.05 ثانیه صبر می‌کنیم
        time.sleep(move_delay / 1000)
        
        pygame.display.flip()
        clock.tick(10)  # تنظیم سرعت بازی

    pygame.quit()

if __name__ == "__main__":
    main()
