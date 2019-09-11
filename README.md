# aplli-immobilier

oh je comprend rien, j'ai cru qu'on me demandé de faire ca MAIS nan enfaite grr bon au moins c cool ^^

en gros il faut:

  - finir de remplir la database
  
    -attendre le chargement (trop chiant)
    
    -supprimer les data qui se repetent
    
  - faire une auto complétion via la database
    - ca je sais pas encore mais si le type écrit un truk faire un like en ajax a chaque on saisit(ca va ramer donc au pire pas grave)
    
  - l'utilisateur saisi un input
  - réponse google map
    - AJAX on récupere lat et long dans la database
    
  - estimation du prix de la meme rue
    - on recupere avec un where et on dit le max et min ou direct avec sql
    - si on a rien, on va directe scrappper l'info sur internet ce n'est pas a but lucratif donc légal
    
  - avec une moyenne par le nombre de piece et le type (maison ou appartement)
   - faire une moyenne par recup des donnée
   
  - faire la doc
    - installation (csv, gzip ...)
    - lancement dabord database
    - ect
