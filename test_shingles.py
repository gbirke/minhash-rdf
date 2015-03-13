import shingles
import StringIO

def test_2_byte_shingles():
    test_str = StringIO.StringIO("abcde")
    assert list(shingles.byte_tokenizer(test_str, 2)) == ["ab", "bc", "cd", "de"]

def test_4_byte_shingles():
    test_str = StringIO.StringIO("abcde")
    assert list(shingles.byte_tokenizer(test_str, 4)) == ["abcd", "bcde"]

def test_2_word_shingles():
    test_str = StringIO.StringIO("The big  \n brownfox jumps over the lazy")
    expected = ["The big", "big brownfox", "brownfox jumps", "jumps over", "over the", "the lazy"]
    word_shingles = list(shingles.word_tokenizer(test_str, 2))
    assert word_shingles == expected

def test_4_word_shingles():
    test_str = StringIO.StringIO("The big  \n brownfox jumps over the lazy")
    expected = ["The big brownfox jumps", "big brownfox jumps over", "brownfox jumps over the", "jumps over the lazy"]
    word_shingles = list(shingles.word_tokenizer(test_str, 4))
    assert word_shingles == expected

test_triples = """
<http://dbpedia.org/resource/Autism> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Disease> .
<http://dbpedia.org/resource/Autism> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation> .
<http://dbpedia.org/resource/Aristotle> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Philosopher> .
<http://dbpedia.org/resource/Aristotle> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Agent> .
<http://dbpedia.org/resource/Aristotle> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent> .
<http://dbpedia.org/resource/Alabama> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/AdministrativeRegion> .
<http://dbpedia.org/resource/Alabama> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.ontologydesignpatterns.org/ont/d0.owl#Location> .
<http://dbpedia.org/resource/Abraham_Lincoln> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/OfficeHolder> .
<http://dbpedia.org/resource/Abraham_Lincoln> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent> .
"""

def test_2_triple_shingles():
    expected = [
        "<http://dbpedia.org/resource/Autism> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Disease> .\n<http://dbpedia.org/resource/Autism> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation> .",
        "<http://dbpedia.org/resource/Autism> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation> .\n<http://dbpedia.org/resource/Aristotle> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Philosopher> .",
        "<http://dbpedia.org/resource/Aristotle> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Philosopher> .\n<http://dbpedia.org/resource/Aristotle> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Agent> ."
    ]
    triple_shingles = list(shingles.triple_tokenizer(StringIO.StringIO(test_triples), 2))[:3]
    assert triple_shingles == expected

def test_2_turtle_shingles():
    expected = [
        "<http://dbpedia.org/resource/Autism> a <http://dbpedia.org/ontology/Disease>,<http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Situation> .\n<http://dbpedia.org/resource/Aristotle> a <http://dbpedia.org/ontology/Philosopher>,<http://dbpedia.org/ontology/Agent>,<http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent> .",
        "<http://dbpedia.org/resource/Aristotle> a <http://dbpedia.org/ontology/Philosopher>,<http://dbpedia.org/ontology/Agent>,<http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent> .\n<http://dbpedia.org/resource/Alabama> a <http://dbpedia.org/ontology/AdministrativeRegion>,<http://www.ontologydesignpatterns.org/ont/d0.owl#Location> .",
        "<http://dbpedia.org/resource/Alabama> a <http://dbpedia.org/ontology/AdministrativeRegion>,<http://www.ontologydesignpatterns.org/ont/d0.owl#Location> .\n<http://dbpedia.org/resource/Abraham_Lincoln> a <http://dbpedia.org/ontology/OfficeHolder>,<http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#Agent> ."
    ]
    triple_shingles = list(shingles.turtle_tokenizer(StringIO.StringIO(test_triples), 2))
    assert triple_shingles == expected