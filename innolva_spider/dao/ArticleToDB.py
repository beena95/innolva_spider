from innolva_spider.dao.mongoDAO import MongoDAO


class ArticleToDB(MongoDAO):

    def __init__(self,
                 host: str = "mongodb+srv://smantuano:12345@dbarticles-qv1r7.mongodb.net/test?retryWrites=true&w=majority",
                 db: str = "DBARTICLES"):

        super().__init__(host, db)

    def save(self, obj, collection: str):
<<<<<<< HEAD
        """save a link or an article into a collection"""
=======
        """save a single article or a single string"""
>>>>>>> d91b09296389306ded1a8b4961c922b28aa9fe22
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
<<<<<<< HEAD
        """save an article list or a string list inside a collection"""
=======
        """save multiple obj or str inside a list"""
>>>>>>> d91b09296389306ded1a8b4961c922b28aa9fe22
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
<<<<<<< HEAD
        """update more documents that match a condition"""
=======
        """update multiple documents that match a condition"""
>>>>>>> d91b09296389306ded1a8b4961c922b28aa9fe22
        coll = self.get_coll(collection)
        coll.update_many(condition_dict, {"$set": update_dict}, upsert=True)

