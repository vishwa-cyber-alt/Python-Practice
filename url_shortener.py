import pyshorteners

def shorten_url(long_url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(long_url)

if __name__ == "__main__":
    url = input("Enter the long URL: ")
    short_url = shorten_url(url)
    print("Shortened URL:", short_url)
