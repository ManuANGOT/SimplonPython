// Création de la constante result permettant de récupérer l'élément HTML id="result"
const result = document.querySelector(`#result`);

//Déclaration des variables
var prenom = "";
nom ="";
résultat = "";
affichage = "";

//Affichage du titre dans le HTML
affichage= "<h3>Addition de deux variables type chaîne (Concaténation)</h3>";

// Récupération des saisies utilisateur pour le nom et prénom
nom = prompt("Veuillez saisir votre nom : ");
affichage += `<span>Vous avez saisi <b>${nom}</b>`;
prenom = prompt("Veuillez saisir votre prenom : ");
affichage += `<span> Vous avez saisi : <b>${prenom}</b>`;

// Addition des deux chaînes (concaténation)
// affichage  += "bonjour"
resultat = " Bonjour <b>" + prenom + " " + nom +"</b> <br/>";

// Ajout de résultat à la variable affichage :
affichage += resultat;

// Affichage du contenu de la variable affichage dans l'élément HTML #result
result.innerHTML = affichage;
