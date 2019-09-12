# aplli-immobilier

oh je comprend rien, j'ai cru qu'on me demandé de faire ca MAIS nan enfaite grr bon au moins c cool ^^ merde pcque le bas est pas beau

en gros il faut:


  - le mec saisit son code postal, si on en trouve un on dit ok sinon on va scrapper

  - on a pas beaucoup de data on sort ce que l'on
  
    - par exemple gyé-sur-seine on a que 4 données. On dit sur le département en maison vaut 50 000 euro
    
    - on donne la possibilité de voir le prix value sur le code postal

  - faire une auto complétion via la database
    - ca je sais pas encore mais si le type écrit un truk faire un like en ajax a chaque on saisit(ca va ramer donc au pire pas grave)
    
  - réponse google map
    - AJAX on récupere lat et long dans la database
  
  - estimation du prix de la meme rue
    - on recupere avec un where et on dit le max et min ou direct avec sql
    - si on a rien, on va directe scrappper l'info sur internet ce n'est pas a but lucratif donc légal
    
  - avec une moyenne par le nombre de piece et le type (maison ou appartement)
   - faire une moyenne par recup des donnée
   
  - si avant ce soir ok, faire selon le code postal tous les départements et faire des zones de prix
    
    - dire au détail si c'est vendu ou non par scrappage
   
   
   - rendre le bas jolie
   
   
  - faire la doc
    - installation (csv, gzip ...)
    - lancement dabord database
    - ect
