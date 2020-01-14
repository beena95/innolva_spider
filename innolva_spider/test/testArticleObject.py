from innolva_spider.dao.ArticleDAO import ArticleToDB
from innolva_spider.model.Article import Article


class Article2:
    def __init__(self, URL, data, autore, titolo, body):
        self.url = URL
        self.date = data
        self.author = autore
        self.title = titolo
        self.body = body
if __name__ == '__main__':


    URL = Article("https://www.lastampa.it/", "01/04/2019", "Aldo Baglio",
               "Storia di un uomo molto strano che diceva parole dure",
               "C'era una volta un uomo che diceva cose molto strane e questo lo rendeva ancora piu' strano, stranamente pero' le sue stranezze erano una delle cose piu' ambigue e strane presenti su questo mondo di strabe stranezze")
    URL1 = Article("https://www.corriere.it/", None, "LORENZO BINACCI", "sbakbfafb", "kjdasodhsalhaslkcjakofchaso")
    a = "Articles"
    lista = ["dfdwwx", "dsasfqw", "rgfdwxasdas", "adsafs", "cwqdwsa", "fsadsda"]
    database = ArticleToDB("mongodb+srv://beena95:xdzm6m6v2@dbarticles-qv1r7.mongodb.net/test?retryWrites=true&w=majority", "DBARTICLES")
    # database.object_to_json(lista, "collection")
    # database.delete_by_id("collection", "5dfba3775846ef0f6e71ee39")
    # database.save(URL, "Articoli")
    # database.save(URL1,"Articoli")
    # database.create_collection("Articles")
    # database.update_by_id("Articoli", "5e10c1ed5ed34f13d33e1270", {"Data" : "674634", "Robe" : "Cose strane"})
    # database.update_by_id("Articoli", "5e10bd556c992fcfb92ba256", {"Autore" :"franco"} )
    # database.delete_by_conditiondict("Articoli", {"Body" :"kjdasodhsalhaslkcjakofchaso"})
    # print(database.count("Articoli"))
    # print(database.get_by_conditiondict("Articoli", {"Autore" :"LORENZO BINACCI"}))
    # database.update_multiple_by_conditiondict("Articoli", {"Autore" :"LORENZO BINACCI"},{"Body" : "Gnagna"} )
    # database.save(lista, "Articoli")
    #database.object_to_json(lista, "collection")
    #database.delete_by_id("collection", "5dfba3775846ef0f6e71ee39")
    #database.save(URL, "Articoli")
    #database.save(URL1,"Articoli")
    #database.create_collection("Articles")
    #database.update_by_id("Articoli", "5e10c1ed5ed34f13d33e1270", {"Data" : "674634", "Robe" : "Cose strane"})
    #database.update_by_id("Articoli", "5e10bd556c992fcfb92ba256", {"Autore" :"franco"} )
    #database.delete_by_conditiondict("Articoli", {"Body" :"kjdasodhsalhaslkcjakofchaso"})
    #print(database.count("Articoli"))
    #print(database.get_by_conditiondict("Articoli", {"Autore" :"LORENZO BINACCI"}))
    #database.update_multiple_by_conditiondict("Articoli", {"Autore" :"LORENZO BINACCI"},{"Body" : "Gnagna"} )
    # for link in database.query("Articoli", {"Autore" :"LORENZO BINACCI"}):
    #     print(link)
    # database.save(URL, "mario")
    # for article in database.all("Links"):
    #     print(type(article))
    database.save_list("Articoli", lista)



    

