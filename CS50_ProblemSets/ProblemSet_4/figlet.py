import sys
import random
from pyfiglet import Figlet

def main():
    if len(sys.argv) not in [1, 3]:
        print("Invalid usage")
        sys.exit(1)
    
    figlet = Figlet()
    
    available_fonts = figlet.getFonts()
    
    if len(sys.argv) == 1:
        font = random.choice(available_fonts)
    else:
        option = sys.argv[1]
        font_name = sys.argv[2]
        
        if option not in ["-f", "--font"]:
            print("Invalid usage")
            sys.exit(1)
        
        if font_name not in available_fonts:
            print(f"Invalid font: {font_name}")
            sys.exit(1)
        
        font = font_name
    
    figlet.setFont(font=font)
    
    text = input("Input: ")
    
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()