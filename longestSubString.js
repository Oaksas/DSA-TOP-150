function longestSubString(s) {
    if (s.length == 0) {
        return "Empty String"
    }
    let i = 0
    let end = 1
    let letterMap={}

    for(end = end;end<s.length;end++){
        if(letterMap[s[end]]){
            
        }
    }

    while (end < s.length) {
        if (s[i] === s[end]) {
            i++
        }
        if(letterMap[s[end]]==0){
            letterMap[s[end]]++
        }
        end++
    }

    return s.slice(i, end)

}
console.log(longestSubString("aacaaacabc"))