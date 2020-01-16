from pymongo.errors import DuplicateKeyError
from innolva_spider.dao.mongoDAO import MongoDAO


class UrlDAO(MongoDAO):

    def __init__(self,
                 host: str = "mongodb+srv://beena95:xdzm6m6v2@dbarticles-qv1r7.mongodb.net/test?retryWrites=true&w=majority",
                 db: str = "INNOLVA_SPIDER_DB",
                 override_primary_key: bool = True):
        super().__init__(host, db)

    def save_url(self, collection: str, url: str):\
        """save a single url inside a collection"""
        coll = self.getcoll(collection)
        try:
            coll.insert({"_id": url})
        except DuplicateKeyError:
            print("key already exists")

    def check_visited(self, url: str, collection: str):
        """check if a single url exists inside a collection"""
        coll = self.getcoll(collection)
        if coll.find_one({"_id": url}):
            return True
        else:
            return False

    def all_urls(self, collection: str) -> set:
        """return a set that contains every link inside a collection"""
        links_set = set()
        coll = self.getcoll(collection)
        for el in coll.find():
            # el is a single document inside the collection
            links_set.add(el["_id"])
        return links_set

    def clear_collection(self, collection: str):
        """remove every document inside a collection"""
        coll = self.getcoll(collection)
        coll.remove()

    def delete_url(self, url: str, collection: str):
        """remove a single url from a collection"""
        coll = self.getcoll(collection)
        coll.remove({"_id": url})


if __name__ == '__main__':
    db = UrlDAO()
    url = "esdasdsaecsa"
    coll = db.getcoll("TEST")
    # coll.create_index({"Link":"sdsdsdsd"})
    # coll.create_index([("Link", DESCENDING)], unique=True)
    # db.clear_collection("TEST")
    # coll.insert({"_id": "www.jusiancasablancas.com"})
    # coll.drop()
    # print(db.check_visited(url, "TEST"))
    # db.save_url("TEST", "3skwjrgfdksnfjwbrhkfnkdkaxsade")
    db.delete_url("TEST", "3skwjrgfdksnfjwbrhkfnkdkaxsade")



