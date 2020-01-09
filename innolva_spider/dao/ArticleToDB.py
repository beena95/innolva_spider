from innolva_spider.dao.mongoDAO import MongoDAO


class ArticleToDB(MongoDAO):

    def __init__(self, host: str = "localhost", port: int = 27017, db: str = "ARTICLE_DB"):
        super().__init__(host, port, db)

    def save(self, obj, collection: str):
        """save a link or an article into a collection"""
        coll = self.get_coll(collection)
        if type(obj) == str:
            coll.insert_one({"Link": obj})
        else:
            dict = {
                "Link": obj.url,
                "Data": obj.date,
                "Autore": obj.author,
                "Titolo": obj.title,
                "Body": obj.body
                }
            coll.insert_one(dict)

    def save_list(self, obj, collection: str):
        """save an article list or a string list inside a collection"""
        coll = self.get_coll(collection)
        for link in obj:
            if type(link) == str:
                coll.insert_one({"Link": link})
            else:
                dict = {
                    "Link": link.url,
                    "Data": link.date,
                    "Autore": link.author,
                    "Titolo": link.title,
                    "Body": link.body
                    }
                coll.insert_one(dict)

    def update_multiple_by_condition_dict(self, collection: str, condition_dict: dict, update_dict: dict):
        """update more documents that match a condition"""
        coll = self.get_coll(collection)
        coll.update_many(condition_dict, {"$set": update_dict}, upsert=True)
