import time,sys,os

RST = "\033[0m" # RESE

time.sleep(0.5)

def contrast_colour(colour):
    if colour == 0 or (16 <= colour <= 33) or (52 <= colour <= 69) or (88 <= colour <= 105) or \
            (124 <= colour <= 141) or (160 <= colour <= 177) or (196 <= colour <= 213) or \
            (232 <= colour <= 243):
        return 15
    else:
        return 0

def print_colour(colour):
    contrast = contrast_colour(colour)
    print(f'\033[48;5;{colour}m', end="")
    print(f'\033[38;5;{contrast}m{colour:3d}', end="")
    print('\033[0m ', end="")

def print_run(start, run):
    for i in range(start, start + run):
        sys.stdout.flush()
        print_colour(i)
        time.sleep(0.001)
    print("  ", end="")

def print_blocks(start, end, block_cols, block_rows, blocks_per_line):
    block_length = block_cols * block_rows

    for i in range(start, end + 1, block_length * blocks_per_line):
        print("\n", end="")
        for row in range(block_rows):
            for block in range(blocks_per_line):
                print_run(i + (block * block_length), block_cols)
            i += block_cols
            sys.stdout.flush()
            print("\n", end="")
            time.sleep(0.05)

def color_max():
    print_run(0, 16)
    print()
    print_blocks(16, 231, 6, 6, 3)
    print_blocks(232, 255, 12, 2, 1)

color_max()
time.sleep(0.5)

def colorin(selec):
    codigo = f"\n'\\33[38;5;{selec}m'"
    fond = f'\033[48;5;{selec}m'
    color = f'\033[38;5;0m'

    if selec == 0 or (selec > 15 and selec <= 33):
        print(codigo+"\n")
        print (f"{fond}Correcta selección"+RST)

    elif selec > 51 and selec <= 69:
        print(codigo+"\n")
        print (f"{fond}Correcta selección"+RST)

    elif selec > 87 and selec <= 105:
        print(codigo+"\n")
        print (f"{fond}Correcta selección"+RST)

    elif selec > 123 and selec <= 141:
        print(codigo+"\n")
        print (f"{fond}Correcta selección"+RST)

    elif selec > 159 and selec <= 177:
        print(codigo+"\n")
        print (f"{fond}Correcta selección"+RST)

    elif selec > 195 and selec <= 213:
        print(codigo+"\n")
        print (f"{fond}Correcta selección"+RST)

    elif selec > 231 and selec <= 243:
        print(codigo+"\n")
        print (f"{fond}Correcta selección"+RST)

    elif selec > 0:
        print(codigo+"\n")
        print (f"{fond}{color}Correcta selección"+RST)

while True:
    print("\ncomando >> !start\ncomando >> !exit")
    selec = input("\n\n}╍[digito]{❜> ")

    if selec.isdigit():
        selec = int(selec)
        if selec <= 255:
    
            colorin(selec)
        else:
            print("fuera del rango")
    
    else:
        if selec == "!start":
            os.system("clear")
            color_max()
        elif selec == "!exit":
            print("\n ∆•∆•∆ ADIOS ∆•∆•∆")
            exit()
        else:
            print("\nerror")

