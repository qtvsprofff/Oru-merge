import os


class Config(object):
    API_HASH = os.environ.get("90d16b7e658fed5fdb5f7660875081ff")
    BOT_TOKEN = os.environ.get("6419648779:AAHRFbbiuD_PeedlK4OlLia2JHfXIKcYW-w")
    TELEGRAM_API = os.environ["19962151"]
    OWNER = os.environ.get("885675538")
    OWNER_USERNAME = os.environ.get("SMD_Owner")
    PASSWORD = os.environ.get("qtvsmerge-robot")
    DATABASE_URL = os.environ.get("mongodb+srv://Leechbot:$nopassword0$@cluster0.96aznin.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("-1001707403763")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("BQEwmScAIE-O8pyEewOvl4zu_aiYQ5IBdAOrj00s0Ls18gEdE3qQBFOEAZaHVkvwyXGeUPEX2g7wAcvrTjOcgXQrLoQ7x7WPLDWFM667M4ISDPOYerqGoChxFF8jRU2k7g6bWbFpUlCMNS3hHXx24txwjceLsF42-ixQNYVApWHanRgWMx-7NVVR-ab8FJ42UQWSa--PAmUw3m_ZIGyaZHmlX7hDUJeDi5BdCf9WHjbMTdFLUthdmc3o7jCVRUH2FMho30c_nmAP-JRYHNNOIf4MzLCQbwYJ5U5ouuzopTWYxuPuxinKtQ2_biaiei9TqLdl7wdQ0MYc_6iUY2Ej-SAICxw2EAAAAABpeCb7AA", None)
    IS_PREMIUM = True
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]
