from dotenv import dotenv_values

class Config:
    config = dotenv_values(".env.config")
    
    @staticmethod
    def get_app_url() -> str:
        return Config.config['NOTESPAGE__URL']