from pyrogram import Client

import os, logging, json

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

##############################################
api_id =  1597219
api_hash = "252f4132f58c15c9c5ccfccdba79c974"
##############################################

jugged = -1001124792940

with Client("history_update", api_id, api_hash) as app:
    logging.info("Getting history.")
    d = {
        msg.audio.file_name: msg.message_id
        for msg in (app.iter_history(jugged))
        if msg.audio
        if not None
    }
    logging.info("Done.")
    with open(
            "/home/jugged/jugged/res/jggd_data.json",
            "w",
            encoding="utf-8"
    ) as f:
        logging.info("Writing history to json file.")
        json.dump(d, f)
        logging.info("Done.")
