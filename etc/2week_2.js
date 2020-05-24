//0. numbers에 있는 모든 값을 출력하기

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for (i = 0; i < numbers.length; i++) {
    console.log(numbers[i])
}

//1. 입력된 숫자보다 작은 수를 모두 출력한다.

function f(num) {
    for (i = 0; i < num; i++) {
        console.log(i)
    }
}

//2. 입력된 숫자보다 작은 짝수 모두 출력하기
//2-1
function d(times) {
    for (i = 2; i < times; i = i + 2) {
        console.log(i)
    }
}
//2-2
// function dd(times){
//     for (let i =2;  i%2 ==0 ;i++){
//         console.log(i)
//     }
// }


//3. 0부터 n-1까지 더하는 함수를 만들고싶다면?

function plus(x) {
    let sum = 0;
    for (let i = 0; i < x; i++) {
        sum = sum + i;
    }
    console.log(sum)
}

// 다음에서 '딸기'는 몇 개일까? 
let fruit_list = ['사과', '감', '감', '배', '포도', '포도', '딸기', '포도', '감', '수박', '딸기']

function count_fruit(fruit_name) {
    let count = 0;
    for (let i = 0; i < fruit_list.length; i++) {
        if (fruit_list[i] == fruit_name) {
            count++
        }
    }
    console.log(count)
}