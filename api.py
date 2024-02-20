from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")




default_db  = "Hamza"

default_collection = "pal"



#RETOURNE LES PAGES HTML
######################################
@app.route('/')
def home():
    return render_template('menu.html')


@app.route('/ajouter_pal')
def ajouter_pal():
    return render_template('ajouter_pal.html')

@app.route('/rechercher_par_id')
def rechercher_par_id():
    return render_template('rechercher_par_id.html')

@app.route('/rechercher_par_type')
def rechercher_par_type():
    return render_template('rechercher_par_type.html')


@app.route('/rechercher_par_name')
def rechercher_par_name():
    return render_template('rechercher_par_name.html')

@app.route('/get_skill_pal')
def get_skill_pal_html():
    return render_template('get_skill_pal.html')


@app.route('/add_skill_to_pal')
def add_skill_to_pal_html():
    return render_template('add_skill_to_pal.html')

@app.route('/modify_skill')
def modify_skill_html():
    return render_template('modify_skill.html')


@app.route('/get_types_pal')
def get_types_pal_html():
    return  render_template('get_types_pal.html')

@app.route('/add_types_to_pall')
def add_type_to_pall_html():
    return  render_template('add_type_to_pall.html')


@app.route('/remove_type_to_pall')
def remove_type_to_pall_html():
    return render_template('remove_type_to_pal.html')

@app.route('/get_pal_by_rarity')
def get_pal_by_rarity_html():
    return render_template('get_pal_by_rarity.html')

@app.route('/get_pal_by_price')
def get_pal_by_price_html():
    return render_template('get_pal_by_price.html')

#######################################














@app.route('/api/insert', methods=['POST'])
def insert_data():
    data = request.json
    db = client[data['db']]
    collection = db[data['collection']]

    # Génère un template de document avec des valeurs par défaut
    pal_template = {
        "_id": ObjectId(),  # Génère un ObjectId MongoDB aléatoire
        "asset": "default_asset",
        "aura": {
            "description": None,
            "name": None,
            "tech": None
        },
        "description": "Description par défaut",
        "drops": [],
        "genus": None,
        "id": None,  # L'ID sera défini après la conversion
        "image": None,
        "imageWiki": None,
        "key": "default_key",
        "maps": {
            "day": None,
            "night": None
        },
        "name": data.get('nom', 'Nom par défaut'),  # Utilise le nom fourni ou un nom par défaut
        "price": 0,
        "rarity": 1,
        "size": "M",
        "skills": [],
        "stats": {
            "attack": {"melee": 0, "ranged": 0},
            "defense": 0,
            "food": 1,
            "hp": 100,
            "speed": {"ride": 0, "run": 0, "walk": 0},
            "stamina": 100,
            "support": 0
        },
        "suitability": [],
        "types": ["default_type"],
        "wiki": None
    }

    # Convertit l'ID en entier et le définit dans le template
    try:
        pal_template['id'] = int(data['id'])
    except ValueError:
        return jsonify({"message": "L'ID doit être un nombre entier."}), 400

    # Insère le document dans la collection
    result = collection.insert_one(pal_template)
    if result.acknowledged:
        return jsonify({"message": "Document successfully added with _id: {}".format(pal_template["_id"])}), 200
    else:
        return jsonify({"message": "An error occurred"}), 500



@app.route('/api/GetAllIDs', methods = ['GET'])
def get_all_id():

    db_name = default_db
    collection_name = default_collection

    db = client[db_name]
    collection = db[collection_name]

    documents = collection.find()


    ids = [str(doc['id']) for doc in documents]
    print(ids)

    return jsonify(ids)


@app.route('/api/GetById', methods = ['GET'])
def get_by_id():


    db_name = default_db

    print(db_name)

    collection_name = default_collection

    doc_id = request.args.get('id')

    db = client[db_name]
    collection = db[collection_name]

    document = collection.find_one({'id': int(doc_id)})

    print(document)

    if document:
        document['_id'] = str(document['_id'])

        return jsonify(document)
    else:
        return jsonify({"message": "Document not found"}), 404



@app.route('/api/GetAllType', methods=['GET'])
def get_all_type():
    db_name = default_db
    collection_name = default_collection
    db = client[db_name]
    collection = db[collection_name]

    documents = collection.find({}, {
        "types": 1})  # Sélectionne tous les documents mais retourne uniquement le champ 'types'

    all_types_set = set()
    for doc in documents:
        for t in doc.get("types", []):  # Assurez-vous que 'types' est une liste
            all_types_set.add(t)

    all_types_list = list(all_types_set)

    return jsonify({"types": all_types_list})



