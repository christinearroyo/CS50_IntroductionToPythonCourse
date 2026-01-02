def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            
            x, y = fraction.split('/')
            
            numerator = int(x)
            denominator = int(y)
            
            if denominator == 0:
                continue
            
            if numerator > denominator:
                continue
            
            percentage = (numerator / denominator) * 100
            
            if percentage <= 1:
                print("E")
                break
            elif percentage >= 99:
                print("F")
                break
            else:
                print(f"{round(percentage)}%")
                break
                
        except ValueError:
            continue
        except ZeroDivisionError:
            continue

if __name__ == "__main__":
    main()