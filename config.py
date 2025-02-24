import os
import logging

class Config:
    
    API_ID = int(os.environ.get("20919625", 12345))
    API_HASH = os.environ.get("40168846bf06f4ff443f0f7a4182bf8d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BOT_SESSION = os.environ.get("1BVtsOJABu4viqJmSLRAkLo35--Ea0dUV-K1hLsg1U7bq5xzdakKdHBGnSaCLEGczKlht99v7thsmThHdB55YdBn8diEnkQCncE1t1NdBOB1GaHyAnc2dsYNQL3BTKdJq6UAjiwlfShum8zY9NP4UL-loNHEhvkoRhE37kg4Dxvl-vg1qWE2RjSkdG7duC3lulx1eBDhGFXG1cnRaj3t6cCqfoyb9CYKPDHPoWkoIJH95AuJ7tjqTnZZBbKEXsqp-QRGmduknLjd-5lV_FW0S1zGXop4QM2rhp6L6p0DmNUYl3FYtCo-WxiCz-CEDEYv9fFbMrpGjJjL41FXS6fuKod09Jv7g0Bc=", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("6233910543", 12345)
    SESSION = os.environ.get("BQE_NUkAauZeGk0BtuZXDBpRkodvSWlzer7YCp5PgErKa73rv2TGIs7bCfexxQ-w2ZZX1MNu69Hu9gSfvW0I6QKpVVwIupLRcZSgd52WVzP4u4b5gNPlu44cTP-cy0XuFkALLSZeLrmpbGlbdBXWmTcEuVBXsm2V7nEp_8bzcPYIyG0qckVwRUsDXWFmger6Cg2cgCF9M1QLkFDqwPx6RB4xp-6TxvCp7Hu36Owe2TjpF7qPSvKLL-EWkv_J0LOvd9MO8fA2C-Em8-Tyx2LodgJlbd2sedEUpikPwMj147wqLW-k3lssY30p_xL4FwHEgDDVLuo4PeGJMMIrsDNDqQ-LgcpELwAAAAFzke0PAA")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
