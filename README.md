# ChatGPT Telegram Bot:

This repo is ChatGPT as Telegram Bot. 

Original Author's [karfly/chatgpt_telegram_bot](https://github.com/karfly/chatgpt_telegram_bot) version: [@chatgpt_karfly_bot](https://t.me/chatgpt_karfly_bot)
This repo's instance: [@winternewt_bot](https://t.me/winternewt_bot)

## Bot commands
- `/start` – Get started
- `/retry` – Regenerate last bot answer
- `/new` – Start new dialog
- `/mode` – Select chat mode
- `/balance` – Show balance
- `/settings` – Show settings
- `/help` – Show help

## Setup
1. Get your [OpenAI API](https://openai.com/api/) key
2. Get your Telegram bot token from [@BotFather](https://t.me/BotFather)
3. Edit `config/config.example.yml` to set your tokens and run 2 commands below (*if you're advanced user, you can also edit* `config/config.example.env`):
    ```bash
    mv config/config.example.yml config/config.yml
    mv config/config.example.env config/config.env
    ```

4. 🔥 And now **run**:
    ```bash
    docker-compose --env-file config/config.env up --build
    ```

## References
1. [*Build ChatGPT from GPT-3*](https://learnprompting.org/docs/applied_prompting/build_chatgpt)
