import os

from fastapi import FastAPI, HTTPException, Header
from pymongo import MongoClient
from pydantic import BaseModel
import hashlib
from datetime import datetime, timedelta
# Importation d'Uvicorn
import uvicorn
from fastapi import Depends
from fastapi.responses import JSONResponse

app = FastAPI()

#MONGO_URI = "mongodb://Hamza:27017/"
#MONGO_URI = "mongodb://172.23.0.2:27017/"
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
#MONGO_URI = "mongodb://localhost:27017/"

client = MongoClient(MONGO_URI)
db = client.Hamza
users_collection = db.infos

class UserLogin(BaseModel):
    user: str
    password: str

def generate_token(username: str):
    token = hashlib.sha256(f"{username}{datetime.utcnow()}".encode()).hexdigest()

    return token

@app.post("/login")
async def login(user_login: UserLogin):
    user = users_collection.find_one({"user": user_login.user, "password": user_login.password})
    print(user_login.user, user_login.password)
    print(user)
    if user:
        token = generate_token(user_login.user)
        expiration_time = datetime.utcnow() + timedelta(hours=2) #UTC mtn c l'heure en france - 1 donc je rajoute 2


        users_collection.update_one(
            {"user": user_login.user},
            {"$set": {"token": token, "date_expi": expiration_time}}
        )

        return f"Bienvenue {user_login.user} , votre session expire le {expiration_time}" \
               f"\nVoici votre token d'authentification -> {token}"
    else:
        raise HTTPException(status_code=400, detail="Invalid username or password")


from bson import ObjectId

def objectid_to_str(item):
    if isinstance(item, dict):
        for key, value in item.items():
            if isinstance(value, ObjectId):
                item[key] = str(value)
            elif isinstance(value, dict):
                objectid_to_str(value)
    return item

async def verify_token(token: str):
    user_info = users_collection.find_one({"token": token})
    print("Date d'expiration du token:", user_info["date_expi"])
    print("Heure actuelle (UTC):",datetime.utcnow() + timedelta(hours=1))

    if user_info is None:
        raise HTTPException(status_code=404, detail="Token not found")

    actuelle_h = datetime.utcnow() + timedelta(hours=1)

    if "date_expi" in user_info and user_info["date_expi"] < actuelle_h:
        raise HTTPException(status_code=401, detail="Token expired")

    return user_info


async def extract_token(Authorization: str = Header(None)):
    if Authorization:
        token_type, token = Authorization.split()
        if token_type.lower() == "bearer":
            return token
    raise HTTPException(status_code=400, detail="Token not provided")



@app.get("/check_token")
async def protected_resource(token: str = Depends(extract_token)):
    user_info = await verify_token(token)
    user_info = objectid_to_str(user_info)
    return {"message": "Ton token est valide brozeeeer"}



@app.post("/create")
async def create_user(user_data: UserLogin):
    # Vérifie si l'utilisateur existe déjà dans la base de données
    existing_user = users_collection.find_one({"user": user_data.user})
    if existing_user:
        return JSONResponse(content={"message": "Utilisateur déjà existant."}, status_code=400)

    # Si l'utilisateur n'existe pas, l'ajouter à la base de données

    new_user_data = {
        "user": user_data.user,
        "password": user_data.password,
        "token": "",
        "date_expi": None
    }
    print(new_user_data)
    users_collection.insert_one(new_user_data)
    print(users_collection.find)

    # Retourne les données du compte créé
    return JSONResponse(content={"message": "Compte créé avec succès."}, status_code=200)



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
