import random

# 全局变量i
i = 0
monkey = []
box = []
banana = []
monbox = []
getit = []


def Monkey_goto(A):
    global i
    i = i + 1
    if A == -1:
        print("Monkey go to A")
        monkey[i] = -1
    elif A == 0:
        print("Monkey go to B")
        monkey[i] = 0
    elif A == 1:
        print("Monkey go to C")
        monkey[i] = 1
    else:
        print("parameter is wrong")


def move_box(A):
    global i
    i = i + 1
    if A == -1:
        print("monkey move box to A")
        monkey[i] = -1
        box[i] = -1
    elif A == 0:
        print("monkey move box to B")
        monkey[i] = 0
        box[i] = 0
    elif A == 1:
        print("monkey move box to C")
        monkey[i] = 1
        box[i] = 1
    else:
        print("parameter is wrong")


def climb_onto_box():
    global i
    i = i + 1
    monbox[i] = 1
    print("Monkey climb onto the box")


def climbdown():
    global i
    i = i + 1
    monbox[i] = 0
    print("Monkey climb down from the box")


def Monkey_get_banana():
    global i
    getit[i] = 1
    print("Monkey reach the banana")


def nextstep():
    global i
    m: int = 0
    j: int
    if i >= 150:
        print("%s  \n", "steplength reached 150,have problem ")
        return
    while getit[i] == 1:
        # getchar(); # / * to save screen for user, press any key to
        return
    j = i + 1
    if box[i] == monkey[i] and box[i] == banana[i]:
        if monbox[i] == 0:
            climb_onto_box()
            Monkey_get_banana()
            nextstep()
        else:
            Monkey_get_banana()
            nextstep()
    elif box[i] == monkey[i] and box[i] != banana[i]:
        if monbox[i] == 0:
            move_box(banana[i])
            nextstep()
        else:
            climbdown()
            nextstep()
    elif box[i] != monkey[i] and box[i] == banana[i]:
        Monkey_goto(box[i])
        nextstep()
    elif box[i] != monkey[i] and box[i] != banana[i]:
        Monkey_goto(box[i])
        nextstep()


if __name__ == '__main__':
    n: int = 0
    a: int = random.randint(-1, 1)
    b: int = random.randint(-1, 1)
    c: int = random.randint(-1, 1)
    d: int = 0
    e: int = 0
    print("初始位置：")
    print("monkey:", a)
    print("box:", b)
    print("banana:", c)
    print("monbox:", d)
    while n < 150:
        monkey.append(a)
        box.append(b)
        banana.append(c)
        monbox.append(d)
        getit.append(e)
        n = n + 1
    nextstep()
