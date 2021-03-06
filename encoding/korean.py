# -*- coding: utf-8 -*-
from __future__ import unicode_literals

korean = [[
    '#',
    'c',
    'ch',
    'h',
    'k',
    'kh',
    'kk',
    'l',
    'm',
    'n',
    'p',
    'ph',
    'pp',
    's',
    'ss',
    't',
    'th',
], [
    'a',
    'ay',
    'e',
    'ey',
    'i',
    'o',
    'oy',
    'u',
    'uy',
    'wa',
    'way',
    'we',
    'wey',
    'wi',
    'wu',
    'ya',
    'ye',
    'yey',
    'yo',
    'yu',
], [
    '#',
    'c',
    'k',
    'l',
    'm',
    'n',
    'ng',
    'p',
    's',
]]

# Official Romanization http://cms.kangwon.ac.kr/user/kimjm/publication/20_01ask_sampa.pdf
# Yale to KOROM http://www.u.arizona.edu/~kepeng/EastAsianCulture/PDFs/HW3K.pdf
# YALE
korean_On_to_xsampa = {
    '#': '#',
    'c': 'dZ_0',
    'cc': 'tS_>',
    'ch': 'tS_h',
    'h': 'h',
    'k': 'g_0',
    'kh': 'k_h',
    'kk': 'k_>',
    'l': '4',
    # 'l': 'L',
    'm': 'm',
    'n': 'n',
    'p': 'b_0',
    'ph': 'p_h',
    'pp': 'p_>',
    's': 's',
    # 's': 'S',
    'ss': 's_>',
    # 'ss': 'S_>',
    't': 'd_0',
    'th': 't_h',
}

korean_Cd_to_xsampa = {
    '#': '#',
    'c': 'dZ_0',
    'k': 'k_}',
    'l': 'l',
    'm': 'm:',
    'n': 'n:',
    'ng': 'N',
    'p': 'p_}',
    's': 's',
    # 's': 'S',
}

korean_Nu_to_xsampa = {
    'a': 'A',
    'ay': 'E',
    'e': 'V',
    'ey': 'e',
    'i': 'i',
    'o': 'o',
    'oy': '2',
    'u': 'M',
    'uy': 'Mj', # 'M\\i',
    'wa': 'wA',
    'way': 'wE',
    'we': 'wV',
    'wey': 'we',
    'wi': 'wi',
    'wu': 'u',
    'ya': 'jA',
    'ye': 'jV',
    'yey': 'je',
    'yo': 'jo',
    'yu': 'ju',
}

korean2xsampa = [korean_On_to_xsampa, korean_Nu_to_xsampa, korean_Cd_to_xsampa]
