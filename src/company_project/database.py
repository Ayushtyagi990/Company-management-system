from sqlmodel import SQLModel, Session, create_engine

engine = create_engine(
    "mysql+pymysql://root:@127.0.0.1:3306/company_project",
    echo=True
)

def get_session():
    with Session(engine) as session:
        yield session


SQLModel.metadata.create_all(engine)
