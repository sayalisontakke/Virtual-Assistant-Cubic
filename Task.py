import datetime
from Speak import Say

def Time():
    time =datetime.datetime.now().strftime("%H:%m")
    Say(time)
    
def Date():
    time =datetime.datetime.date.today()
    Say(date)
    
def Day():
    day =datetime.datetime.now().strftime("%A")
    Say(day)
    
#Day()
    
def NonInputExecution(query):
    query = str(query)
    if "time" in query:
        Time()
        
    elif "date" in query:
        Date()
        
    elif "day" in query:
        Day()
        
        
    
#     2 Input
# eg. google search, wikipedia
def InputExecution(tag,query):
    if "wikipedia" in tag:
        name = str(query).replace("who is", "").replace("about", "").replace("what is", "").replace("wikipedia", "")
        import wikipedia
        result = wikipedia.summary(name)
        Say(result)
        
        
    elif "google" in tag:
        query = str(query).replace("google", "")
        query = query.replace("search", "")
        import pywhatkit
        pywhatkit.search(query)

