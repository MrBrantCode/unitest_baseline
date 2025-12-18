"""
QUESTION:
Implement the `extract_entities_and_relations` function, which takes a dictionary representing the NLU response as input and returns a list of tuples. Each tuple should contain information about the extracted entities and relations. The function should handle the following: 

- Entities: a tuple `(entity_type, entity_text)`
- Relations: a tuple `(relation_type, entity1_text, entity2_text)`

The NLU response is a dictionary with the following structure: 
```json
{
  "entities": [
    {
      "type": "entity_type",
      "text": "entity_text"
    }
  ],
  "relations": [
    {
      "type": "relation_type",
      "entity1": "entity1_text",
      "entity2": "entity2_text"
    }
  ]
}
```
"""

def extract_entities_and_relations(nlu_response: dict) -> list:
    entities = [(entity['type'], entity['text']) for entity in nlu_response.get('entities', [])]
    relations = [(relation['type'], relation['entity1'], relation['entity2']) for relation in nlu_response.get('relations', [])]
    return entities + relations