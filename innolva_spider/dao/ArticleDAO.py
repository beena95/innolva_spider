from innolva_spider.dao.mongoDAO import MongoDAO
from innolva_spider.model.Article import Article


class ArticleDAO(MongoDAO):

    def __init__(self,
                 host: str = "mongodb+srv://gneata:12345@dbarticles-qv1r7.mongodb.net/test?retryWrites=true&w=majority",
                 db: str = "INNOLVA_SPIDER_DB"):
        super().__init__(host, db)

    def save(self, collection: str, obj):
        """save a single article or a single string"""
        if type(obj) == list:
            for article in obj:
                dict = {
                    "Link": article.url,
                    "Data": article.date,
                    "Autore": article.author,
                    "Titolo": article.title,
                    "Body": article.body
                }
                super().save(collection, dict)
        elif isinstance(obj, Article):
            dict = {
                "Link": obj.url,
                "Data": obj.date,
                "Autore": obj.author,
                "Titolo": obj.title,
                "Body": obj.body
            }
            super().save(collection, dict)

    def update_multiple_by_condition_dict(self, collection: str, condition_dict: dict, update_dict: dict):
        """update multiple documents that match a condition"""
        coll = self.getcoll(collection)
        coll.update_many(condition_dict, {"$set": update_dict}, upsert=True)

    def clear_collection(self, collection: str):
        """remove every document inside a collection"""
        coll = self.getcoll(collection)
        coll.remove()


if __name__ == '__main__':
    lista = ["dgahahtrh", "agra<grhe<g", "segGG<GR", "sRHAHAERH", "WGahrad"]

    # article1 = Article("dvdwfew", "fegrerher", "sara", "ascasfasf", "dsfsdfs")
    a = ArticleDAO()
    articolo = Article("jijibjnj", "hbjnkmkmk", "sei un gaggio", "jbghcvbjnjk", "vghbjnjnk")
    a.save("TEST", articolo)
    # a.clear_collection("collection")
    # a.query("collection",{"Autore":"Sara"})
    # a.clear_collection("TEST")
