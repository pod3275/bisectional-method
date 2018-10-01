# bisectional-method
- 수치해석에서 많이 사용되는 이분법(bisectional method) 함수 python code.
- 유효숫자는 소수점 n째자리로 설정됨.
    - 각 반복마다 같은 숫자로 반복되는 경우 수렴이기 때문에 정답의 유효숫자로 간주함.
- f(x)=0인 해에 대한 이분법 실행.
- 코드의 main은 예시 문제로, f(x) = x/30 - cos(x) 에 대한 해를 구함.
    - x = 30cos(x) 이므로 -30부터 30까지 범위를 가짐. 따라서 MIN = -30, MAX = 30.
