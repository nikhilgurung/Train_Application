import requests
class IRCTC:
    def __init__(self):
        user_input = input("""How would you like to proceed?
        1. Enter 1 to check live train status
        2. Enter 2 to check PNR
        3. Enter 3 to check train schedule
        """)
        if user_input == "1":
            print("Train Live status")
        elif user_input == "2":
            print("PNR")
        else:
            self.train_schedule()
    #To know the Train schedule
    def train_schedule(self):
        train_number = input("Enter the train number:")
        self.fetch_data(train_number)

    #To Fetch the Train Data
    '''Fill this data in the <> spaces
       1.You need to provide an API key
       2.Train number.
       3. Date in YYYYMMDD format'''
    def fetch_data(self,train_number):
        data = requests.get("http://indianrailapi.com/api/v2/livetrainstatus/apikey/<>/trainnumber/<>/date/<>/")

        data =data.json()
        print(data)

#You can create Object of our own
obj = IRCTC()
