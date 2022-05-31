from flask import Flask, render_template, session, request

import pymongo

from modules import roulette, wallet

app = Flask('app', template_folder='templates')
app.secret_key = "mot_de_passe"

#client = pymongo.MongoClient("mongodb+srv://PaulMagicMakers:PaulMagicMakers@cluster0.k1flc.mongodb.net/?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb+srv://PaulMagicMSecond:PaulMagicMSecond@cluster0.y8osu.mongodb.net/?retryWrites=true&w=majority")


db = client.test

@app.route('/')
def index_page():
  session['util']= "toto"
  print(session["util"])


  return render_template('index.html')


@app.route('/roulette')
def roulette_page():

  db = client.test
  print(db.list_collection_names())
#  db.create_collection("collection_name")
  print(db.list_collection_names())
  
  resultat_afficher = roulette.CasinoRoulette()
  print("le tirage est " ,resultat_afficher.tirage())
  print(session["util"])
  return render_template('roulette_page.html', valeur=resultat_afficher.tirage())

@app.route('/wallet', methods=['GET', 'POST'])
def wallet_route():
  if request.method == 'POST':
 #   print(request.form.get('create'))
  #  print(request.form.get('read'))
    if request.form.get('create') == "Créer une collection":
      print('in the create')
      wallet.CasinoWallet().create_wallet()

    elif request.form.get('read') == "Lire la collection":
      results = wallet.CasinoWallet().read_wallet()
      print("on a lu")
  #  create = request.form.get('create')
  #  print(create)
    #wallet.CasinoWallet().create_wallet()

    elif request.form.get('update') == "Mettre à jour":
      wallet.CasinoWallet().update_money()
      print("on a mis à jour")

    
    
    return render_template('wallet_page.html')

#  wallet.CasinoWallet().create_wallet()
 # print(db.list_collection_names())
  return render_template('wallet_page.html')


app.run(host='0.0.0.0', port=8080)