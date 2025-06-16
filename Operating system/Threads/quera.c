#include <stdio.h>
#include <pthread.h>
#include <unistd.h> // برای تابع sleep

// تعداد رشته‌ها
#define NUM_THREADS 10

// تابعی که هر رشته اجرا خواهد کرد
void* printHello(void* thread_id) {
    int tid = *(int*)thread_id; // شناسه‌ی رشته
    for (int i = 0; i < 3; i++) {
        printf("Hello, World (thread %d)\n", tid);
        sleep(1); // توقف برای نمایش بهتر خروجی
    }
    pthread_exit(NULL); // خاتمه دادن به رشته
}

int main() {
    pthread_t threads[NUM_THREADS]; // آرایه‌ای از شناسه‌های رشته‌ها
    int thread_ids[NUM_THREADS];    // آرایه‌ای برای نگهداری شناسه‌های رشته‌ها

    // ایجاد رشته‌ها
    for (int i = 0; i < NUM_THREADS; i++) {
        thread_ids[i] = i + 1; // شناسه‌ی رشته‌ها از 1 تا 10
        int rc = pthread_create(&threads[i], NULL, printHello, (void*)&thread_ids[i]);
        if (rc) {
            printf("Error: unable to create thread %d\n", i + 1);
            return 1;
        }
    }

    // انتظار برای خاتمه‌ی تمام رشته‌ها
    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("All threads have finished.\n");
    return 0;
}
