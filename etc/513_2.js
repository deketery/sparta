// and  &&   or || 

let person1 = {"name":"김승환","age":"30","work":"회사원"}
let person2 = {"name":"김해리","age":"29","work":"백수"}
//20대 판별기 and

function check_20(person){
    if (person["age"]>=20 && person["age"]<30 ){
        return true;
    }
    else{
        return false;
    }
}

// 회사원 이거나 프리랜서면 true 아니면 false
function check_worker(person){
    if (person["work"] == "회사원" || person["work"]=="프리랜서"){
        return true;
    }
    else{
        return false;
    }
}

// i=i+1     i ++ .js    //  i += 1 .py

// for (let i=0, i<=100, i++){
// console.log(i);
// }