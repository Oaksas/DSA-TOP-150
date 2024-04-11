def RomanToInt(roman):
    mapp = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = 0
    for i in range(len(roman)):
        if i < len(roman) - 1 and mapp[roman[i]] < mapp[roman[i+1]]:
            result -= mapp[roman[i]]
        else:
            result += mapp[roman[i]]

    return result


# Convert "LXXXV" to an integer
print(RomanToInt("MCMXCI"))  # Output should be 85
