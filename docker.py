import docker

client = docker.from_env()


# Démarrer un conteneur MongoDB
conteneur = client.containers.run("mongo", detach=True, ports={'27017/tcp': 27017}, name="mon-mongo")

print(f"Conteneur démarré avec l'ID : {conteneur.id}")
