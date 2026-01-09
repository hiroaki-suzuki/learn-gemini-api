from google import genai
from google.genai import types

client = genai.Client()


def generate_monster_summary():
    # Geminiへのリクエスト
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="漫画のMonsterの概要について100文字程度で教えて下さい",
    )

    print("=" * 80)
    print(response.text)
    print("=" * 80)


def generate_google_search():
    # GeminiのWeb検索
    grounding_tool = types.Tool(google_search=types.GoogleSearch())
    config = types.GenerateContentConfig(tools=[grounding_tool])

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents="Geminiの最新の状況を教えて下さい",
        config=config,
    )

    print("=" * 80)
    print(response.text)
    print("=" * 80)


if __name__ == "__main__":
    generate_monster_summary()
    generate_google_search()
