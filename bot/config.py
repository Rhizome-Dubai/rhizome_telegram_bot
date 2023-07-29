import yaml
import dotenv
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load yaml config
with open(config_dir / "config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# load .env config
config_env = dotenv.dotenv_values(config_dir / "config.env")

# config parameters
telegram_token = config_yaml["telegram_token"]
openai_api_key = config_yaml["openai_api_key"]
chatgpt_model = config_yaml.get("default_model", "gpt-3.5-turbo") 
allowed_telegram_usernames = config_yaml["allowed_telegram_usernames"]
new_dialog_timeout = config_yaml["new_dialog_timeout"]
enable_message_streaming = config_yaml.get("enable_message_streaming", True)
return_n_generated_images = config_yaml.get("return_n_generated_images", 1)
n_chat_modes_per_page = config_yaml.get("n_chat_modes_per_page", 5)
mongodb_uri = f"mongodb://{config_env['MONGODB_URI']}:{config_env['MONGODB_PORT']}"
mongodb_db = f"{config_env['MONGODB_DB']}"

# chat_modes
with open(config_dir / "chat_modes.yml", 'r', encoding='utf-8') as f:
    chat_modes = yaml.safe_load(f)

# models
with open(config_dir / "models.yml", 'r', encoding='utf-8') as f:
    models = yaml.safe_load(f)
available_models=models.get("available_text_models", ["gpt-3.5-turbo", "gpt-3.5-turbo-16k", "gpt-4"])
chat_models=models.get("available_chat_models", ["gpt-3.5-turbo", "gpt-3.5-turbo-16k", "gpt-4"])
comp_models=models.get("available_completion_models", ["text-davinci-003"])
# files
help_group_chat_video_path = Path(__file__).parent.parent.resolve() / "static" / "help_group_chat.mp4"
