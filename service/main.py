from time import localtime, asctime, sleep


if __name__ == '__main__':
    while True:
        sleep(2)
        print(asctime(localtime()).encode('utf8'))
