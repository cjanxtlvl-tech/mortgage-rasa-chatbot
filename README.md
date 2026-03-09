# mortgage-rasa-chatbot

A starter Rasa chatbot project for a mortgage lead generation website.

This assistant is designed for:
- Lead capture
- Loan-type guidance
- Basic FAQ handling
- Callback requests
- Light pre-qualification

## Project References
- Product/business goals: `PROJECT_GOALS.md`
- Technical chatbot spec: `docs/chatbot-spec.md`

## Quick Start
1. Install dependencies:
   ```bash
   pip install rasa rasa-sdk
   ```
2. Train the model:
   ```bash
   rasa train
   ```
3. Run the assistant in shell mode:
   ```bash
   rasa shell
   ```
4. Run the custom action server (separate terminal):
   ```bash
   rasa run actions
   ```

## Using Makefile Shortcuts
If you prefer shortcut commands, use:

```bash
make install
make train
make shell
make actions
make test
```

## Repository Structure
- `domain.yml`: Intents, entities, slots, responses, and form definitions
- `config.yml`: NLU pipeline and dialogue policies
- `data/`: NLU, stories, rules, and form blueprint content
- `actions/actions.py`: Custom actions and form validation hooks
- `tests/test_stories.yml`: Conversation tests

## Notes for Contractors
- This is a clean starter foundation for V1.
- Keep response tone professional, friendly, concise, and conversion-focused.
- Add CRM/webhook integrations in custom actions when backend endpoints are ready.
