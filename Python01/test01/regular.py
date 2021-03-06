# regular expression 정규 표현식

import re
# re = python이 만들어든 모듈 | library
'''
Regular Expression
. : 문자 1개
^ : 문자열의 시작
$ : 문자열의 마지막
[] : 문자 집합
| : OR
() : 괄호 안 정규식 그룹

* : 0 or more
+ : 1 or more
? : 0 or 1
{n} : n번 반복 | n = 숫자
{n,m} : n번부터 m번까지
{n, } : n번부터 무한대
'''

"""
r 문자열 표기법 (re 모듈의 확장 문법)
\w : [a-zA-Z0-9_] : a~z, A~Z, 0~9 _를 포함하는 모든 문자
\W : [^a-zA-Z0-9_] : 위의 문자를 제외한 나머지 문자 | ^ : not
\d : [0-9] : 0~9
\D : [^0-9] : 숫자를 제외한 나머지 문자
\s : [\t\n\r\f\v] : 공백문자 | \f\v : 위 아래
\S : [^\t\n\r\f\v] : 공백을 제외한 나머지 문자
\b : 단어의 시작과 끝의 빈 공백
\B : 단어의 시작과 끝이 아닌 빈 공백
\\ : \
\[n] : 지정된 n만큼 일치하는 문자열
\A : 문자열의 시작
\Z : 문자열의 끝
"""

str01 = '나의 이메일은 kh.123@kh.com123 입니다.'
match = re.search(r'[a-z.\d]*@[a-zA-z.]*', str01)
# [\w] : 문자들이 들어갈건데, * 몇 개 들어가도 상관없음(0 ~ more)
# @ 꼭 들어가야할 문자 | [a-zA-z.] .까지 몇 개도 상관없음

print(match.group())

