from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import (Student, Teacher, Review)
import ipdb

if __name__ == '__main__':
    engine = create_engine("sqlite:///db/reviews.db")

    Session = sessionmaker(bind=engine)
    session = Session()

    ipdb.set_trace()