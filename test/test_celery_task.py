
from test.test_celery import add

for i in range(3):
    for j in range(3):
        kk = add.delay(i, j)
        kk.ready()
        print(kk.get())