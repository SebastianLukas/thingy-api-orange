import redis
import math


class Database:
    """
    Database handler for Redis db.
    Implements functions for operating on Redis sorted sets (ZSET).
    """

    __connection = None
    __time_range = 86400 # TTL for database entries in seconds. Currently set to 86400 (1 day).

    def __init__(self):
        self.__connection = redis.Redis(host='localhost', port=6379, db=0)

    def enqueue(self, key, value, score):
        self.__connection.zadd(key, value, score)

    def insert(self, key, value):
        self.__connection.set(key, value)

    def get(self, key):
        return self.__connection.get(key)

    def exists(self, key):
        return self.__connection.exists(key)

    def get_set(self, key, start, end):
        return self.__connection.zrange(key, start, end)

    def get_set_len(self, key):
        return len(self.__connection.zrange(key, 0, -1))

    def delete(self, key):
        self.__connection.delete(key)

    def del_expired_items(self, key, curr_time):
        print("checking for expired items")
        rem = self.__connection.zremrangebyscore(key, -math.inf, curr_time - self.__time_range)
        print("removed items: ", rem)

    def get_hash(self, key, hash_name):
        return self.__connection.hget(key, hash_name)

    def get_hash_all(self, key):
        return self.__connection.hgetall(key)

    def set_hash(self, key, hash_key, val):
        return self.__connection.hset(key, hash_key, val)

    def set_hash_multiple(self, key, values):
        return self.__connection.hmset(key, values)
    
    def delete_hash(self, key, hash_key):
        return self.__connection.hdel(key, hash_key)

    def key_exists_in_hash(self, key, hash_key):
        return self.__connection.hexists(key, hash_key)