from innolva_spider.innolva_spider.dao.mongoDAO import MongoDAO
from innolva_spider.innolva_spider.model.Article import Article


class ArticleToDB(MongoDAO):

    def __init__(self,

                 host: str = "mongodb+srv://smantuano:12345@dbarticles-qv1r7.mongodb.net/test?retryWrites=true&w=majority",
                 db: str = "INNOLVA_SPIDER_DB"):
         super().__init__(host, db)

    def save(self, collection: str, obj):
        """save a single article or a single string"""
        dict = {}
        if type(obj) == str:
            dict = {"Link": obj}
        elif isinstance(obj, Article):
            dict = {
                "Link": obj.url,
                "Data": obj.date,
                "Autore": obj.author,
                "Titolo": obj.title,
                "Body": obj.body
            }
        super().save(collection, dict)

    def save_list(self, collection: str, list):
        """save a single article or a single string"""
        dict = {}
        for obj in list:
            if type(obj) == str:
                dict = ({"Link": obj})
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
        coll = self.get_coll(collection)
        coll.update_many(condition_dict, {"$set": update_dict}, upsert=True)

    def links_list(self, collection: str, start: int = 0):
        """return a set that contain all links inside a function"""
        my_set = set()
        coll = self.get_coll(collection)
        for el in coll.find().skip(start):
            el["_id"] = str(el["_id"])
            my_set.add(el["Link"])
        return my_set

