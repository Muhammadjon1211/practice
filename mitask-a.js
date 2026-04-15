// MITASK-A
/*
Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi 
letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/


//SOLUTIION
const letterCount = (lett, word) => {
    if (typeof lett === "string" && lett.length === 1) {
        if (typeof word === 'string') {
            let number = 0;
            for (let i = 0; word.length > i; i++) {
                if (lett === word[i]) {
                    number += 1
                }
            } 
            return number
        } else {
            console.log("Please ender a word as a second argument")
        }
    } else {
        console.log("Please enter a single letter as a first argument")
    }
}

const result = letterCount("m", "muhammad")
console.log(result)