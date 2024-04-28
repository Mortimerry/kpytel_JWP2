from sqlalchemy import create_engine, Column, Integer, String, text, inspect, MetaData, Table, func, select
from sqlalchemy.orm import declarative_base, Session


engine = create_engine('sqlite:///census.sqlite', echo=True, future=True)
connection = engine.connect()


inspector = inspect(engine)
table_names = inspector.get_table_names()
print(table_names)

metadata = MetaData()
state_fact = Table('state_fact', metadata, autoload_with=engine)
print(repr(state_fact))

census = Table('census', metadata, autoload_with=engine)
print(repr(census))

#Podpunkt 1
pd1 = text('SELECT DISTINCT name FROM state_fact ORDER BY name asc')
result_proxy = connection.execute(pd1)
results1 = result_proxy.fetchall()
print(results1)

#Podpunkt 2

pd2 = text('SELECT state, sum(pop2000) as Populacja2000, sum(pop2008) as Populacja2008 FROM census WHERE state = "Alaska" or state = "New York" GROUP BY state')
result_proxy = connection.execute(pd2)
results2 = result_proxy.fetchall()
print(results2)


#Podpunkt3

pd3 = text('SELECT state, sex, sum(pop2008) as Populacja2008 FROM census WHERE state = "New York" and sex = "F" UNION ALL SELECT state,sex, sum(pop2008) as Kobiety FROM census WHERE state = "New York" and sex = "M"')
result_proxy = connection.execute(pd3)
results3 = result_proxy.fetchall()
print(results3)