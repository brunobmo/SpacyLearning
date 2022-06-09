# Import spaCy
import spacy

# Create a blank English nlp object
nlp = spacy.blank("en")

# Created by processing a string of text with the nlp object
doc = nlp("Hello world!")

# Iterate over tokens in a Doc
for token in doc:
    print(token.text)

# Index into the Doc to get a single Token
token = doc[1]

# Get the token text via the .text attribute
print(token.text)