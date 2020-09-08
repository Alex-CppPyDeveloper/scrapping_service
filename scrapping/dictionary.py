dec = {
    u'a': u'a',
    u'б': u'b',
    u'в': u'v',
    u'г': u'g',
    u'д': u'd',
    u'е': u'e',
    u'ё': u'e',
    u'ж': u'zh',
    u'з': u'z',
    u'и': u'i',
    u'й': u'yi',
    u'к': u'k',
    u'л': u'l',
    u'м': u'm',
    u'н': u'n',
    u'о': u'o',
    u'п': u'p',
    u'р': u'r',
    u'с': u'c',
    u'т': u't',
    u'у': u'u',
    u'ф': u'f',
    u'х': u'h',
    u'ц': u'ts',
    u'ч': u'ch',
    u'ш': u'sh',
    u'щ': u'sch',
    u'э': u'e',
    u'ь': u'',
    u'ы': u'y',
    u'ъ': u'',
    u'ю': u'yu',
    u'я': u'ya',
}


def rus_in_eng(text):
    text = text.replace(' ', '_').lower()
    tranc_text = ''
    for ch in text:
        tranc_text += dec.get(ch, ch)

    return tranc_text
