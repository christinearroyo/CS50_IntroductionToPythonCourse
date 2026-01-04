def main():
    grocery_list = {}
    
    try:
        while True:
            try:
                item = input().strip().upper()
                
                if item in grocery_list:
                    grocery_list[item] += 1
                else:
                    grocery_list[item] = 1
                    
            except EOFError:
                break
                
    except KeyboardInterrupt:
        pass
    
    sorted_items = sorted(grocery_list.items())
    
    for item, count in sorted_items:
        print(f"{count} {item}")

if __name__ == "__main__":
    main()