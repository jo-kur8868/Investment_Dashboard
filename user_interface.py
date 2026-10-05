from fetcher import Fetcher

def main():
    print(" Investment Dashboard ")

    # Prompting the user for a company ticker
    print(" Which company would you like to analyze? (Enter the ticker) ")
    Fetcher.set_ticker(input("- "))

if __name__ == "__main__":
    main()