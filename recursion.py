counter = 0


def building_options(n, lst=[]):
    global counter
    if n == 0:
        counter += 1
        print(counter, ' + '.join(lst))
    elif n == 1:
        counter += 1
        print(counter, ' + '.join(lst + ['low']))
    else:
        building_options(n - 1, lst + ['low'])
        building_options(n - 2, lst + ['high'])


if __name__ == '__main__':
    building_options(5)
