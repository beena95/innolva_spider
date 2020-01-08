from innolva_spider.dao.mongoDAO import MongoDAO


class ArticleToDB(MongoDAO):
    def __init__(self, host, port, db):
        super().__init__(host, port, db)

    def save(self, obj, collection: str):
        coll = self.get_coll(collection)
        if type(obj) == str:
            coll.insert_one({"Link": obj})
        else:
            dict = {
                "URL": obj.URL,
                "Data": obj.data,
                "Autore": obj.autore,
                "Titolo": obj.titolo,
                "Body": obj.body}
            coll.insert_one(dict)

    def save_list(self, obj, collection: str):
        coll = self.get_coll(collection)
        for link in obj:
            if type(link) == str:
                coll.insert_one({"Link": link})
            else:
                dict = {
                    "URL": link.URL,
                    "Data": link.data,
                    "Autore": link.autore,
                    "Titolo": link.titolo,
                    "Body": link.body}
                coll.insert_one(dict)

    def create_collection(self, collection):
        try:
            self.client[self.db][collection]
        except:
            print("this collection can't be created")

    def update_multiple_by_condition_dict(self, collection, condition_dict, update_dict):
        coll = self.get_coll(collection)
        coll.update_many(condition_dict, {"$set": update_dict}, upsert=True)
