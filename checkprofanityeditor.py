import urllib.request


def read_text():
    quotes = open("C:\Python34\Programs py\quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):

    connection= urllib.request.urlopen("http://www.wdyl.com/profanity?q="+ urllib.parse.quote(text_to_check))
    output = connection.read()
    print(output)
    connection.close()

    if "true" in output:
        print ("Profanity Alert!")
    elif "false" in output:
        print("No curse words")
    else:
        print("could not scan")
 

read_text()
