#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/input.h>
#include <linux/init.h>
#include <linux/timer.h>
static struct input_dev *kbd_dev;
static struct timer_list blink_timer;
static void blink_led(struct timer_list *t)
{
    static bool led_state = false;
    led_state = !led_state;
    input_event(kbd_dev, EV_LED, LED_CAPSL, led_state);  // استفاده از input_event برای تغییر وضعیت LED
    input_sync(kbd_dev);  // ارسال تغییرات به دستگاه
    mod_timer(&blink_timer, jiffies + msecs_to_jiffies(500));  // تنظیم تایمر برای ادامه
}
static int __init led_blink_init(void)
{
    printk(KERN_INFO "LED blink module loading...\n");
    // ایجاد دستگاه ورودی
    kbd_dev = input_allocate_device();
    if (!kbd_dev)
        return -ENOMEM;
    kbd_dev->evbit[0] = BIT(EV_LED);
    kbd_dev->ledbit[0] = BIT(LED_CAPSL);
    // ثبت دستگاه ورودی
    if (input_register_device(kbd_dev)) {
        input_free_device(kbd_dev);
        return -EIO;
    }
    // تنظیم تایمر
    timer_setup(&blink_timer, blink_led, 0);
    mod_timer(&blink_timer, jiffies + msecs_to_jiffies(500));  // شروع تایمر
    return 0;
}
static void __exit led_blink_exit(void)
{
    printk(KERN_INFO "LED blink module unloading...\n");
    // حذف تایمر و خاموش کردن LED
    del_timer_sync(&blink_timer);
    input_unregister_device(kbd_dev);
    input_free_device(kbd_dev);
}
module_init(led_blink_init);
module_exit(led_blink_exit);
MODULE_LICENSE("GPL");
MODULE_AUTHOR("Narges");
MODULE_DESCRIPTION("A kernel module that blinks the keyboard LEDs.");
