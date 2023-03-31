BOOK_PATH = '/home/gotcrab/PycharmProjects/book_bot/books/book.txt'
PAGE_SIZE = 900

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    symbols = ('.', ',', '!', '?', ':', ';')
    end = start + page_size
    if (len(text) - start) < page_size:
        return text[start:], len(text[start:])
    while text[end] in symbols:
        end -= 1
    while text[end - 1] not in symbols:
        end -= 1
    result = text[start: end]
    return result, len(result)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, encoding='utf-8') as bk:
        cursor = 0
        page = 1
        book_in_work: str = bk.read()

    while cursor != len(book_in_work):
        book[page] = _get_part_text(book_in_work, cursor, PAGE_SIZE)[0].lstrip()
        cursor_next = _get_part_text(book_in_work, cursor, PAGE_SIZE)[1]
        cursor += cursor_next
        page += 1


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)

