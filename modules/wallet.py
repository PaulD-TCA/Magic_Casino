import pymongo


class CasinoWallet:
  def __init__(self):
    self.client = pymongo.MongoClient("mongodb+srv://PaulMagicMSecond:PaulMagicMSecond@cluster0.y8osu.mongodb.net/?retryWrites=true&w=majority")
    self.db = self.client.test
  
  def create_wallet(self):
    #Get a list with collections names
    collections = self.db.list_collection_names()
    #return True or False if the collection exist
    any_collection = "my_wallet" in collections
    if any_collection == True:
      print("The database already exists")
    else:
      self.db.create_collection("my_wallet")
      self.db.my_wallet.insert_one({'_id': 1, 'money': '0'})
    
  def read_wallet(self): 
    print(self.db.my_wallet.find_one({'_id': 1}))
    results = self.db.my_wallet.find()
    print(results)
    for result in results:
        print(result)
      

  def update_money(self): 
    self.db.my_wallet.update_one({'_id': 1}, {"$set": {'money': "100"}})

  def delete_wallet(self): 
    self.db.create_collection("my_wallet")