from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# اطلاعات ورود
username = "4001830235"
password = "1363426370"

# مسیر درایور کروم (دانلود شده از: https://chromedriver.chromium.org/)
driver_path = "chromedriver.exe"  # یا مسیر کامل مثلاً "/home/user/chromedriver"

# شروع مرورگر
driver = webdriver.Chrome(executable_path=driver_path)

# باز کردن صفحه لاگین
driver.get("https://dinning.azaruniv.ac.ir//nutLogin.asp")
time.sleep(2)

# پیدا کردن فیلد یوزرنیم و پسورد
driver.find_element(By.NAME, "txtcode").send_keys(username)
driver.find_element(By.NAME, "txtpass").send_keys(password)

# کلیک روی دکمه ورود
driver.find_element(By.NAME, "B1").click()

# چند ثانیه صبر کنه برای مشاهده نتیجه
time.sleep(5)

# مرورگر رو نبندیم (موقتی برای تست)
# driver.quit()
