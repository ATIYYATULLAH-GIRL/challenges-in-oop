class Roman:
    def conversion(self, number):
        arabic_numeral= [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_numeral= ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_new_num=""
        for i in range(len(arabic_numeral)):
            while number>=arabic_numeral[i]:
                number-=arabic_numeral[i]
                roman_new_num+=roman_numeral[i]
        return roman_new_num
number=int(input("Enter an integer: "))
print(Roman().conversion(number))