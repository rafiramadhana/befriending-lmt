from flask import Flask
import json
import logging

logging.getLogger("werkzeug").disabled = True
logging.basicConfig(level=logging.INFO, format="%(message)s")


class StructuredMessage(object):
    def __init__(self, message, **kwargs):
        self.message = message
        self.kwargs = kwargs
        self.level = self.kwargs["level"]
        if self.level == "":
            self.level = "INFO"

    def __str__(self):
        return "[%s] %s %s" % (self.level, self.message, json.dumps(self.kwargs))


app = Flask(__name__)


@app.post("/books/purchase")
def purchase_book():
    ok = False

    if ok:
        logging.info(
            StructuredMessage(
                "POST /books/purchase 200",
                level="INFO",
                book_name="Hello world",
                book_publisher="John",
            )
        )
        return "OK"
    else:
        logging.error(
            StructuredMessage(
                "POST /books/purchase 408",
                level="ERROR",
                book_name="Hello world",
                book_publisher="John",
            )
        )
        return "Book not found!", 408
