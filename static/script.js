// Fonction pour ajouter un pal
function ajouterPal() {
    const db = document.getElementById('db').value;
    const collection = document.getElementById('collection').value;
    const id = document.getElementById('id').value;
    const nom = document.getElementById('nom').value;

    fetch('/api/insert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ db, collection, id, nom }),
    })
    .then(response => response.json())
    .then(data => alert(data.message))
    .catch(error => console.error('Error:', error));
}



//Fonction pour get par type
function rechercheParType(){


    const type = document.getElementById('type').value;
    console.log(type)
    // Utilisez la comparaison strictement non égale à '' pour vérifier si l'ID n'est pas vide
    if (type !== '') {
        const url = `/api/GetByType?db=Hamza&collection=pal&type=${type}`;

        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error('La réponse du réseau n\'était pas ok');
                }
                return response.json();  // Convertit la réponse en JSON
            })
            .then(data => {
                const resultWindow = window.open();
                resultWindow.document.write(`<pre>${JSON.stringify(data, null, 2)}</pre>`);
                resultWindow.document.close(); // Assurez-vous de fermer le document pour finaliser l'écriture
            })
            .catch(error => {
                console.error('Erreur lors de la recherche:', error);
                alert('Erreur lors de la recherche. Veuillez vérifier la console pour plus de détails.');
            });
    } else {
        alert("Veuillez entrer un Type valide."); // Correction de 'alerte' à 'alert'
    }
}




function getAllType() {
    const typeListElementLeft = document.getElementById('idListLeft');

    // Réinitialiser la liste des types
    typeListElementLeft.innerHTML = '';

    // Récupérer les types du serveur
    fetch('/api/GetAllType')
        .then(response => {
            if (!response.ok) {
                throw new Error('La réponse du réseau n\'était pas ok');
            }
            return response.json(); // Convertit la réponse en JSON
        })
        .then(data => {
            // Vérifier si la réponse contient bien un champ 'types'
            if (data && data.types) {
                // Ajouter chaque type à la liste
                data.types.forEach(type => {
                    const li = document.createElement('li');
                    li.textContent = type;
                    typeListElementLeft.appendChild(li);
                });
            } else {
                throw new Error('Format des données inattendu');
            }
        })
        .catch(error => {
            console.error('Erreur lors de la récupération des types:', error);
            alert('Erreur lors de la récupération des types. Veuillez vérifier la console pour plus de détails.');
        });
}












































function rechercheID() {
    const id = document.getElementById('id2').value;

    // Utilisez la comparaison strictement non égale à '' pour vérifier si l'ID n'est pas vide
    if (id !== '') {
        const url = `/api/GetById?db=Hamza&collection=pal&id=${id}`;

        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error('La réponse du réseau n\'était pas ok');
                }
                return response.json();  // Convertit la réponse en JSON
            })
            .then(data => {
                const resultWindow = window.open();
                resultWindow.document.write(`<pre>${JSON.stringify(data, null, 2)}</pre>`);
                resultWindow.document.close(); // Assurez-vous de fermer le document pour finaliser l'écriture
            })
            .catch(error => {
                console.error('Erreur lors de la recherche:', error);
                alert('Erreur lors de la recherche. Veuillez vérifier la console pour plus de détails.');
            });
    } else {
        alert("Veuillez entrer un ID valide."); // Correction de 'alerte' à 'alert'
    }
}



function getAllID() {
    const idListElementLeft = document.getElementById('idListLeft');
    const idListElementRight = document.getElementById('idListRight');

    // Réinitialiser les listes des IDs
    idListElementLeft.innerHTML = '';
    idListElementRight.innerHTML = '';

    // Récupérer les IDs du serveur
     fetch('/api/GetAllIDs?db=Hamza&collection=pal')
        .then(response => {
            if (!response.ok) {
                throw new Error('La réponse du réseau n\'était pas ok');
            }
            return response.json(); // Convertit la réponse en JSON
        })
        .then(data => {
            // Ajouter chaque ID à la liste
            data.forEach((id, index) => {
                const li = document.createElement('li');
                li.textContent = id;
                // Répartir les IDs dans les deux colonnes
                if (index % 2 === 0) {
                    idListElementLeft.appendChild(li);
                } else {
                    idListElementRight.appendChild(li);
                }
            });
        })
        .catch(error => {
            console.error('Erreur lors de la récupération des IDs:', error);
            alert('Erreur lors de la récupération des IDs. Veuillez vérifier la console pour plus de détails.');
        });
}







//Fonction pour get par Name
function rechercheParName(){


    const name = document.getElementById('name').value;
    console.log(name)
    if (name !== '') {
        const url = `/api/GetByName?name=${name}`;

        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error('La réponse du réseau n\'était pas ok');
                }
                return response.json();
            })
            .then(data => {
                const resultWindow = window.open();
                resultWindow.document.write(`<pre>${JSON.stringify(data, null, 2)}</pre>`);
                resultWindow.document.close();
            })
            .catch(error => {
                console.error('Erreur lors de la recherche:', error);
                alert('Erreur lors de la recherche. Veuillez vérifier la console pour plus de détails.');
            });
    } else {
        alert("Veuillez entrer un Name valide.");
    }
}






