from innolva_spider.dao.mongoDAO import MongoDAO


class ArticleDAO(MongoDAO):

    def save(self, collection: str, obj):
        """save a single article or a single string"""
        dict = {}
        if type(obj) == list:
            for i in list:
             dict = {
                "Link": obj.url,
                "Data": obj.date,
                "Autore": obj.author,
                "Titolo": obj.title,
                "Body": obj.body
            }
            super().save(collection, dict)
        else:
            dict = {
                "Link": obj.url,
                "Data": obj.date,
                "Autore": obj.author,
                "Titolo": obj.title,
                "Body": obj.body
            }

    def update_multiple_by_condition_dict(self, collection: str, condition_dict: dict, update_dict: dict):
        """update multiple documents that match a condition"""
        coll = self.getcoll(collection)
        coll.update_many(condition_dict, {"$set": update_dict}, upsert=True)

    def clear_collection(self, collection: str):
        """remove every document inside a collection"""
        coll = self.getcoll(collection)
        coll.remove()

if __name__ == '__main__':
    lista = ["url","sdfwfv"]
    a = ArticleDAO
    a.save("collection", lista)

