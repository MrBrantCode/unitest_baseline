"""
QUESTION:
Implement a caching system with two classes, `StopCache` and `BusCache`, each representing a cache for stops and buses respectively. Each cache class should have the following methods: `get_<entity>(entity_id)`, `set_<entity>(entity_id, entity_info)`, and `delete_<entity>(entity_id)`, where `<entity>` is either `stop` or `bus`. The cache should use a dictionary to store the entities, where the keys are the entity IDs and the values are the corresponding entity information. The cache should handle cache misses by returning `None` when an entity is not found. The cache eviction policy should be a simple removal of the entity when the `delete_<entity>` method is called.
"""

def entrance(stops, buses):
    class Cache:
        def __init__(self):
            self.cache = {}

        def get(self, entity_id):
            return self.cache.get(entity_id, None)

        def set(self, entity_id, entity_info):
            self.cache[entity_id] = entity_info

        def delete(self, entity_id):
            if entity_id in self.cache:
                del self.cache[entity_id]

    stop_cache = Cache()
    bus_cache = Cache()

    for stop_id, stop_info in stops.items():
        stop_cache.set(stop_id, stop_info)

    for bus_id, bus_info in buses.items():
        bus_cache.set(bus_id, bus_info)

    def get_stop(stop_id):
        return stop_cache.get(stop_id)

    def get_bus(bus_id):
        return bus_cache.get(bus_id)

    def set_stop(stop_id, stop_info):
        stop_cache.set(stop_id, stop_info)

    def set_bus(bus_id, bus_info):
        bus_cache.set(bus_id, bus_info)

    def delete_stop(stop_id):
        stop_cache.delete(stop_id)

    def delete_bus(bus_id):
        bus_cache.delete(bus_id)

    return {
        'get_stop': get_stop,
        'get_bus': get_bus,
        'set_stop': set_stop,
        'set_bus': set_bus,
        'delete_stop': delete_stop,
        'delete_bus': delete_bus,
    }