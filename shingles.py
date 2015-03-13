import re
import collections

def byte_tokenizer(input_file, num_tokens):
    bytes = collections.deque(maxlen=num_tokens)
    while 1:
        chunk = input_file.read(4096)
        if not chunk:
            break
        for c in chunk:
            bytes.append(c)
            if len(bytes) == num_tokens:
                yield "".join(bytes)

def word_tokenizer(input_file, num_tokens):
    words = collections.deque(maxlen=num_tokens)
    for line in input_file:
        words_line = re.split("\s+", line)
        for word in words_line:
            if not word:
                continue
            words.append(word)
            if len(words) == num_tokens:
                yield " ".join(words)

def triple_tokenizer(input_file, num_tokens):
    triples = collections.deque(maxlen=num_tokens)
    triple_pattern = re.compile(r"\s*<[^>]+>\s+<[^>]+>\s+<[^>]+>\s+\.")
    for line in input_file:
        is_triple = triple_pattern.match(line)
        if not is_triple:
            continue
        triples.append(is_triple.group(0))
        if len(triples) == num_tokens:
                yield "\n".join(triples)

def turtle_tokenizer(input_file, num_tokens):
    """ Convert DBPedia triple format to more compact turtle statements """
    triples = collections.deque(maxlen=num_tokens)
    triple_pattern = re.compile(r"\s*(<[^>]+>)\s+<[^>]+>\s+(<[^>]+>)\s+\.")
    current_predicate = None
    objects = []
    for line in input_file:
        is_triple = triple_pattern.match(line)
        if not is_triple:
            continue
        if is_triple.group(1) != current_predicate:
            if current_predicate:
                triples.append("{} a {} .".format(current_predicate, ",".join(objects)))
            current_predicate = is_triple.group(1)
            objects = []
            if len(triples) == num_tokens:
                yield "\n".join(triples)
        objects.append(is_triple.group(2))
        
    # flush last 
    triples.append("{} a {} .".format(current_predicate, ",".join(objects)))
    if len(triples) == num_tokens:
        yield "\n".join(triples)