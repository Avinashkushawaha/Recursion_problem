def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])
    
print(f"The reverse of 'hello' is '{reverse_string('hello')}'")
