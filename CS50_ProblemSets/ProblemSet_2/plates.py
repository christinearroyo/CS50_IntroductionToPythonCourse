plate = input("Plate: ")

if not (2 <= len(plate) <= 6):
    print("Invalid")
else:
    if not plate.isalnum():
        print("Invalid")
    else:
        if not (plate[0].isalpha() and plate[1].isalpha()):
            print("Invalid")
        else:
            digit_started = False
            valid = True
            
            for i, ch in enumerate(plate):
                if ch.isdigit():
                    if not digit_started:
                        digit_started = True
                        if ch == '0':
                            valid = False
                            break
                elif ch.isalpha():
                    if digit_started:
                        valid = False
                        break
            
            if valid:
                print("Valid")
            else:
                print("Invalid")