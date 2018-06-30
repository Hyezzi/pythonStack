## Stack using python list
#### 스택(stack)의 의미와 특징
  * 추상 데이터형(abstract data type)
  * 데이터를 후입선출 하는 방식 사용 (LIFO : Last In, First Out)
    *  가장 먼저 삽입되어 스택에 들어간 요소가 가장 최후에 삭제
  * 기본 연산 : 삽입(push), 삭제(pop)
    * 삽입 : 데이터 요소를 스택의 최상위(top)에 추가하고 기존의 요소들은 그 아래에 둠
    * 삭제 : 스택의 현재 최상위 요소를 제거하고 이를 반환
  * 오버플로우(overflow)와 언더플로우(underflow)
    * 오버플로우 : 스택이 가득 찬 경우 새로운 요소를 삽입 연산을 통해 스택에 추가하려고 하면 오버플로우(overflow) 상태
    * 언더플로우 : 스택이 비어 있는 경우(empty) 삭제를 시도하면 언더플로우(underflow) 상태
    
#### 스택의 장점
 * 구현과 이해가 쉬움. 
 * 입출력이 역순인 경우 용이함. 
 
#### 스택의 단점
 * 배열로 구현하는 경우, 스택의 크기가 고정적이라 최대 크기 이상의 값을 삽입 불가
 * 배열로 구현하는 경우, 메모리 낭비가 발생
 * 최상단 이외의 값을 이용해야 할 경우 번거로움. 

#### 스택의 용도
 * 입력과 출력이 역순으로 이루어져야 하는 경우
   * 에디터의 되돌리기 기능
 * back tracking
   * 인공지능의 경우, 브랜치의 형태로 표현된 여러가지 경우의 수를 비교하여 가장 효율적인 경우를 찾아야 한다. 효율적이지 않을 경우, 특정 노드로 돌아가서 다른 경우의 수를 찾아야 한다. 이 방식은 지나왔던 노드들은 반대로 돌아가며 기점이 되는 특정 노드로 돌아가야 하므로, stack을 사용한다. 
 * 메인 메모리
   * 함수를 실행중일 때, 실행 과정에서 발생하는 주소 저장. 함수 실행이 시작하면 push, 종료되면 pop.
