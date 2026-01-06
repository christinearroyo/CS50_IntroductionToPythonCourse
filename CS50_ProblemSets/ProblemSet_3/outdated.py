def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    while True:
        try:
            date_input = input("Date: ").strip()
            
            if "/" in date_input:
                parts = date_input.split("/")
                if len(parts) != 3:
                    continue
                
                month, day, year = parts
                
                try:
                    month = int(month)
                    day = int(day)
                    year = int(year)
                except ValueError:
                    continue
                
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
            
            elif " " in date_input and "," in date_input:
                parts = date_input.split()
                if len(parts) != 3:
                    continue
                
                month_str, day_str, year_str = parts
                
                day_str = day_str.rstrip(",")
                
                if month_str in months:
                    month = months.index(month_str) + 1 
                else:
                    continue
                
                try:
                    day = int(day_str)
                    year = int(year_str)
                except ValueError:
                    continue
                
                if 1 <= day <= 31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
                
        except (ValueError, IndexError):
            pass

if __name__ == "__main__":
    main()