function getAllName() {
    const idListElementLeft = document.getElementById('idListLeft');
    const idListElementRight = document.getElementById('idListRight');

    // Réinitialiser les listes des IDs
    idListElementLeft.innerHTML = '';
    idListElementRight.innerHTML = '';

    // Récupérer les IDs du serveur
     fetch('/api/GetAllName')
        .then(response => {
            if (!response.ok) {
                throw new Error('La réponse du réseau n\'était pas ok');
            }
            return response.json(); // Convertit la réponse en JSON
        })
        .then(data => {
            // Ajouter chaque ID à la liste
            data.forEach((name, index) => {
                const li = document.createElement('li');
                li.textContent = name;
                // Répartir les IDs dans les deux colonnes
                if (index % 2 === 0) {
                    idListElementLeft.appendChild(li);
                } else {
                    idListElementRight.appendChild(li);
                }
            });
        })
        .catch(error => {
            console.error('Erreur lors de la récupération des IDs:', error);
            alert('Erreur lors de la récupération des IDs. Veuillez vérifier la console pour plus de détails.');
        });
}











function getSkillPal() {
    const SkillPal = document.getElementById('SkillPal');
    const name2 = document.getElementById('namepal').value;

    SkillPal.innerHTML = '';

    fetch(`/api/GetSkillPal?name=${name2}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('La réponse du réseau n\'était pas ok');
            }

            return response.json();
        })
        .then(data => {
            data.forEach(skill => {
                const li = document.createElement('li');
                console.log(data);
                li.innerHTML = `
                    <strong>Name:</strong> ${skill.name}<br>
                    <strong>Level:</strong> ${skill.level}<br>
                    <strong>Type:</strong> ${skill.type}<br>
                    <strong>Cooldown:</strong> ${skill.cooldown}<br>
                    <strong>Power:</strong> ${skill.power}<br>
                    <strong>Description:</strong> ${skill.description}<br>
                `;
                SkillPal.appendChild(li);
            });
        })
        .catch(error => {
            console.error('Erreur lors de la récupération des compétences:', error);
            alert('Erreur lors de la récupération des compétences. Veuillez vérifier la console pour plus de détails.');
        });
}



function addSkillToPal() {
    // Récupérer les valeurs des champs du formulaire
    const palName = document.getElementById('palName').value;
    const skillName = document.getElementById('skillName').value;
    const skillLevel = document.getElementById('skillLevel').value;
    const skillType = document.getElementById('skillType').value;
    const skillCooldown = document.getElementById('skillCooldown').value;
    const skillPower = document.getElementById('skillPower').value;
    const skillDescription = document.getElementById('skillDescription').value;

    const requestData = {
        pal_name: palName,
        skill_name: skillName,
        skill_level: skillLevel,
        skill_type: skillType,
        skill_cooldown: skillCooldown,
        skill_power: skillPower,
        skill_description: skillDescription
    };

    fetch('/api/AddSkillToPal', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('La réponse du réseau n\'était pas ok');
        }
        return response.json();
    })
    .then(data => {
        alert(data.message); // Afficher le message de réussite ou d'erreur
    })
    .catch(error => {
        console.error('Erreur lors de l\'ajout de la compétence au Pal:', error);
        alert('Erreur lors de l\'ajout de la compétence au Pal. check la console brotheeer');
    });
}



function modifyAttribute(event, form) {
    event.preventDefault();
    const oldName = form.oldName.value;
    const attributeName = form.attributeName.value;
    const newValue = form.newValue.value;
    console.log('Ancienne valeur :', oldName);
    console.log('Nouvelle valeur :', newValue);

    const palName = document.getElementById('palName').value;

    fetch('/api/ModifySkill', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: palName,
            skill_name: oldName,
            attribute_name: attributeName,
            new_value: newValue
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('La réponse du réseau n\'était pas ok');
        }
        return response.json();
    })
    .then(data => {
        alert.log(data.message);
        //window.location.reload();
    })
    .catch(error => {
        console.error('Erreur lors de la modification du skill:', error);
        alert('Erreur lors de la modification du skill. Veuillez vérifier la console pour plus de détails.');
    });
}



function removeTypeFromPal() {
    const palName = document.getElementById('palName').value;
    const palType = document.getElementById('palType').value;

    fetch('/api/RemoveTypeFromPal', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            name: palName,
            type: palType
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error('Erreur lors de la suppression du type du Pal:', error);
        alert('Erreur lors de la suppression du type. Veuillez vérifier la console pour plus de détails.');
    });
}



