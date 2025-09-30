import nltk
from gensim.models import Word2Vec
from nltk.corpus import stopwords
import re

paragraph ="""The world economy links nations through trade, investment, and finance.
Globalization has increased interdependence among countries.
International trade allows specialization and efficiency.
Exports provide income, while imports meet demand.
The balance of trade influences economic strength.
Foreign investment drives industrial development.
Multinational corporations spread technology worldwide.
Financial markets channel capital into businesses.
Stock markets reflect investor confidence.
Central banks regulate money supply and stability.
Interest rates affect borrowing and spending.
Inflation lowers purchasing power.
Deflation slows growth and raises risks.
Unemployment remains a global concern.
High employment drives demand and consumption.
Government spending supports economic activity.
Public debt creates financial pressure.
Taxation funds infrastructure and services.
Fiscal policy balances growth and stability.
Monetary policy manages liquidity and inflation.
Trade agreements promote cooperation.
Free trade zones boost efficiency.
Protectionism restricts competition and growth.
Tariffs raise costs for consumers.
Currency values affect exports and imports.
Strong currencies hurt exporters but help buyers.
Weak currencies make exports cheaper.
Global institutions oversee financial risks.
The IMF supports nations in crisis.
The World Bank funds development projects.
The WTO resolves trade disputes.
The EU created a single market.
The United States drives global finance.
China reshapes trade with rapid growth.
India attracts rising investment.
Japan leads in innovation.
Africa provides natural resources.
Latin America supplies agriculture.
The Middle East influences energy.
Oil and gas dominate markets.
Renewables gain importance for sustainability.
Climate change impacts global stability.
Technology drives productivity.
Digital currencies challenge banks.
Cryptocurrencies bring opportunities and risks.
Inequality persists between nations.
Education strengthens human capital.
Entrepreneurship fuels job creation.
Sustainable growth needs cooperation.
The global economy continues to evolve."""
     
#text preprocessing the data 
text = re.sub(r'\[[0-9]*\]', ' ',paragraph)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+', ' ',text)

sentences = nltk.sent_tokenize(text)

sentences = [nltk.word_tokenize(sentences) for sentences in sentences]

for i in range (len(sentences)):
    sentences[i] = [word for word in sentences[i] if word not in stopwords.words('english')]
    

model = Word2Vec(sentences,min_count=1)


words = model.wv.vocab

vector = model.wv['economy']

similar = model.wv.most_similar('economy')

similar = model.wv.most_similar('trade')

similar = model.wv.most_similar('growth')

similar = model.wv.most_similar('technology')

similar = model.wv.most_similar('beautiful')






















