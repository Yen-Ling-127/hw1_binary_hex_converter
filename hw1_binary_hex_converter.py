while True:
    input_str = input("請輸入一個介於0~255之間的數字，或輸入exit退出：")
    if input_str == "exit":
        print("程式已結束。")
        break
    
    try:
        int(input_str)
    except:
        print("錯誤：請輸入一個有效的數字。")
        continue
        
    num = int(input_str)
    if not 0 <= num <= 255:
        print("錯誤：數字必須介於0到255之間。")
        continue

    binary = ""
    num_for_binary = num  
    while num_for_binary > 0:
        binary = str(num_for_binary % 2) + binary
        num_for_binary = num_for_binary // 2

    hexadecimal = ""
    num_for_hexadecimal = num  
    hex_chars = "0123456789ABCDEF"
    while num_for_hexadecimal > 0:
        hexadecimal = hex_chars[num_for_hexadecimal % 16] + hexadecimal
        num_for_hexadecimal = num_for_hexadecimal // 16

    if num == 0:
        binary = "0"
        hexadecimal = "0"
    
    print(f"10進位：{num}")
    print(f"2進位：{binary}")
    print(f"16進位：{hexadecimal}")
