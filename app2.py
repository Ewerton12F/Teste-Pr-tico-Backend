from sqlalchemy import create_engine, inspect, MetaData, Table

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ewertonfreitas:ZXdlcnRvbmZy@jobs.visie.com.br/ewertonfreitas'
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

# Create a MetaData instance
metadata = MetaData()
print(metadata.tables)

# reflect db schema to MetaData
metadata.reflect(bind=engine)
print(metadata.tables)