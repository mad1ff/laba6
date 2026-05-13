class NewsScraperError(Exception):
    """Базовое исключение для скрейпера новостей."""
    pass

class NetworkError(NewsScraperError):
    """Ошибка сети при запросе."""
    pass

class ParsingError(NewsScraperError):
    """Ошибка при парсинге HTML."""
    pass

class EmptyNewsError(NewsScraperError):
    """Новости не найдены."""
    pass
