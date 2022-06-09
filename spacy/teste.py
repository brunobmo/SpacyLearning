import spacy
from gensim.corpora.dictionary import Dictionary
from gensim.models.ldamodel import LdaModel

data = """Os sócios das sociedades por quotas unipessoais ICR, os investidores informais das sociedades veículo de investimento em empresas com potencial de crescimento, certificadas no âmbito do Programa COMPETE, e os investidores informais em capital de risco a título individual certificados pelo IAPMEI, no âmbito do Programa FINICIA, podem deduzir à sua coleta em IRS do próprio ano, até ao limite de 15% desta, um montante correspondente a 20% do valor investido por si ou pela sociedade por quotas unipessoais ICR de que sejam sócios.
Por valor investido entende-se a entrada de capitais em dinheiro destinados à subscrição ou aquisição de quotas ou ações ou à realização de prestações acessórias ou suplementares de capital em sociedades que usem efetivamente essas entradas de capital na realização de investimentos com potencial de crescimento e valorização.

A dedução à coleta acima referida não se aplica aos seguintes casos:
a) Investimentos em sociedades cotadas em bolsa de valores e em sociedades cujo capital seja controlado maioritariamente por outras sociedades, excetuados os investimentos efetuados em SCR e em fundos de capital de risco;
b) Investimentos em sociedades sujeitas a regulação pelo Banco de Portugal ou pela Autoridade de Supervisão de Seguros e Fundos de Pensões.
A dedução à coleta deste benefício está limitada pelo n.º 7 do <a href="http://www.lexit.pt/0C00.0762">artigo 78.º</a> do CIRS, que fixa limites absolutos para o total de deduções à coleta, incluindo benefícios fiscais, a partir do 2.º escalão do rendimento coletável."""

# Our spaCy model:
nlp = spacy.load("pt_core_news_lg")# Tags I want to remove from the text
doc = nlp(data)
removal= ['ADV','PRON','CCONJ','PUNCT','PART','DET','ADP','SPACE', 'NUM', 'SYM']
tokens = []
for token in doc:
   proj_tok = [token.lemma_.lower() for token in doc if token.pos_ not in removal and not token.is_stop and token.is_alpha]
   tokens.append(proj_tok)

# print(tokens)

# I will apply the Dictionary Object from Gensim, which maps each word to their unique ID:
dictionary = Dictionary(tokens)

#print(dictionary.token2id)

corpus = [dictionary.doc2bow(doc) for doc in tokens]
#print(corpus)

lda_model = LdaModel(corpus=corpus, id2word=dictionary, iterations=50, num_topics=10, passes=10)
#print(lda_model.print_topics())
print(lda_model[corpus][0])
#data['tokens'] = tokens
#data['tokens']