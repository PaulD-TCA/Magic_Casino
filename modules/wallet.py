import pymongo


class CasinoWallet:
  def __init__(self):
    self.client = pymongo.MongoClient("mongodb+srv://PaulCasino:PaulCasino@cluster0.vicit.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    self.db = self.client.test
  
  def create_wallet(self): 
    self.db.create_collection("my_wallet")

  def wallet_content(self): 
    self.db.create_collection("my_wallet")

  def update_money(self): 
    self.db.create_collection("my_wallet")

  def delete_wallet(self): 
    self.db.create_collection("my_wallet")