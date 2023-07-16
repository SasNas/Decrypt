ry = 1
while ry == 1:
    ans = input(' Encrypt (message => code) or decrypt (code => message)? Choose "e" or "d"    ')
    q1 = 0

    if ans == "d":
        result2 = []
        code = input("Input your useless numbers   ")
        code_list = list(code)
        code_len = len(code_list)
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
            else:
                q1 = 1
            
        if q1 == 0:
            final_result2 = "".join(result2)
            print ('Your message is "', final_result2, '"')
            ry = 0
        else:
            print("I have no idea where did you get those numbers")
        

    elif ans == "e":
        message = input("Input your message. Small English letters, dot, comma, space only  ")
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
            else:
                q1 = 1
            
        if q1 == 0:
            final_result = "".join(result)
            print ("Your final code is ", final_result)
            ry = 0
        else:
            print("Use small English letters, dot, comma, space only")
    else:
        print('Answer "Z" or "R", please')
print("Thanks for using this thing")
print('')
print("                              Alex")
input("Press Enter to exit")
