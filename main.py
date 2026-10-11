FULL_CHAR = "█"

print("".join([f"\033[0;97m{FULL_CHAR}\033[0m" for i in range(9999)]))