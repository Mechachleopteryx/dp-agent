from .settings import TELEGRAM_TOKEN, TELEGRAM_PROXY
from .core.telegram_client import run_tg
from .setup_agent import setup_agent


def main():
    agent, session, workers = setup_agent()
    try:
        run_tg(TELEGRAM_TOKEN, TELEGRAM_PROXY, agent)
    finally:
        session.close()
        for i in workers:
            i.cancel()


if __name__ == '__main__':
    main()