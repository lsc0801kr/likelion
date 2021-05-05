pairs = {'red': '빨간색', 'blue': '파랑색', 'green': '초록색'}
# 딕셔너리 자료형 {key:value}

# 새로운 자료 data를 추가하자
pairs['yellow'] = '노랑색'
print(pairs)

# 기존 data를 삭제하자
# del 딕셔너리형 변수{key}로 표현
del pairs['blue']
print(pairs)

# key를 통해서 value를 얻는 함수 .get함수
# 딕셔너리형 변수.get(key)
color = pairs.get('green')
print(color)

color1 = pairs.get('red')
print(color1)
