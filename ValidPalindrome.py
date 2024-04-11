def palindrome(str):
    if len(str) == 0:
        return False
    start = 0
    end = len(str) - 1

    while start <= end:
        if str[start] != str[end]:
            return f"{str} Is not a Palindrom"
        start += 1
        end -= 1
    return f"{str} Is Palindrom"


print(palindrome("1000021"))
