# Utiliser l'image OpenJDK officielle
FROM openjdk:17-jdk-slim
WORKDIR /app

COPY . .
RUN mvn clean package -DskipTests=true
# Copier le fichier JAR de votre application dans le conteneur
COPY target/demo-0.0.1-SNAPSHOT.jar /app/demo.jar

# Définir le point d'entrée pour exécuter le JAR
ENTRYPOINT ["java", "-jar", "/app/demo.jar"]