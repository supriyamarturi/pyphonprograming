def switch_demo(argument):
    switcher = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten"
    }
    print switcher.get(argument, "Invalid Input")
n=int(raw_input())
switch_demo(n)
