# str[start:stop:step]

trial = "reversal"
new_trial = trial[::-1]
print(new_trial)


# Recursion method

def string_reversal(str):
    if len(str) == 0:
        return str
    else:
        return string_reversal(str[1:]) + str[0]


str = "reversal"
reverse = string_reversal(str)
print(reverse)
