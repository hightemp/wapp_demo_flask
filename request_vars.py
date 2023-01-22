import pydotenv

env = pydotenv.Environment()

__DEBUG__ = env.get('__DEBUG__', False)
STATIC_PATH = "/static"

if (__DEBUG__):
    STATIC_PATH = "/zip/static"

# Книга(PDF)
# - Название
# - Ссылка - файл
# - Ссылка - заметки

def fnGetTopMenu():
    return [
        {
            "href": "/",
            "title": '<i class="bi bi-house"></i>'
        },
        {
            "href": "/books",
            "title": '<i class="bi bi-book"></i>' 
        },
        {
            "href": "/notes",
            "title": '<i class="bi bi-journal"></i>' 
        },
        {
            "href": "/comments",
            "title": '<i class="bi bi-layout-text-sidebar"></i>' 
        },
        {
            "href": "/files",
            "title": '<i class="bi bi-files"></i>' 
        },
    ]

class RequestVars:
    sStaticPath = STATIC_PATH

    oArgs = {}

    sCurrentPath = ""
    lTopMenu = fnGetTopMenu()

    oForm = None
    




