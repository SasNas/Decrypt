ry = 1
while ry == 1:
    ans = input(' Encrypt (message => code) or decrypt (code => message)? Choose "E" or "D"    ')
    q1 = 0

    if ans == "d" or ans == "D":
        result2 = []
        code = input("Input your useless numbers   ")
        code_list = list(code)
        code_len = len(code_list)
        if code_len % 2 == 1:
            print("How did you get odd number of digits?")
        else:
            for popa in range (0, code_len, 2):
                n1 = code_list[popa]
                n2 = code_list[popa + 1]
                n3 = n1 + n2
            
                if n3 == "01":
                    result2.append(" ")
                elif n3 == "02":
                    result2.append(",")
                elif n3 == "03":
                    result2.append(".")
                elif n3 == "04":
                    result2.append("q")
                elif n3 == "05":
                    result2.append("w")
                elif n3 == "06":
                    result2.append("e")
                elif n3 == "07":
                    result2.append("r")
                elif n3 == "08":
                    result2.append("t")
                elif n3 == "09":
                    result2.append("y")
                elif n3 == "10":
                    result2.append("u")
                elif n3 == "11":
                    result2.append("i")
                elif n3 == "12":
                    result2.append("o")
                elif n3 == "13":
                    result2.append("p")
                elif n3 == "14":
                    result2.append("a")
                elif n3 == "15":
                    result2.append("s")
                elif n3 == "16":
                    result2.append("d")
                elif n3 == "17":
                    result2.append("f")
                elif n3 == "18":
                    result2.append("g")
                elif n3 == "19":
                    result2.append("h")
                elif n3 == "20":
                    result2.append("j")
                elif n3 == "21":
                    result2.append("k")
                elif n3 == "22":
                    result2.append("l")
                elif n3 == "23":
                    result2.append("z")
                elif n3 == "24":
                    result2.append("x")
                elif n3 == "25":
                    result2.append("c")
                elif n3 == "26":
                    result2.append("v")
                elif n3 == "27":
                    result2.append("b")
                elif n3 == "28":
                    result2.append("n")
                elif n3 == "29":
                    result2.append("m")
                elif n3 == "30":
                    result2.append("?")
                elif n3 == "31":
                    result2.append("!")
                elif n3 == "32":
                    result2.append("Q")
                elif n3 == "33":
                    result2.append("W")
                elif n3 == "34":
                    result2.append("E")
                elif n3 == "35":
                    result2.append("R")
                elif n3 == "36":
                    result2.append("T")
                elif n3 == "37":
                    result2.append("Y")
                elif n3 == "38":
                    result2.append("U")
                elif n3 == "39":
                    result2.append("I")
                elif n3 == "40":
                    result2.append("O")
                elif n3 == "41":
                    result2.append("P")
                elif n3 == "42":
                    result2.append("A")
                elif n3 == "43":
                    result2.append("S")
                elif n3 == "44":
                    result2.append("D")
                elif n3 == "45":
                    result2.append("F")
                elif n3 == "46":
                    result2.append("G")
                elif n3 == "47":
                    result2.append("H")
                elif n3 == "48":
                    result2.append("J")
                elif n3 == "49":
                    result2.append("K")
                elif n3 == "50":
                    result2.append("L")
                elif n3 == "51":
                    result2.append("Z")
                elif n3 == "52":
                    result2.append("X")
                elif n3 == "53":
                    result2.append("C")
                elif n3 == "54":
                    result2.append("V")
                elif n3 == "55":
                    result2.append("B")
                elif n3 == "56":
                    result2.append("N")
                elif n3 == "57":
                    result2.append("M")
                else:
                    q1 = 1
            
            if q1 == 0:
                final_result2 = "".join(result2)
                print ('Your message is "', final_result2, '"')
                somt = input (" Start one more time? (No / anything else)")
                if somt == "no" or somt == "No" or somt == "No":
                    ry = 0
                else:
                    print("OK")
                
            else:
                print("I have no idea where did you get those numbers")
        

    elif ans == "e" or ans == "E":
        print("                                                             ")
        message = input("Input your message. English letters, dot, comma, space only |  ")
        print("                                                             ")
        ml = list(message)
        result = []
        nu = len(ml)
        for hui in range(nu):
            if ml[hui]== " ":
                result.append("01")
            elif ml[hui]== ",":
                result.append("02")
            elif ml[hui]== ".":
                result.append("03")
            elif ml[hui]== "q":
                result.append("04")
            elif ml[hui]== "w":
                result.append("05")
            elif ml[hui]== "e":
                result.append("06")
            elif ml[hui]== "r":
                result.append("07")
            elif ml[hui]== "t":
                result.append("08")
            elif ml[hui]== "y":
                result.append("09")
            elif ml[hui]== "u":
                result.append("10")
            elif ml[hui]== "i":
                result.append("11")
            elif ml[hui]== "o":
                result.append("12")
            elif ml[hui]== "p":
                result.append("13")
            elif ml[hui]== "a":
                result.append("14")
            elif ml[hui]== "s":
                result.append("15")
            elif ml[hui]== "d":
                result.append("16")
            elif ml[hui]== "f":
                result.append("17")
            elif ml[hui]== "g":
                result.append("18")
            elif ml[hui]== "h":
                result.append("19")
            elif ml[hui]== "j":
                result.append("20")
            elif ml[hui]== "k":
                result.append("21")
            elif ml[hui]== "l":
                result.append("22")
            elif ml[hui]== "z":
                result.append("23")
            elif ml[hui]== "x":
                result.append("24")
            elif ml[hui]== "c":
                result.append("25")
            elif ml[hui]== "v":
                result.append("26")
            elif ml[hui]== "b":
                result.append("27")
            elif ml[hui]== "n":
                result.append("28")
            elif ml[hui]== "m":
                result.append("29")
            elif ml[hui]== "?":
                result.append("30")
            elif ml[hui]== "!":
                result.append("31")
            elif ml[hui]== "Q":
                result.append("32")
            elif ml[hui]== "W":
                result.append("33")
            elif ml[hui]== "E":
                result.append("34")
            elif ml[hui]== "R":
                result.append("35")
            elif ml[hui]== "T":
                result.append("36")
            elif ml[hui]== "Y":
                result.append("37")
            elif ml[hui]== "U":
                result.append("38")
            elif ml[hui]== "I":
                result.append("39")
            elif ml[hui]== "O":
                result.append("40")
            elif ml[hui]== "P":
                result.append("41")
            elif ml[hui]== "A":
                result.append("42")
            elif ml[hui]== "S":
                result.append("43")
            elif ml[hui]== "D":
                result.append("44")
            elif ml[hui]== "F":
                result.append("45")
            elif ml[hui]== "G":
                result.append("46")
            elif ml[hui]== "H":
                result.append("47")
            elif ml[hui]== "J":
                result.append("48")
            elif ml[hui]== "K":
                result.append("49")
            elif ml[hui]== "L":
                result.append("50")
            elif ml[hui]== "Z":
                result.append("51")
            elif ml[hui]== "X":
                result.append("52")
            elif ml[hui]== "C":
                result.append("53")
            elif ml[hui]== "V":
                result.append("54")
            elif ml[hui]== "B":
                result.append("55")
            elif ml[hui]== "N":
                result.append("56")
            elif ml[hui]== "M":
                result.append("57")
            else:
                q1 = 1
            
        if q1 == 0:
            final_result = "".join(result)
            print ("Your final code is ", final_result)
            somt2 = input (" Start one more time? (No / anything else)")
            if somt2 == "no" or somt2 == "No" or somt2 == "No":
                ry = 0
            else:
                print("OK")
        else:
            print("Use English letters, dot, comma, space only")
    else:
        print('Answer "e" or "d", please')
print("Thanks for using this thing")
print('')
print("                              Alex")
input("Press Enter to exit")
