from bson import ObjectId
from pymongo import MongoClient, DESCENDING


class MongoDAO:

    def __init__(self, host, db):
        self.db = db
        self.host = host
        self.client = MongoClient(host=self.host)

    def save(self, collection, obj):
        coll = self.get_coll(collection)
        if not type(obj) == list:
            obj = [obj]
        obj_to_insert = [o for o in obj if "_id" not in o]
        obj_to_update = [o for o in obj if "_id" in o]
        # insert on object without "_id" field
        if len(obj_to_insert) > 0:
            coll.insert(obj_to_insert, check_keys=False)
        # update on object with "_id" field
        for o in obj_to_update:
            id_ob = o["_id"]
            del o["_id"]
            try:
                doc = coll.find_one_and_update(
                    {"_id": ObjectId(id_ob)},
                    {"$set": o}, upsert=True)
                if not doc:
                    coll.insert(o, check_keys=False)
            except:
                coll.insert(o, check_keys=False)

    def update_by_id(self, collection, id, key_values_dict):
        """this function updates the document that match the input id"""
        coll = self.get_coll(collection)
        if self.get_by_id(collection, id):
            coll.find_one_and_update({"_id": ObjectId(id)}, {"$set": key_values_dict}, upsert=True)

    def update_by_condition_dict(self, collection, conditiondict, updatedict):
        """this function updates the document that match the condition"""
        coll = self.get_coll(collection)
        coll.update_one(conditiondict, {"$set": updatedict}, upsert=True)

    def delete_by_id(self, collection, id):
        """this function delete the document that has input id"""
        coll = self.get_coll(collection)
        coll.remove({"_id": ObjectId(id)})

    def delete_by_condition_dict(self, collection, conditiondict):
        """this function delete the document that the condition"""
        coll = self.get_coll(collection)
        coll.remove(conditiondict, True)

    def all(self, collection, start: int = 0, rows: int = None, selection=None):
        """return the whole collection"""
        coll = self.get_coll(collection)
        if rows:
            for el in coll.find(None, selection).skip(start).limit(rows):
                el["_id"] = str(el["_id"])
                yield el
        else:
            for el in coll.find().skip(start):
                el["_id"] = str(el["_id"])
                yield el

    def links_list(self, collection, start: int = 0):
        """get the links throught a set"""
        my_set = set()
        coll = self.get_coll(collection)
        for el in coll.find().skip(start):
            el["_id"] = str(el["_id"])
            my_set.add(el["Link"])
        return my_set

    def get_by_id(self, collection, id):
        """get the document that match the id"""
        coll = self.get_coll(collection)
        el = coll.find_one({"_id": ObjectId(id)})
        if not el:
            raise Exception("Element with id " + str(id) + " not found")
        el["_id"] = str(el["_id"])
        return el

    def get_by_condition_dict(self, collection, conditiondict):
        """get the document based on id"""
        coll = self.get_coll(collection)
        el = coll.find_one(conditiondict)
        if not el:
            raise Exception("Element not found")
        return el

    def collections(self):
        """get all the collections"""
        return self.client.get_database(self.db).collection_names()

    def drop(self, collection):
        """delete a single collection"""
        coll = self.get_coll(collection)
        coll.drop()

    def get_coll(self, collection):
        """get a collection"""
        return self.client.get_database(self.db).get_collection(collection)

    def sample(self, collection, n):
        coll = self.get_coll(collection)
        for el in coll.aggregate([{"$sample": {"size": n}}]):
            el["_id"] = str(el["_id"])
            yield el

    def query(self, collection, where, select=None):
        """with this function you can do a query similar to sql database"""
        coll = self.get_coll(collection)
        for el in coll.find(where, select):
            el["_id"] = str(el["_id"])
            yield el

    def copy(self, collection1, collection2):
        """copy everything inside the first collection inside the second collection"""
        coll1 = self.get_coll(collection1)
        coll2 = self.get_coll(collection2)
        coll2.remove()
        for el in coll1.find():
            coll2.insert(el)

    def count(self, collection):
        """count the documents inside the collection"""
        return self.get_coll(collection).count()

    def get_last(self, collection, q: {} = None):
        """get the last document added to collection"""
        coll = self.get_coll(collection)
        return coll.find_one(sort=[('_id', DESCENDING)])

    def clear_collection(self, collection):
        """remove every document inside a collection"""
        coll = self.get_coll(collection)
        coll.remove({})
