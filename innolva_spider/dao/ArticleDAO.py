from innolva_spider.dao.mongoDAO import MongoDAO
from innolva_spider.model.Article import Article


class ArticleDAO(MongoDAO):

    # def __init__(self,
    #
    #              host: str = "mongodb+srv://smantuano:12345@dbarticles-qv1r7.mongodb.net/test?retryWrites=true&w=majority",
    #              db: str = "INNOLVA_SPIDER_DB"):
    #      super().__init__(host, db)

    def save(self, collection: str, obj):
        """save a single article or a single string"""
        dict = {}
        if type(obj) == list:
            for i in obj:
             dict = {
                "Link": obj.url,
                "Data": obj.date,
                "Autore": obj.author,
                "Titolo": obj.title,
                "Body": obj.body
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

    article1 = Article("dvdwfew", "fegrerher", "sara", "ascasfasf", "dsfsdfs")
    a = ArticleDAO("localhost", "DATABASE", 27017)
    a.save("collection", article1)
    #a.clear_collection("collection")
    #a.query("collection",{"Autore":"Sara"})
    a.update_multiple_by_condition_dict("collection", )