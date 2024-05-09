package com.demo;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.util.ArrayList;
import java.util.List;

@Document(collection = "joueurs")
public class Joueur {
    @Id
    private String id;
    private int level;
    private double experience;
    private List<String> monstres;

    public Joueur() {
        this.level = 1;  // Le joueur commence au niveau 1
        this.experience = 0;  // Pas d'expérience au début
        this.monstres = new ArrayList<>(10);  // 10 monstres par défaut
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }

    public double getExperience() {
        return experience;
    }

    public void setExperience(double experience) {
        this.experience = experience;
    }

    public List<String> getMonstres() {
        return monstres;
    }

    public void setMonstres(List<String> monstres) {
        this.monstres = monstres;
    }

}