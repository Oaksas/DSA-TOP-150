function maxSubArr(arr, k) {
    if (arr.length < 3) {
        return "Insufficient Array"
    }
    let init = 0
    let max = 2
    let maxSum = 0
    let maxArr = []

    while (max < arr.length) {


        if (maxSum < (arr[init] + arr[init + 1] + arr[max])) {
            maxSum = arr[init] + arr[init + 1] + arr[max]
            maxArr = [arr[init], arr[init + 1], arr[max]]
        }
        else {
            init++
            max++
        }
    }

    return maxArr


}

console.log(maxSubArr([4, 2, 1, 7, 8, 1, 2, 8, 1, 11], 3))
