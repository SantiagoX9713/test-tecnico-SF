def find_missing_letter(letters):
    missing_letter = ''
    s = len(letters) - 1
    for i in range(0,s):
        if (ord(letters[i+1]) - ord(letters[i]) > 1):
            missing_letter = chr(ord(letters[i]) + 1)
    return missing_letter

#No conocía los métodos ord() y chr() pero investigué y con ellos pude solucionarlo