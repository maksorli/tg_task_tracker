from sqlalchemy.orm import Session

from models.models import TelegramUser


def get_services(session: Session):
 
    query = session.query(TelegramUser)

    

    tasks = query.all()
    # return [website.url for website in websites]
    return tasks