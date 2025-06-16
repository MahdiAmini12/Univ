#!/bin/bash

# اسامی سرویس‌هایی که می‌خواهیم وضعیت آن‌ها را بررسی کنیم
services=("apache2" "nginx" "ssh")

# پیمایش در لیست سرویس‌ها
for service in "${services[@]}"; do
    # بررسی وضعیت سرویس
    status=$(systemctl is-active $service)

    if [ "$status" == "active" ]; then
        # اگر سرویس در حال اجرا است
        echo "$service is running."
    else
        # اگر سرویس غیرفعال است
        echo "$service is not running. Starting the service..."
        systemctl start $service

        # بررسی دوباره وضعیت سرویس بعد از شروع
        status=$(systemctl is-active $service)
        if [ "$status" == "active" ]; then
            echo "$service started successfully."
        else
            echo "Failed to start $service."
        fi
    fi
done
