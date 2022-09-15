from datetime import datetime
from fileinput import filename
import json
from html2image import Html2Image

def sample_responses(input_text):
    filename = input_text+".png"
    # filename = json.dumps(sample_responses(input_text))
    user_message = str(input_text).lower()

    def download(link, filename):


        try:
            print("\n\nDownloading.....{}\n\n".format(filename))
            hti = Html2Image()
            print(link)
            print("\n\ncopy paste this link in browser if not downloaded\n\n")
            hti.screenshot(url=link, save_as=filename)
            # context = {'img': image}

            print("{} downloaded successfully.....\n".format(filename))
        except OSError:
            print("\nUnfortunately failed to generate file. \nNot supported for your OS. \n")
            print(link)
            print("Copy paste this link in browser if not downloaded\n")


    if user_message.startswith('e1922'):
        # enum = input_text
        link = "http://result.bteupexam.in/Odd_Semester/main/result.aspx?Roll_no="+input_text
        filename = input_text+".png"
        download(link, filename)
        return filename
        
    else:
        # choice = 0k
        print("bye bye...:D")
        

    
    if user_message in ("hi, hlo, kem cho, hi?"):
        return "Hey HOw's it going?"

    if user_message in ("who are you", "who are you?", "kon ho"):
        return "I'm a bot which can download your result and currently in under development"

    if user_message in ("time now", "time?", "time"):
       now = datetime.now()
       date_time = now.strftime("%d/%m/%y, %H:%M:%S")

       return str(date_time)

    return "type /send to download your result"
