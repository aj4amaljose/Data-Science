from .connection import SessionLocal


def get_session():
    """
    Manages session during function execution
    """
    session = SessionLocal()
    try:
        yield session
    except:
        session.rollback()
    finally:
        session.commit()
        session.close()
