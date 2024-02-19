from pymongo import MongoClient
from bson.objectid import ObjectId  # Pour convertir la chaîne en ObjectId
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")

def test():
        # Connexion à MongoDB (assurez-vous que MongoDB est accessible à cette adresse)
        #client = MongoClient("mongodb://localhost:27017/")

        # Création ou sélection de la base de données
        #db = client["Hamza"]

        # Création ou sélection de la collection
        #collection = db["Infos"]

        # Insertion de données initiales dans la collection
        # data_initiale = {"nom": "sri-rame", "valeur": 15555}
        # resultat = collection.insert_one(data_initiale)
        #
        # print(resultat)

        # for document in collection.find():
        #     print(document)
        #     # Vérifiez si l'_id du document correspond à l'_id que vous voulez supprimer
        #     if str(document.get("_id")) == "65c4dc8f4e817c7d9c9fcac6":
        #         # Suppression du document
        #         collection.delete_one({"_id": ObjectId("65c4dc8f4e817c7d9c9fcac6")})
        #         print("Document supprimé")

        #print(f"Document inséré avec l'ID: {resultat.inserted_id}")

        import requests

        headers = {
            # Already added when you pass json=
            # 'Content-Type': 'application/json',
        }

        json_data = {
            'nom': 'exempleNom',
            'valeur': 12345,
        }

        response = requests.post('http://localhost:2000/byID', headers=headers, json=json_data)
        print(response.json())


def addjson():
    from pymongo import MongoClient
    import json

    file_path = 'pal.json'

    # Connexion à MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["Hamza"]
    collection = db["pal"]

    # Lire le fichier JSON
    with open(file_path, 'r') as file:
        file_data = json.load(file)


    if isinstance(file_data, list):
        collection.insert_many(file_data)
    else:
        collection.insert_one(file_data)

    print("Les données ont été insérées dans MongoDB.")

def get_by_id():
        # db_name = request.args.get('db')
        # collection_name = request.args.get('collection')
        doc_id = request.args.get('id')

        db = client['Hamza']
        collection = db['pal']

        # Convertir l'ID de String à ObjectId pour la recherche
        try:
            document = collection.find_one({'_id': ObjectId(doc_id)})
        except Exception as e:
            return jsonify({"message": "Invalid ID format", "error": str(e)}), 400

        if document:
            # ObjectId n'est pas sérialisable en JSON, supprimez-le ou convertissez-le en string
            document['_id'] = str(document['_id'])
            return jsonify(document)
        else:
            return jsonify({"message": "Document not found"}), 404




def test():
    import requests

    params = {
        'db': 'Hamza',
        'collection': 'pal',
        'id': '2',
    }

    response = requests.get('http://127.0.0.1:2000/api/GetById', params=params)
    print(response.json())

test()

#get_by_id()