@app.route('/api/GetByType', methods=['GET'])
def get_by_type():
    db_name = request.args.get('db', default_db)
    collection_name = request.args.get('collection', default_collection)
    doc_type = request.args.get('type')

    if not doc_type:
        return jsonify({"message": "Type parameter is required"}), 400

    db = client[db_name]
    collection = db[collection_name]

    documents = collection.find({"types": doc_type})

    results = [doc for doc in documents]

    for doc in results:
        doc['_id'] = str(doc['_id'])


    if results:
        return jsonify(results)
    else:
        return jsonify({"message": "Mon cousin ya pas de monstreeeu avec ce type "}), 404



#A FINIR FONCTION POUR LES NOMS ET FAIRE SON ALL NAME
@app.route('/api/GetByName', methods=['GET'])
def get_by_name():
    db_name = default_db
    collection_name = default_collection
    doc_type = request.args.get('name')

    if not doc_type:
        return jsonify({'message': 'Veuillez fournir un nom valide'}), 400

    db = client[db_name]
    collection = db[collection_name]

    documents = collection.find({'name': doc_type})

    results = [doc for doc in documents]

    for doc in results:
        doc['_id'] = str(doc['_id'])

    if results:
        return jsonify(results)
    else:
        return jsonify({"message": f"Aucun élément avec le nom '{doc_type}' trouvé"}), 404


@app.route('/api/GetAllName', methods=['GET'])
def get_all_name():

        print('test')
        db_name = default_db
        collection_name = default_collection

        db = client[db_name]
        collection = db[collection_name]

        documents = collection.find()

        ids = [doc['name'] for doc in documents]
        print(ids)
        return jsonify(ids)




from bson import ObjectId

@app.route('/api/GetSkillPal', methods =['GET'])
def get_skill_pal():
    db_name = default_db
    collection_name = default_collection
    pal_name = request.args.get('name')

    if not pal_name:
        return jsonify({'message': 'Veuillez fournir un nom de Pal valide'}), 400

    db = client[db_name]
    collection = db[collection_name]

    # Recherche du Pal par son nom
    document = collection.find_one({'name': pal_name})

    if document:
        # Récupération de la liste des compétences du Pal trouvé
        skills = document.get('skills', [])

        # Ajout d'un identifiant unique pour chaque compétence
        for index, skill in enumerate(skills):
            skill['_id'] = str(index + 1)

        return jsonify(skills)
    else:
        return jsonify({"message": f"Aucun Pal avec le nom '{pal_name}' trouvé"}), 404




@app.route('/api/AddSkillToPal', methods=['POST'])
def add_skill_to_pal():
    data = request.json

    required_fields = ['pal_name', 'skill_name', 'skill_level', 'skill_type', 'skill_cooldown', 'skill_power', 'skill_description']
    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"Le champ '{field}' est requis"}), 400

    pal_name = data['pal_name']
    skill_name = data['skill_name']
    skill_level = data['skill_level']
    skill_type = data['skill_type']
    skill_cooldown = data['skill_cooldown']
    skill_power = data['skill_power']
    skill_description = data['skill_description']

    db = client[default_db]
    collection = db[default_collection]
    pal = collection.find_one({'name': pal_name})

    if not pal:
        return jsonify({"message": f"Aucun Pal avec le nom '{pal_name}' trouvé"}), 404

    new_skill = {
        'name': skill_name,
        'level': skill_level,
        'type': skill_type,
        'cooldown': skill_cooldown,
        'power': skill_power,
        'description': skill_description
    }

    pal_skills = pal.get('skills', [])
    pal_skills.append(new_skill)

    # Mettre à jour le document du pal dans la base de données
    result = collection.update_one({'_id': pal['_id']}, {'$set': {'skills': pal_skills}})

    if result.modified_count > 0:
        return jsonify({"message": f"Compétence '{skill_name}' ajoutée avec succès au Pal '{pal_name}'"}), 200
    else:
        return jsonify({"message": "Une erreur s'est produite lors de l'ajout de la compétence au Pal"}), 500






@app.route('/api/ModifySkill', methods=['POST'])
def modify_skill():
    pal_name = request.json.get('name')
    skill_name = request.json.get('skill_name')
    attribute_name = request.json.get('attribute_name')
    new_value = request.json.get('new_value')
    print(pal_name)
    print(skill_name)
    print(attribute_name)
    print(new_value)
    if not all([pal_name, skill_name, attribute_name, new_value]):
        return jsonify({'message': 'Veuillez fournir toutes les informations nécessaires'}), 400
    db = client[default_db]
    collection = db[default_collection]

    # Recherche du Pal par son nom
    document = collection.find_one({'name': pal_name})

    if document:
        skills = document.get('skills', [])
        for skill in skills:
            if skill['name'] == skill_name:
                print(skill)
                if attribute_name in skill:
                    skill[attribute_name] = new_value
                    # Mise à jour du document dans la base de données
                    collection.update_one({'name': pal_name}, {'$set': {'skills': skills}})
                    return jsonify({'message': 'Skill modifié avec succès'})
                else:
                    return jsonify({'message': f"L'attribut '{attribute_name}' n'existe pas dans ce skill"}), 400

        return jsonify({'message': f"Skill avec le nom '{skill_name}' non trouvé pour le Pal '{pal_name}'"}), 404
    else:
        return jsonify({"message": f"Aucun Pal avec le nom '{pal_name}' trouvé"}), 404




