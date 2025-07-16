#Importing requests library 
import requests

class GetRequester:

    #When calling this class we are saving the URL that gets passed in
    def __init__(self, url):
        self.url = url
    #Calling the API using Get and returning the data in  bytes
    def get_response_body(self):
            response = requests.get(self.url)
            return response.content 
    # Calling the API using get and returning the data in json format 
    def load_json(self):
            response = requests.get(self.url)
            return response.json()

#This allows us to run via the terminal by typing in "python lib/GetRequester.py"        
if __name__ == "__main__":
    url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
    #Calling our class with the URL from above 
    requester = GetRequester(url)
    #Gets and prints the raw response 
    print("RAW RESPONSE:")
    print(requester.get_response_body())
    #Gets and prints the response in JSON format 
    print("\nJSON DATA:")
    print(requester.load_json())

