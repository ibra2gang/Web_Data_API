package com.demo;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface JoueurRepository extends MongoRepository<Joueur, String> {
}