@app.route('/api/GetTypesPall', methods=['GET'])
def get_types_pall():
    db_name = default_db
    collection_name = default_collection
    pal_name = request.args.get('name')

    if not pal_name:
        return jsonify({'message': 'Veuillez fournir un nom de Pal valide'}), 400

    db = client[db_name]
    collection = db[collection_name]

    # Recherche du Pal par son nom
    document = collection.find_one({'name': pal_name})

    if document:
        # Récupération des types du Pal trouvé
        types = document.get('types', [])

        # Pas besoin d'ajouter un identifiant unique pour chaque type, donc on peut directement retourner la liste des types
        return jsonify({"types": types})
    else:
        return jsonify({"message": f"Aucun Pal avec le nom '{pal_name}' trouvé"}), 404



@app.route('/api/AddTypeToPal', methods=['POST'])
def add_type_to_pal():
    # Récupération des données JSON envoyées avec la requête
    data = request.json
    pal_name = data.get('name')
    new_type = data.get('type')

    if not pal_name or not new_type:
        return jsonify({'message': 'Le nom du Pal et le type à ajouter sont requis.'}), 400

    # Connexion à la base de données et à la collection spécifiques
    db = client[default_db]
    collection = db[default_collection]

    # Recherche du Pal par son nom et ajout du nouveau type
    result = collection.find_one_and_update(
        {'name': pal_name},
        {'$addToSet': {'types': new_type}},  # Utilisation de $addToSet pour éviter les doublons
        return_document=True
    )

    if result:
        return jsonify({'message': f'Le type "{new_type}" a été ajouté avec succès au Pal "{pal_name}".'})
    else:
        return jsonify({'message': f'Le Pal nommé "{pal_name}" n\'a pas été trouvé.'}), 404


@app.route('/api/RemoveTypeFromPal', methods=['POST'])
def remove_type_from_pal():
    data = request.json
    pal_name = data.get('name')
    pal_type = data.get('type')

    db = client[default_db]
    collection = db[default_collection]
    if not pal_name or not pal_type:
        return jsonify({'message': 'Le nom du Pal et le type à supprimer sont requis.'}), 400

    result = collection.find_one_and_update(
        {'name': pal_name},
        {'$pull': {'types': pal_type}},  # Utilise $pull pour supprimer le type
        return_document=True
    )

    if result:
        return jsonify({'message': f'Le type "{pal_type}" a été supprimé avec succès du Pal "{pal_name}".'})
    else:
        return jsonify({'message': f'Le Pal nommé "{pal_name}" n\'a pas été trouvé ou le type "{pal_type}" n\'existe pas.'}), 404



@app.route('/api/GetPalsByRarity', methods=['GET'])
def get_pals_by_rarity():
    try:
        rarity = int(request.args.get('rarity'))
        db = client[default_db]
        collection = db[default_collection]

        pals = collection.find({"rarity": rarity})

        # Préparation des données pour la réponse
        pals_list = [{"name": pal["name"], "rarity": pal["rarity"]} for pal in pals]

        return jsonify(pals_list)
    except Exception as e:
        print(e)
        return jsonify({"message": str(e)}), 500



@app.route('/api/GetPalsByPrice', methods=['GET'])
def get_pals_by_price():
    try:
        min_price = int(request.args.get('min', 0))
        max_price = int(request.args.get('max', 1000000))  # Utilisez une valeur maximale par défaut élevée

        db = client[default_db]
        collection = db[default_collection]

        pals = collection.find({"price": {"$gte": min_price, "$lte": max_price}}).sort("price", 1)

        pals_list = [{"name": pal["name"], "price": pal["price"]} for pal in pals]

        return jsonify(pals_list)
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route('/api/GetPriceRange', methods=['GET'])
def get_price_range():
    db = client[default_db]
    collection = db[default_collection]

    # Trouver le prix minimum et maximum parmi tous les Pals pour eviter que l'utilisateur ne met un prix entre 7 et 10 alors que y'en a pas !
    min_price = collection.find_one(sort=[("price", 1)], projection={"price": 1, "_id": 0})["price"]
    max_price = collection.find_one(sort=[("price", -1)], projection={"price": 1, "_id": 0})["price"]

    return jsonify({"minPrice": min_price, "maxPrice": max_price})


if __name__ == '__main__':
    app.run(debug=True , port= 2000)
