package com.demo;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/joueurs")
public class JoueurController {
    @Autowired
    private JoueurService joueurService;

    @PostMapping("/add")
    public Joueur createJoueur(@RequestBody Joueur joueur) {
        return joueurService.createJoueur(joueur);
    }

    @GetMapping("/")  // Afficher tous les joueurs
    public List<Joueur> getAllJoueurs() {
        return joueurService.getAllJoueurs();
    }

    @GetMapping("/{id}")
    public Optional<Joueur> getJoueur(@PathVariable String id) {
        return joueurService.getJoueurById(id);
    }

    @PutMapping("/{id}/experience")
    public Joueur addExperience(@PathVariable String id, @RequestParam int experience) {
        return joueurService.addExperience(id, experience);
    }

    @PutMapping("/{id}/level-up")
    public Joueur levelUp(@PathVariable String id) {
        return joueurService.levelUp(id);
    }

    @PutMapping("/{id}/monstres")
    public Joueur addMonstre(@PathVariable String id, @RequestParam String monstreId) {
        return joueurService.addMonstre(id, monstreId);
    }

    @DeleteMapping("/{id}/monstres/{monstreId}")
    public Joueur removeMonstre(@PathVariable String id, @PathVariable String monstreId) {
        return joueurService.removeMonstre(id, monstreId);
    }

    @DeleteMapping("/del/{id}")  // Nouvelle méthode pour supprimer un joueur
    public ResponseEntity<String> deleteJoueur(@PathVariable String id) {
        boolean deleted = joueurService.deleteJoueur(id);
        if (deleted) {
            return ResponseEntity.ok("Joueur supprimé avec succès");
        } else {
            return ResponseEntity.status(404).body("Joueur non trouvé");
        }
    }
/*
 * {
    "id": "123",
    "level": 1,
    "experience": 50,
    "monstres": []
}
*/
}