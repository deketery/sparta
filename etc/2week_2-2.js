// 50이상 도시만 추출
$.ajax({
    type: "GET",
    url: "http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99",
    data: {},
    success: function (response) {
        let mise_list = response["RealtimeCityAir"]["row"];
        for (let i = 0; i < mise_list.length; i++) {
            let mise = mise_list[i];
            let gu_name = mise["MSRSTE_NM"];
            let gu_mise = mise["IDEX_MVL"];

            if (gu_mise > 50) {
                console.log(gu_name, gu_mise);
            };
        }
    },
});


//가장 큰수
let numbers = [1, 3, 5, 2, 4];
let number_max = 0;
for (let i = 0; i < numbers.length; i++) {
    if (number_max < numbers[i]) {
        number_max = numbers[i]
    }
}
console.log(number_max)


//가장 미세먼지 농도가 높은 도시 추출

