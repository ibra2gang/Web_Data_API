package com.demo;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class JoueurService {
    @Autowired
    private final JoueurRepository joueurRepository;

    public JoueurService(JoueurRepository joueurRepository) {
        this.joueurRepository = joueurRepository;
    }

    public List<Joueur> getAllJoueurs() {
        return joueurRepository.findAll();
    }

    public Joueur createJoueur(Joueur joueur) {
        if (joueurRepository.findById(joueur.getId()).isPresent()) {
            throw new IllegalArgumentException("Un joueur avec cet identifiant existe déjà");
        }
        return joueurRepository.save(joueur);
    }

    public Optional<Joueur> getJoueurById(String id) {
        return joueurRepository.findById(id);
    }

    public Joueur addExperience(String joueurId, int experience) {
        Optional<Joueur> joueurOpt = joueurRepository.findById(joueurId);

        if (joueurOpt.isPresent()) {
            Joueur joueur = joueurOpt.get();
            joueur.setExperience(joueur.getExperience() + experience);
            return joueurRepository.save(joueur);
        } else {
            throw new IllegalArgumentException("Joueur non trouvé");
        }
    }

    public Joueur levelUp(String joueurId) {
        Optional<Joueur> joueurOpt = joueurRepository.findById(joueurId);

        if (joueurOpt.isPresent()) {
            Joueur joueur = joueurOpt.get();
            joueur.setLevel(joueur.getLevel() + 1);
            joueur.setExperience(0);  // Reset l'expérience
            joueur.getMonstres().add(""); // Ajoute un monstre supplémentaire par niveau
            return joueurRepository.save(joueur);
        } else {
            throw new IllegalArgumentException("Joueur non trouvé");
        }
    }

    public Joueur addMonstre(String joueurId, String monstreId) {
        Optional<Joueur> joueurOpt = joueurRepository.findById(joueurId);

        if (joueurOpt.isPresent()) {
            Joueur joueur = joueurOpt.get();
            joueur.getMonstres().add(monstreId);
            return joueurRepository.save(joueur);
        } else {
            throw new IllegalArgumentException("Joueur non trouvé");
        }
    }

    public Joueur removeMonstre(String joueurId, String monstreId) {
        Optional<Joueur> joueurOpt = joueurRepository.findById(joueurId);

        if (joueurOpt.isPresent()) {
            Joueur joueur = joueurOpt.get();
            joueur.getMonstres().remove(monstreId);
            return joueurRepository.save(joueur);
        } else {
            throw new IllegalArgumentException("Joueur non trouvé");
        }
    }

    public boolean deleteJoueur(String id) {
        if (joueurRepository.findById(id).isPresent()) {
            joueurRepository.deleteById(id);
            return true;
        } else {
            return false;
        }
    }
}