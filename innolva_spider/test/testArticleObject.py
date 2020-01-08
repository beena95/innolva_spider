from innolva_spider.dao.ArticleToDB import ArticleToDB


class Article:
    def __init__(self, URL, data, autore, titolo, body):
        self.URL = URL
        self.data = data
        self.autore = autore
        self.titolo = titolo
        self.body = body
if __name__ == '__main__':


    URL = Article("https://www.lastampa.it/", "01/04/2019", "Aldo Baglio",
               "Storia di un uomo molto strano che diceva parole dure",
               "C'era una volta un uomo che diceva cose molto strane e questo lo rendeva ancora piu' strano, stranamente pero' le sue stranezze erano una delle cose piu' ambigue e strane presenti su questo mondo di strabe stranezze")
    URL1 = Article("https://www.corriere.it/", None, "LORENZO BINACCI", "sbakbfafb", "kjdasodhsalhaslkcjakofchaso")
    lista = [URL, URL1]
    database = ArticleToDB("Localhost", 27017, "DATABASE")
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
    #database.save(lista, "Articoli")
    # for link in database.query("Articoli", {"Autore" :"LORENZO BINACCI"}):
    #     print(link)
    database.save(URL, "mario")

