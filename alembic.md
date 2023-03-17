- install alembic `pip install alembic`
- free codecamp video at 10.34.00 minute
- `alembic init alembic` -> will create a folder called alembic
- inside the env file import the Base of database file
`from app.models import Base`
- also change the `target_metadata = Base.metadata` to Base.metadata
- put this in env.py file 
```
config.set_main_option("sqlalchemy.url",f"postgresql+psycopg2://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}")
```

- when we want to make changes to db , we do revision, it tracks all the changes on a step by step
- `alembic revision -m "create post table"` this will create a file in revisions folder

- populate the upgrade function in revision file
    - `op.create_table('posts',sa.Column("id",sa.Integer(),nullable=False,primary_key=True),sa.Column('title',sa.String(),nullable=False))`
- `alembic upgrade <revision id>` - will upgrade to a particular revision
- it will create a revison table along with the upgrade function data.Note : dont delete the revision table
- `alembic revision -m "add content column to post table"`- will give new revision
- `alembic current` will give the current revision number
- `alembic heads` will give the latest revision number
- `alembic upgrade head` will give take us to the latest revision
- `alembic downgrade <revision id>` or `alembic downgrade -1` will take us one step down
- `alembic revision -m "add user table"`
- we can also do `alembic upgrade +1` to go one step up
- `alembic revision -m "add foreign ket to post table"`
- alembic is intelligent to find which column is left and will do the changes by itself.
- `alembic revision --autogenerate -m "auto-vote"`