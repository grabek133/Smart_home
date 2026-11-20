# Smart_home

Serwer Model Context Protocol (MCP) w Pythonie. Udostępnia jedno narzędzie `Smart_home`, które sprawdza parametr tekstowy `nowy_kolor` w formacie `#RRGGBB` i zwraca przyjętą wartość wielkimi literami. Przykładowo `{"nowy_kolor":"#ffaabb"}` zwraca `{"nowy_kolor":"#FFAABB"}`. Funkcja potwierdza przyjęcie koloru. Sterowanie fizycznym urządzeniem wymaga osobnej integracji.

Projekt korzysta z oficjalnego SDK MCP dla Pythona i transportu Streamable HTTP. [Dokumentacja MCP](https://modelcontextprotocol.io/introduction) · [SDK dla Pythona](https://github.com/modelcontextprotocol/python-sdk)

## Uruchomienie lokalne

Wymagany jest Python 3.10 lub nowszy. Polecenia dla Linuxa i macOS, wykonywane w katalogu projektu:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python server.py
```

Klient MCP może połączyć się z `http://127.0.0.1:8000/mcp` przez Streamable HTTP.

## Połączenie z ChatGPT

ChatGPT potrzebuje publicznego adresu HTTPS zakończonego `/mcp`. Na hoście z publiczną domeną i certyfikatem TLS uruchom serwer lokalnie i skieruj ruch na niego przez reverse proxy. Przykładowa konfiguracja Caddy, gdzie `mcp.example.com` należy zastąpić własną domeną:

```caddyfile
mcp.example.com {
    reverse_proxy /mcp 127.0.0.1:8000 {
        header_up Host 127.0.0.1:8000
    }
}
```

Ten endpoint działa bez uwierzytelniania i wykonuje wyłącznie walidację koloru. W wersji webowej ChatGPT na koncie z dostępem do trybu deweloperskiego dodaj aplikację MCP z adresem `https://mcp.example.com/mcp` i wybierz brak uwierzytelniania. Po dodaniu sprawdź na tym samym koncie na Androidzie, czy aplikację można wybrać w rozmowie. Dostępność własnych aplikacji MCP na Androidzie zależy od obsługi po stronie ChatGPT i ustawień konta. [Instrukcja łączenia aplikacji z ChatGPT](https://developers.openai.com/apps-sdk/deploy/connect-chatgpt)
