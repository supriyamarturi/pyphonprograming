def switch_demo(argument):
    switcher = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
    }
    print switcher.get(argument, "Invalid Input")
m=int(raw_input())
switch_demo(m)
