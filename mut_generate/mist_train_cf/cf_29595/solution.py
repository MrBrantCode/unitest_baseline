"""
QUESTION:
Implement the `test_recognition_overlap` function that takes an initialized spaCy NLP pipeline as input and evaluates the recognition overlap between taxon and chemical entities in a given text. The function should return the overlap statistics, including the number of overlapping entities and their respective spans.

The input pipeline is expected to be initialized with the "en_core_web_sm" model and include custom components for recognizing taxa and chemicals using the "taxontagger" and "chemtagger" respectively. The function should work with a provided test data or sample text that is processed by the input pipeline.
"""

def test_recognition_overlap(pipeline, doc):
    # Initialize variables to store overlapping entities and their spans
    overlapping_entities = []
    overlapping_spans = []

    # Extract entities of type taxon and chemical from the document
    taxon_entities = [ent.text for ent in doc.ents if ent.label_ == "TAXON"]
    chemical_entities = [ent.text for ent in doc.ents if ent.label_ == "CHEMICAL"]

    # Find overlapping entities between taxa and chemicals
    overlap = set(taxon_entities) & set(chemical_entities)
    overlapping_entities.extend(overlap)

    # Find the spans of overlapping entities
    for entity in overlap:
        taxon_spans = [ent.start_char for ent in doc.ents if ent.text == entity and ent.label_ == "TAXON"]
        chemical_spans = [ent.start_char for ent in doc.ents if ent.text == entity and ent.label_ == "CHEMICAL"]
        overlapping_spans.extend((taxon_span, chemical_span) for taxon_span in taxon_spans for chemical_span in chemical_spans)

    # Return the statistics of recognition overlap
    return {
        "num_overlapping_entities": len(overlapping_entities),
        "overlapping_entities": overlapping_entities,
        "overlapping_spans": overlapping_spans
    }